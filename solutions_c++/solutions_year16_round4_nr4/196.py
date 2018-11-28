#include <cmath>
#include <cstdio>
#include <cstring>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <vector>
#include <string>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long ll;

#define ALL(c) (c).begin(),(c).end()
#define SORT(a) sort(a.begin(), a.end())
#define UNIQ(a) a.resize(unique(a.begin(), a.end()) - a.begin())

#define MAXN 32

int N;
int a[MAXN][MAXN];
int maskw[MAXN] = {0};
int masko[MAXN] = {0};

int brute_rec(int d)
{
	if(d == N)
	{
		return 1;
	}

	int ret = 0;
	for(int iw=0; iw<N; ++iw) if(maskw[iw] == 0)
		for(int io=0; io<N; ++io) if(masko[io] == 0 && a[iw][io])
		{
			maskw[iw] = 1;
			masko[io] = 1;

			int v = brute_rec(d+1);

			maskw[iw] = 0;
			masko[io] = 0;

			if(v == 0)
			{
				return 0;
			}
			ret = 1;
		}
	return ret;
}

int brute()
{
	return brute_rec(0);
}

int main() {
	int t;
	
	cin >> t;
	for(int tt=1; tt<=t; ++tt)
	{
		cin >> N;
		vector<string> s(N);
		int a0[MAXN][MAXN];
		for(int i=0; i<N; ++i)
		{
			cin >> s[i];
			for(int j=0; j<N; ++j)
				a0[i][j] = s[i][j] == '1' ? 1 : 0;
		}
		
		int ans = 999999;

		for(int c=0; c<(1<<(N*N)); ++c)
		{
			int pay = 0;
			for(int y=0,j=0; y<N; ++y)
				for(int x=0; x<N; ++x,++j)
				{
					a[y][x] = a0[y][x];
					if((c>>j)&1)
					{
						++pay;
						a[y][x] = 1;
					}
				}
			if(brute())
			{
				//print2(pay, c);
				ans = min(ans, pay);
			}
		}
		
		cout << "Case #" << tt << ": " << ans << "\n";
		cout.flush();
	}

	return 0;
}
