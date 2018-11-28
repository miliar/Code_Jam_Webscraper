#include <fstream>
#include <vector>
#include <bitset>
using namespace std;

const unsigned long long maxValue = 10000001;

void buildMatrix(vector< vector<string> > &qMatrix);
inline string delta(string line, string col, vector< vector<string> > &qMatrix);
inline int getPos(string a);

int main()
{
    vector< vector<string> > qMatrix(4, vector<string>(4));
    buildMatrix(qMatrix);
    int T, i;
    long long X, L, j, k, l, product;
    string line;
    bool possible;
    string first, second, third;
    ifstream f("input.in");
    f >> T;
    bitset<maxValue> b;
    ofstream g("output.out");
    for (i = 1; i <= T; i++)
    {
        f >> L >> X;
        f >> line;
        product = L * X;
        possible = false;
        first = second = third = "";
        b.reset();
        for (j = 0; j < product; j++)
        {
            first = delta(first, string(1, line[j % L]), qMatrix);
            if (first == "i")
                b[j + 1] = 1;
        }

        for (j = product - 1; j >= 0 && !possible; j--)
        {
            third = delta(string(1, line[j % L]), third, qMatrix);
            if (third == "k")
            {
                second = "";
                for (k = j - 1; k >= 0 && !possible; k--)
                {
                    second = delta(string(1, line[k % L]), second, qMatrix);
                    if (b[k] && second == "j")
                        possible = true;
                }
            }
        }

        g << "Case #" << i << ": ";
        if (possible)
            g << "YES";
        else
            g << "NO";
        g << '\n';
    }
    return 0;
}

void buildMatrix(vector< vector<string> > &qMatrix)
{
    qMatrix[0][0] = "1";
    qMatrix[0][1] = "i";
    qMatrix[0][2] = "j";
    qMatrix[0][3] = "k";

    qMatrix[1][0] = "i";
    qMatrix[1][1] = "-1";
    qMatrix[1][2] = "k";
    qMatrix[1][3] = "-j";

    qMatrix[2][0] = "j";
    qMatrix[2][1] = "-k";
    qMatrix[2][2] = "-1";
    qMatrix[2][3] = "i";

    qMatrix[3][0] = "k";
    qMatrix[3][1] = "j";
    qMatrix[3][2] = "-i";
    qMatrix[3][3] = "-1";
}

inline string delta(string line, string col, vector< vector<string> > &qMatrix)
{
    if (line == "")
        return col;
    else if (col == "")
        return line;
    else
    {
        bool negative = false;
        string result = "";

        if (line.size() > 1)
            negative = true, line = line[1];
        if (col.size() > 1)
            negative = true, col = col[1];
        result = qMatrix[getPos(line)][getPos(col)];
        if (negative)
            result = "-" + result;
        if (result.size() > 2 && result[0] == result[1])
            result = result[2];
        return result;
    }
}

inline int getPos(string a)
{
    if (a == "1")
        return 0;
    else if (a == "i")
        return 1;
    else if (a == "j")
        return 2;
    else if (a == "k")
        return 3;
    return -1;
}
