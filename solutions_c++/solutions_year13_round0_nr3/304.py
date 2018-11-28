#include <cmath>
#include <cstring>
#include <iostream>
#include <QtGlobal>
using namespace std;

#include <QFile>
#include <QVector>
#include <QTextStream>

QTextStream input, output;

QVector<char*> data;

/* Inverts order of symbols in the string */
void Invert(char x[])
{
    uint size = strlen(x);
    for(uint i = 0; i < size / 2; ++i)
    {
        char tmp = x[i];
        x[i] = x[size - i - 1];
        x[size - i - 1] = tmp;
    }
}

bool IsPalindrome(char digits[])
{
    int size = strlen(digits);
    for(int i = 0, mid = (size - 1) / 2; i <= mid; ++i)
        if(digits[i] != digits[size - i - 1]) return false;
    return true;
}

void Add(char x[], uint &ndigits, quint64 val, uint shift)
{

    if(val == 0) return;

    while(ndigits <= shift)
    {
        x[ndigits] = '0';
        ++ndigits;
    }

    while(val > 0)
    {
        if(shift == ndigits)
        {
            x[shift] = '0';
            ++ndigits;
        }
        val += x[shift] - '0';
        x[shift] = '0' + val % 10;
        ++shift; val /= 10;
    }

    x[ndigits] = '\0';

}

quint64 GetBlock(char x[], uint shift, uint size)
{
    uint factor = 1;
    quint64 res = 0;
    while((size > 0) && (x[shift] != '\0'))
    {
        res += factor * (x[shift] - '0');
        ++shift; --size;
        factor *= 10;
    }
    return res;
}

bool FastTest(char x[])
{
    uint sum = 0, i = 0, size = strlen(x);
    while((sum < 10) && (i < size))
    {
        uint digit = x[i] - '0';
        sum += digit * digit;
        ++i;
    }
    return sum < 10;
}

void Square(char src[], char res[])
{
    static uint block_size = 8;
    res[0] = '\0';
    uint src_size = strlen(src), res_size = 0;
    for(uint i = 0; i <= src_size / block_size; ++i)
    {
        quint64 block_i = GetBlock(src, i * block_size, block_size);
        for(uint j = i; j <= src_size / block_size; ++j)
        {
            quint64 block_j = GetBlock(src, j * block_size, block_size);
            if(block_i * block_j > 0)
            {
                Add(res, res_size,
                    block_i * block_j * (i == j ? 1 : 2),
                    (i + j) * block_size);
            }
        }
    }
}

/* Assumes that p is palindrome! */
void NextPalindrome(char p[])
{
    int size = strlen(p);
    int a = (size - 1) / 2, b = size - a - 1;
    do
    {
        if(p[a] < '2')
        {
            ++p[a];
            if(b != a) ++p[b];
            return;
        }
        else if((p[a] == '2') && (size == 1))
        {
            p[a] = '3';
            return;
        }
        else
        {
            p[a--] = '0';
            p[b++] = '0';
        }
    } while(a >= 0);
    memset(p, '0', size + 1);
    p[0] = '1';
    p[size] = '1';
    p[size + 1] = '\0';
}

/*
 *  Assumes that p is such palindrome, that p^2 is also palindrome,
 *  and turns p into next greater palindrome having such property.
*/
void NextValidPalindrome(char p[], int &checksum)
{
    uint size = strlen(p);
    if(size > 2)
    {
        bool repeat = false;
        int a = (size - 1) / 2, b = size - a - 1;
        do
        {
            repeat = false;
            if(a != b)
            {
                if((p[a] == '0') && (checksum > 7))
                {
                    do --a; while((p[a] == '0') && (a >= 0));
                    b = size - a - 1;
                }
                if((p[a] < '2'))
                {
                    ++p[a]; ++p[b];
                    uint digit = p[a] - '0';
                    checksum += 4 * digit - 2;
                }
                else
                {
                    p[a--] = '0';
                    p[b++] = '0';
                    checksum -= 8;
                    repeat = true;
                }
            }
            else if(a == b)
            {
                if((p[a] == '0') && (checksum > 8))
                {
                    do --a; while((p[a] == '0') && (a >= 0));
                    b = size - a - 1;
                }
                if(p[a] < '2')
                {
                    ++p[a];
                    uint digit = p[a] - '0';
                    checksum += 2 * digit - 1;
                }
                else
                {
                    p[a--] = '0';
                    ++b; checksum -= 4;
                    repeat = true;
                }
            }
        } while((repeat || (checksum > 9) ) && (a >= 0));
        if(a < 0)
        {
            memset(p, '0', size + 1);
            p[0] = '1'; p[size] = '1';
            p[size + 1] = '\0';
            checksum = 2;
            cout << "new size = " << size + 1 << endl;
        }
    }
    else if(size == 1)
    {
        if      (p[0] == '1')
        {
            p[0] = '2';
            checksum = 4;
        }
        else if (p[0] == '2')
        {
            p[0] = '3';
            checksum = 9;
        }
        else
        {
            strcpy(p, "11");
            checksum = 2;
        }
    }
    else /* size == 2 */
    {
        if(strcmp(p, "11") == 0)
        {
            strcpy(p, "22");
            checksum = 8;
        }
        else
        {
            strcpy(p, "101");
            checksum = 2;
        }
    }

}

int Compare(char first[], char second[])
{
    uint size_first = strlen(first);
    uint size_second = strlen(second);
    if(size_first < size_second) return -1;
    else if(size_first > size_second) return 1;
    for(int i = size_first - 1; i >= 0; --i)
    {
        if(first[i] < second[i]) return -1;
        else if(first[i] > second[i]) return 1;
    }
    return 0;
}

void GenerateData(quint64 max)
{
    int checksum = 1;
    char p[102] = "1", square[102], limit[102];
    memset(limit, '9', (max + 1) / 2);
    limit[(max + 1) / 2] = '\0';
    do
    {



        /*
        if(FastTest(p))
        {
            char *tmp = new char [2 * strlen(p) + 1];
            Square(p, tmp);
            data.append(tmp);
            cout << p << " - " << tmp << endl;
        }
        */

        /*
        Square(p, square);
        if(IsPalindrome(square))
        {
            uint size = strlen(square) + 1;
            char *tmp = new char [size];
            memcpy(tmp, square, size);
            cout << p << " - " << square << endl;
            data.append(tmp);
        }


        NextPalindrome(p);
        */

        char *tmp = new char [2 * strlen(p) + 1];
        Square(p, tmp);
        data.append(tmp);
        //cout << p << " - " << checksum << " - " << tmp << endl;
        NextValidPalindrome(p, checksum);

    } while(Compare(p, limit) <= 0);

}

void SolveCase()
{
    static char A[102], B[102];
    input >> A >> B;
    Invert(A);
    Invert(B);
    int res = 0;
    QVector<char*>::ConstIterator i = data.constBegin(), end = data.constEnd();
    while((i != end) && (Compare(*i, A) < 0)) ++i;
    while((i != end) && (Compare(*i, B) <= 0))
    {
        ++res;
        ++i;
    }
    output << res << endl;
}

int main(int argc, char *argv[])
{
    Q_UNUSED(argc);
    Q_UNUSED(argv);

    /*
    char a[] = "1001";
    char b[] = "1001";
    cout << Compare(a, b) << endl;
    return 0;
*/

    GenerateData(100);

    QFile infile("input.txt"), outfile("output.txt");
    infile.open(QIODevice::ReadOnly);
    outfile.open(QIODevice::WriteOnly);
    input.setDevice(&infile);
    output.setDevice(&outfile);

    uint T; input >> T;
    for(uint t = 1; t <= T; ++t)
    {
        output << "Case #" << t << ": ";
        SolveCase();
    }

    return 0;
}
