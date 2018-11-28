#include<cstdio>
#include<iostream>
#include<cmath>
#include<cstring>
#include<cstdlib>
#include<string>
#include<sstream>
#include<vector>
#include<algorithm>
#include<cassert>

using namespace std;

#define rep(i,n) for(int i = 0; i < (int)n; i++)
#define FOR(i,n,m) for(int i = (int)n; i <= (int)m; i++)
#define FOD(i,n,m) for(int i = (int)n; i >= (int)m; i--)
#define EACH(i,v) for(__typeof((v).begin()) i = (v).begin(); i != (v).end(); i++)

const int N = 50010;

string s;
int n,m,ans;
double f[2050*2050];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int CNT;
	cin>>CNT;
	FOR(cnt, 1, CNT)
	{
		cin>>s;
		n=s.length();
		m=1<<n;
		int init=0;
		rep(i,n)
			if (s[i] == 'X')
				init|=1<<i;
		double ans = 0;
		memset(f, 0, sizeof(f));
		f[init] = 1.0;
		FOR(msk, init, m - 2) {
			double p = f[msk] / n;
			int l = 0;
			while (msk & (1 << l)) l++;
			FOD(j, n - 1, 0) {
				if (msk & (1 << j)) l++;
				else l = 0;
				ans += p * (n - l);
				int x = j + l;
				if (x >= n) x -= n;
				f[msk | (1 << x)] += p;
			}
		}
		printf("Case #%d: %.10f\n", cnt, ans);
	}
}
