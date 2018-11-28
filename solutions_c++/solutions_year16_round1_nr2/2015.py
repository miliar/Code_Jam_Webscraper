#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<cmath>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<bitset>
using namespace std;
#define mem(x) memset(x,0,sizeof x)
#define LL long long
#define all(o) (o).begin(),(o).end()
const int maxn = 3000;
int cnt[maxn];
int a[60];
int n;
vector<int> ans;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	cin.tie(NULL);
	int t; cin >> t;
	for (int kcase = 1; kcase <= t; kcase++)
	{
		cin >> n;
		mem(cnt);
		int maxi = 0;
		int mini = 1000000;
		ans.clear();
		for (int i = 1; i <= 2 * n - 1; i++)
		{
			for (int j = 1; j <= n; j++) scanf("%d", &a[j]);
			for (int j = 1; j <= n; j++){ maxi = max(a[j], maxi); mini = min(a[j], mini); }
			for (int j = 1; j <= n; j++){ cnt[a[j]]++; }
		}
		mem(a);
		for (int i = mini; i <= maxi; i++)
		{
			if (cnt[i] && (cnt[i] & 1)){ ans.push_back(i); }
		}
		sort(all(ans));
		printf("Case #%d: ", kcase);
		for (int i = 0; i < ans.size(); i++) cout << ans[i] << " ";
		cout << endl;
	}
	return 0;
}