#include <fstream>

using namespace std;

char word[1001];
bool pancakes[1001];

int convertWordToBool()
{
    int i = 0;
    while (word[i] != '\0')
    {
        pancakes[i] = word[i] == '+';
        i++;
    }
    return i;
}

int computeMinNumberOfFlips(int k, int l)
{
    int i, j;
    int limit = l - k + 1;
    int number = 0;
    for (i = 0; i < limit; i++)
    {
        if (!pancakes[i])
        {
            number++;
            for (j = 0; j < k; j++)
                pancakes[i + j] = !pancakes[i + j];
        }
    }
    for (; i < l; i++)
        if (!pancakes[i])
            return -1;
    return number;
}

int main()
{
    int t, l, k, minNumber;
    ifstream f("flipper.in");
    ofstream g("flipper.out");
    f >> t;
    for (int i = 0; i < t; i++)
    {
        f >> word >> k;
        l = convertWordToBool();
        minNumber = computeMinNumberOfFlips(k, l);
        g << "Case #" << i + 1 << ": ";
        if (minNumber >= 0)
            g << minNumber;
        else
            g << "IMPOSSIBLE";
        g << '\n';
    }
    return 0;
}