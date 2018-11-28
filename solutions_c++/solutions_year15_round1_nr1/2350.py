#include <cstdio>
#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <cstring>

using namespace std;

const int maxn = 1010;
const int MOD = 1e9+7;

#define rep(i, x, y) for (int i=x; i<=y; i++)
#define mset(arr) memset(arr, 0, sizeof(arr))  

int T, N;
int m[maxn];

int main() {
		
	freopen("a.in", "r", stdin);
	freopen("b.out", "w", stdout);

	cin>>T;
	for (int kase = 1; kase <= T; ++kase)
	{
		cin>>N;
		for (int i = 0; i < N; ++i)
			cin>>m[i];


		int ans1 = 0;
		for (int i = 0; i < N-1; ++i)
		{
			if (m[i] > m[i+1])
			{
				ans1 += m[i] - m[i+1];
			}
		}

		int ans2 = 0, maxcut = 0;
		for (int i = 0; i < N-1; ++i)
		{
			if (m[i] > m[i+1])
			{
				maxcut = max(m[i] - m[i+1], maxcut);
			}
		}
		for (int i = 0; i < N-1; ++i)
		{
			ans2 += min(m[i], maxcut);
		}

		printf("Case #%d: ", kase);
		cout<<ans1<<" "<<ans2<<endl;
	}
	return 0;
}
