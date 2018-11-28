#include <iostream>
#include <fstream>

using namespace std;

struct Quaternion
{
    char value;
    bool sign;  // 0 = positive, 1 = negative
    Quaternion(){}
    Quaternion(char c)
    {
        value = c;
        sign = false;
    }
    void multiply(Quaternion& q)
    {
        if (value == 'a')
        {
            value = q.value;
            sign = (sign ^ q.sign);
        }
        else if (q.value == 'a')
        {
            sign = (sign ^ q.sign);
        }
        else if (value == q.value)
        {
            value = 'a';
            sign = !(sign ^ q.sign);
        }
        else
        {
            if ((value == 'i') && (q.value == 'j'))
            {
                value = 'k';
                sign = (sign ^ q.sign);
            }
            else if ((value == 'i') && (q.value == 'k'))
            {
                value = 'j';
                sign = !(sign ^ q.sign);
            }
            else if ((value == 'j') && (q.value == 'i'))
            {
                value = 'k';
                sign = !(sign ^ q.sign);
            }
            else if ((value == 'j') && (q.value == 'k'))
            {
                value = 'i';
                sign = (sign ^ q.sign);
            }
            else if ((value == 'k') && (q.value == 'i'))
            {
                value = 'j';
                sign = (sign ^ q.sign);
            }
            else if ((value == 'k') && (q.value == 'j'))
            {
                value = 'i';
                sign = !(sign ^ q.sign);
            }
        }
    }
};

int N, T, L, X, j;
char target;
string result, line;
bool starting;
Quaternion* q1;

void performCheck()
{
    while ((q1->sign == false) && (q1->value == target))
    {
        if (target == 'k')
        {
            if ((N == X - 1) && (j == L - 1))
            {
                result = "YES";
                target = ' ';
            }
            else
            {
                break;
            }
        }
        else
        {
            if (j == L - 1)
            {
                starting = true;
            }
            else
            {
                delete(q1);
                j++;
                q1 = new Quaternion(line[j]);
            }
            if (target == 'i')
            {
                target = 'j';
            }
            else if (target == 'j')
            {
                target = 'k';
            }
        }
    }
}

int main()
{
    ifstream input ("input.in");
    if (input.is_open())
    {

        ofstream output ("output.out");
        input >> T;
        for (int i = 0; i < T; i++)
        {
            result = "NO";
            input >> L >> X;
            input >> line;
            if(L * X >= 3)
            {
                starting = true;

                target = 'i';
                for (N = 0; N < X; N++)
                {
                    j = 0;
                    if (starting)
                    {
                        q1 = new Quaternion(line[0]);
                        performCheck();
                        j++;
                        starting = false;
                    }
                    for (; j < L; j++)
                    {
                        Quaternion q2(line[j]);
                        q1->multiply(q2);
                        performCheck();
                    }
                }
            }
            output << "Case #" << i + 1 << ": " << result << endl;
        }
    input.close();
    output.close();
    }
    return 0;
}
