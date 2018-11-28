#include<iostream>
#include<vector>
#include<fstream>
#include<queue>
#include<algorithm>
#include<list>
#include<cstdio>
#include<stack>
#include<cstring>
#include <climits>
#include<cmath>
#include<string>
#include <functional>
#include<sstream>
#include<map>
#include<set>


#pragma comment(linker, "/STACK:100000000000000")

using namespace std;
#define     For(i,a,b)        for (int i=a; i<b; i++)
#define     Rep(i,a)          for (int i=0; i<a; i++)
#define     ALL(v)            (v).begin(),(v).end()
#define     Set(a,x)          memset((a),(x),sizeof(a))
#define     EXIST(a,b)        find(ALL(a),(b))!=(a).end()
#define     Sort(x)           sort(ALL(x))
#define     UNIQUE(v)         Sort(v); (v).resize(unique(ALL(v)) - (v).begin())
#define     MP                make_pair
#define     SF                scanf
#define     PF                printf
#define     MAXN              1001
#define     MAXM              1001
#define     MOD               1000000007
#define     Dbug             cout<<"";
#define     EPS              1e-15
typedef long long ll;
typedef pair<int,int> pii;
int a, b, k, n;
vector<int> v1, v2, v3;
vector<int> bin(int x)
{
	vector<int> v;
	while(x) v.push_back(x&1), x/=2;
	reverse(ALL(v));
	return v;
}
vector<int> add(int x, vector<int> v)
{
	vector<int> ret;
	Rep(i, x-v.size()) ret.push_back(0);
	Rep(i, v.size()) ret.push_back(v[i]);
	return ret;
}
ll dp[40][2][2][2];
ll rec(int p, bool a, bool b, bool c)
{
	if(p==n) return 1;
	if(~dp[p][a][b][c]) return dp[p][a][b][c];
	ll ret=0;
	int x1=a, x2=b, x3=c;
	if(v3[p]==1) x3=1;
	if(v2[p]==1) x2=1;
	if(v1[p]==1) x1=1;
	if(v1[p]==1 || a) ret+=rec(p+1, a, x2, x3);
	ret+=rec(p+1, x1, x2, x3);
	if(v2[p]==1 || b) ret+=rec(p+1, x1, b, x3);
	if(v3[p]==1 || c)
	{
		if(v2[p]==1 && v1[p]==1) ret+=rec(p+1, a, b, c);
		else if(v2[p]==1 && (v1[p]==0 && a)) ret+=rec(p+1, a, b, c);
		else if(v2[p]==0 && b && v1[p]==1) ret+=rec(p+1, a, b, c);
		else if(v2[p]==0 && b && a && v1[p]==0) ret+=rec(p+1, a, b, c);
	}
	return dp[p][a][b][c]=ret;
}
int main(){
	//ios_base::sync_with_stdio(false);
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);

	int tc=1, t;
	cin>>t;
	while(t--)
	{
		cin>>a>>b>>k;
		a--, b--, k--;
		v1=bin(a), v2=bin(b), v3=bin(k);
		int mx=max(v1.size(), max(v2.size(), v3.size()));
		if(v1.size()<mx) v1=add(mx, v1);
		if(v2.size()<mx) v2=add(mx, v2);
		if(v3.size()<mx) v3=add(mx, v3);
		n=mx;
		Set(dp, -1);
		ll ans=rec(0, 0, 0, 0);
		PF("Case #%d: ", tc++);
		cout<<ans<<endl;
	}
	return 0;
}