#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

typedef long long ll;



void solve()
{
	int n, x;
    cin >> n >> x;
    vector<int> files(n);
    for (int i = 0; i < n; ++i)
    {
        cin >> files[i];
    }
    sort(files.begin(), files.end());
    vector<bool> used(n, false);
    int ans = 0;
    for (int i = n - 1; i >= 0; --i)
    {
        if (!used[i])
        {
            used[i] = true;
            ++ans;
            for (int j = i - 1; j >= 0; --j)
            {
                if (!used[j] && files[i] + files[j] <= x)
                {
                    used[j] = true;
                    break;
                }
            }
        }
    }
    cout << ans;
}

void main()
{
	freopen("i.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}
}