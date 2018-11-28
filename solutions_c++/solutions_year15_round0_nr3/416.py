#include <cstdio>
#include <string>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
#define I 2
#define J 3
#define K 4
using namespace std;
typedef long long ll;
int t=1;
const int multi[5][5] = {{0,0,0,0,0},
					     {0,1,I,J,K},
					     {0,I,-1,K,-J},
					     {0,J,-K,-1,I},
					     {0,K,J,-I,-1},
					    };
int dp[111111];
string s;

inline int inter(char c)
{
	if( c == 'i' ) return I;
	else if( c == 'j' ) return J;
	else return K;
}

void solve()
{
	ll l,x;
	cin >> l >> x;
	if(x>4) x = x%4+4;
	cin >> s;
	int op=1;
	int temp=inter(s[0]);
	int a,b;
	dp[0]=temp;
	for( int i = 1 ; i < l*x ; i++ )
	{
		a = dp[i-1]; b = inter(s[i%s.length()]);
		if( a < 0 ) { a=-a; op=-1; }
		else op=1;
		temp = multi[a][b];
		dp[i] = temp*op;
	}
	bool s1=false,s2=false,s3=false;
	for( int i = 0 ; i < l*x ; i++ )
	{
		if(!s1&&dp[i]==I) s1=true;
		else if(s1&&!s2&&dp[i]==K){ s2=true; break; }
	}
	if(dp[l*x-1]==-1) s3=true;

	if(s1&&s2&&s3) cout << "Case #" << t << ": YES" << endl;
	else cout << "Case #" << t << ": NO" << endl;
	return;
}
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int tt;
	cin >> tt;
	for(t=1;t<=tt;t++)
	{
		memset(dp,0,sizeof(dp));
		solve();
	}
	return 0;
}