#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int TC;
    cin >> TC;
    for (int tc = 1; tc <= TC; tc++)
    {
        int N, S;
        cin >> N >> S;
        vector<int> v;
        for (int i = 0; i < N; i++)
        {
            int x;
            scanf("%d", &x);
            v.push_back(x);
        }
        sort(v.begin(), v.end());

        int ans = 0;
        int p = 0;
        for (int i = N - 1; i >= p; i--)
        {
            if (v[i] + v[p] <= S) p++;
            ans++;
        }
        cout << "Case #" << tc << ": " << ans << endl;
    }
}
