#include <fstream>
#include <cmath>
#include <vector>
#include <limits>
using namespace std;

vector<string> searchSpace;

bool match(string &myString, string target)
{
    while (target.length() < myString.length())
        target = "0" + target;

    for (int i = 0; i < myString.length(); i++)
        if (myString[i] != '?' && myString[i] != target[i])
            return false;
    return true;
}

void printMin(string &C, string &J, ofstream &g)
{
    int minDiff = numeric_limits<int>::max(), solA = 0, solB = numeric_limits<int>::max(), a, b;
    int i, j;
    int length = C.size();
    int start, finish;
    if (length == 1)
    {
        start = 0;
        finish = 9;
    }
    else if (length == 2)
    {
        start = 0;
        finish = 99;
    }
    else if (length == 3)
    {
        start = 0;
        finish = 999;
    }

    for (i = start; i <= finish; i++)
        for (j = start; j <= finish; j++)
            if (match(C, searchSpace[i]) && match(J, searchSpace[j]))
        {
            a = stoi(searchSpace[i]);
            b = stoi(searchSpace[j]);
            if (abs(a - b) < minDiff)
                solA = a, solB = b, minDiff = abs(a - b);
        }

    int diffA = (solA == 0) ? length - 1 : length - ((int)log10(solA) + 1);
    int diffB = (solB == 0) ? length - 1 : length - ((int)log10(solB) + 1);
    for (i = 0; i < diffA; i++)
        g << 0;
    g << solA << " ";
    for (i = 0; i < diffB; i++)
        g << 0;
    g << solB << " ";
}

int main()
{
    int T, i, j;
    ifstream f("input.in");
    ofstream g("output.out");
    for (i = 0; i <= 999; i++)
        searchSpace.push_back(to_string(i));
    f >> T;
    string C, J;
    for (i = 1; i <= T; i++)
    {
        f >> C >> J;
        g << "Case #" << i << ": ";
        printMin(C, J, g);
        g << '\n';
    }
    f.close();
    g.close();
    return 0;
}
