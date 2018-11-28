#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <vector>
#include <string>
#include <map>

using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T = 1;
    cin >> T;
    for (int nT = 1; nT <= T; ++nT)
    {
        int n, S;
        vector<int> vec;
        cin >> n >> S;
        for (int i = 0; i < n; ++i)
        {
            int num;
            cin >> num;
            vec.push_back(num);
        }
        sort(vec.begin(), vec.end());
        int result = 0;
        int pos = 0, end = vec.size() - 1;
        while (pos < end)
        {
            if (vec[pos] + vec[end] <= S)
                ++pos, --end, ++result;
            else
                --end;
        }
        result = vec.size() - result;
        printf("Case #%d: %d\n", nT, result);
    }

    return 0;
}