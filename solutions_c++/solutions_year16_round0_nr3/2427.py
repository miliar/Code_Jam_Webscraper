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
vector<string> ans;
vector<int> ans1[100];
LL sum[20][20];
int n, k;
inline LL _pow(LL x, int m)
{
	LL ret = 1;
	for (int i = 1; i <= m; i++) ret *= x;
	return ret;
}
inline LL isprime(LL x)
{
	for (LL i = 2; (LL)i*i <= x; i++)
	{
		if (x%i == 0){ return i; }
	}
	return 0;
}
int main()
{
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("C-small-attempt1.out", "w", stdout);
	cin.tie(NULL);
	int t; cin >> t;
	for (int kcase = 1; kcase <= t; kcase++)
	{
		cin >> n >> k;
		string s = "1000000000000001";
		string s1 = "1000000000000001";
		mem(sum);
		for (int base = 2; base <= 10; base++)
		{
			for (int i = 1; i <= 14;i++)
			{
				sum[base][i] =sum[base][i-1]+ _pow((LL)base, i);
			}
		}
		vector<LL> temp;
		vector<LL> l;
		int h = 0;
		for (int i = 1; i <= 14; i++)
		{
			bool ok = false;
			for (int j = 1; j <=i; j++){
				ok = false;
				LL u = 0, v = 0;
				for (int base = 2; base <= 10; base++)
				{
					u = sum[base][i] - sum[base][j - 1];
					u++;
					u += _pow((LL)base, 15);
					 v = sum[2][i] - sum[2][j - 1];
					if (isprime(u)){ temp.push_back(isprime(u)); }
					else{ ok = true; temp.clear(); break; }
				}
				if (!ok)
				{
					while (v != 0)
					{
						int r = v % 2;
						l.push_back(r);
						v /= 2;
					}
					for (int c = 0; c < l.size(); c++)
					{
						if (l[c] == 1) s[n-c-1] ='1';
					}
					ans.push_back(s); s = s1;
					for (int w = 0; w < 9; w++) ans1[h].push_back(temp[w]);
					h++;
					temp.clear();
					l.clear();
				}
			}
		}
		printf("Case #%d:\n", kcase);
		for (int i = 0; i < k; i++)
		{
			cout << ans[i] << " ";
			for (int j = 0; j < 9; j++) cout << ans1[i][j] << " ";
			cout << endl;
		}
	}
	//system("pause");
	return 0;
}