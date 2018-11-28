#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int sumDiff(vector<int>& m)
{
    int sum = 0;
    for(int i = 0; i < m.size() - 1; ++i)
    {
        if (m[i+1] < m[i])
        {
            sum += m[i] - m[i+1];
        }
    }
    return sum;
}

int maxDiff(vector<int>& m)
{
    int max = 0;
    for(int i = 0; i < m.size() - 1; ++i)
    {
        if (m[i+1] < m[i] && (m[i] - m[i+1]) > max)
        {
            max = m[i] - m[i+1];
        }
    }
    return max;
}

int possible(vector<int>& m, int maxDiff)
{
    int sum = 0;
    for(int i = 0; i < m.size() - 1; ++i)
    {
        if (m[i] > 0)
        {
            sum += (m[i] >= maxDiff) ? maxDiff : m[i];
        }
    }
    return sum;
}

int main()
{
    int T, N;
    cin >> T;
    for (int i = 1; i <= T; ++i)
    {
        cin >> N;
        vector<int> m(N);
        for (int j = 0; j < N; ++j)
        {
            cin >> m[j];
        }

        int first, second;
        first = sumDiff(m);
        int max_diff = maxDiff(m);
        second = possible(m, max_diff);
        printf("Case #%d: %d %d\n", i, first, second);
    }

    return 0;
}
