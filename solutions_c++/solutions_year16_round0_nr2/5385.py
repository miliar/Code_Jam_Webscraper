#include<iostream>
#include<vector>
#include<string>
using namespace std;

string str;

long long fromItoJ(int i, int j, bool isPositive)
{
    if((isPositive && i > j) || (!isPositive && i < j))
        return 0;

    char refPlus = isPositive ? '+' : '-';
    int step = isPositive ? 1 : -1;

    if (str[j] == refPlus)
    {
        return fromItoJ(i, j - step, isPositive);
    }
    else
    {
        if (str[i] == refPlus)
        {
            int temp = 0;
            while (str[i] == refPlus)
            {
                i += step;
                temp++;
            }
            return 1 + 1 + fromItoJ(j, i, !isPositive);
        }
        else
            return 1 + fromItoJ(j, i + 1, !isPositive);
    }
}

inline long long test()
{
    return fromItoJ(0, str.size() - 1, true);
}

int main()
{
    int caseCount;
    cin >> caseCount;
    for (int i = 1; i <= caseCount; ++i)
    {
        cin >> str;
        long long result = test();
        cout << "Case #" << i << ": " << result << endl;
    }

    return 0;
}

