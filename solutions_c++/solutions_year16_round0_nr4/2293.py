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
LL k, c,s;
inline LL _pow(LL x, LL y)
{
	LL ret = 1;
	for (LL i = 1; i <= y; i++) ret *= x;
	return ret;
}

int main()
{
	freopen("D-small-attempt1.in", "r", stdin);
	freopen("D-small-attempt1.out", "w", stdout);
	cin.tie(NULL);
	int t; cin >> t;
	for (int kcase = 1; kcase <= t; kcase++)
	{
		cin >> k >> c>>s;
		vector<LL> pos;
		LL u = _pow(k, c);
		if (k == 1)
		{
			printf("Case #%d: 1\n", kcase); continue;
		}
		LL r = (u - 1) / (k - 1);
		if (r == 1)
		{
			if (s <k){ printf("Case #%d: IMPOSSIBLE\n", kcase); continue; }
			else
			{
				printf("Case #%d: ", kcase);
				for (int i = 1; i <= k; i++) cout << i << " ";
				cout << endl; continue;
			}
		}
		for (LL i = 2; i <= u; i += r) pos.push_back(i);
		printf("Case #%d: ", kcase);
		if (pos.size()>=s)
		for (int i = 0; i < s; i++) cout << pos[i] << " ";
		else for (int i = 0; i < pos.size(); i++) cout << pos[i] << " ";
		cout << endl;
	}
	return 0;
}