#include<cstdio>
#include<iostream>
#include<cstring>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>
#include<sstream>
#include<set>
#include<climits>
#define gc getchar
#define f first
#define s second
#define TEST ll T = scan(); for(int t=1; t<=T; t++)
#define D(x) ll x = scan()
using namespace std;
typedef long long ll;
#define rep(i, n) for(ll i=0; i<n; i++)
ll scan() 
{
  char c = gc();
  while(c<'0' || c>'9') c = gc();
  ll ret = 0;
  while(c>='0' && c<='9') {
    ret = 10 * ret + c - 48;
    c = gc();
  }
  return ret;
}
int main()
{
	int sum[50][50];
	for (int i = 1; i < 21; i++) 
	{
		sum[i][i] = i;
		for (int j = i + 1; j <= 2 * i && j<21; j++)
			sum[i][j] = i + 1;
		for (int j = 2*i + 1; j < 21; j++) {
			sum[i][j] = sum[i][j - i] + 1;
		}
	}
	TEST
	{
		ll ans = 0;
		int r, c, w;
		cin >> r >> c >> w;
		if (r != 1) {
			ans = r - 1;
			ans *= c / w;
			if (c%w)
				ans += r - 1;
		}
		cout <<"Case #"<<t << ": " << ans + sum[w][c] << endl;
	}	
	return 0;
}
