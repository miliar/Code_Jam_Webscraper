#include <bits/stdc++.h>
using namespace std;
typedef vector<int> vi; typedef pair<int,int> pii; typedef vector<pair<int,int> > vpii;
typedef long long ll; typedef vector<long long> vl; typedef pair<long long,long long> pll;
typedef vector<pll> vpll;typedef vector<string> vs; typedef double D; typedef vector<bool> vb;
typedef pair<ll,pll> pip;
#define sz(v) int((v).size())
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define F first
#define S second
#define sd(x) scanf("%d", &x)
#define slld(x) scanf("%I64d", &x)
#define debug(X) cerr << "	--> " << #X << " = " << X << endl
#define present(c,x) ((c).find(x) != (c).end())
#define mod 1000000007LL
#define INF 2000000000LL
#define N 11234
#define int ll
#define num 20
char s[N];
char ar[2*num*N];
int m[4][4] = { {0,1,2,3},{1,4,3,6},{2,7,4,1},{3,2,5,4} };
int len[3];
map<char,int> mapp;
map<int,char> mp;
inline int multiply(char a, char b)
{
	return m[mapp[a]][mapp[b]];
}
void solve()
{
	int l,x;
	scanf("%lld%lld",&l,&x);
	scanf("%s",s);
	for(int i=0;i<3;++i)len[i] = -1;
	for(int i=0;i<l;++i)
	{
		for(int j=0;j<2*num;++j)
		{
			ar[i+j*l] = s[i];
		}
	}
	if(x>num+x%num)x=num+x%num;
	int cur = 0;
	for(int i=0;i<l*x;++i)
	{
		if(cur<4)		cur = multiply(mp[cur],ar[i]);
		else 			cur = (multiply(mp[cur-4],ar[i]) + 4)%8;
		if(cur==1)
		{
			len[0] = i;
			break;
		}
	}
	if(len[0]<0){printf("NO\n");return;}
	cur = 0;
	for(int i=len[0]+1;i<x*l;++i)
	{
		if(cur<4)		cur = multiply(mp[cur],ar[i]);
		else 			cur = (multiply(mp[cur-4],ar[i]) + 4)%8;
		if(cur==2)
		{
			len[1] = i;
			break;
		}
	}
	if(len[1]<0){printf("NO\n");return;}
	cur = 0;
	for(int i=len[1]+1;i<x*l;++i)
	{
		if(cur<4)		cur = multiply(mp[cur],ar[i]);
		else 			cur = (multiply(mp[cur-4],ar[i]) + 4)%8;
	}
	if(cur==3)printf("YES\n");
	else printf("NO\n");
}
#undef int
int main()
{

	freopen("C-large.in","r",stdin);
	freopen("ansC.txt","w",stdout);
	mapp['1'] = 0;
	mapp['i'] = 1;
	mapp['j'] = 2;
	mapp['k'] = 3;
	mp[0] = '1';
	mp[1] = 'i';
	mp[2] = 'j';
	mp[3] = 'k';
	int t = 1;
	scanf("%d",&t);
	for(int z=1;z<=t;++z)
	{
		printf("Case #%d: ",z);
		solve();
	}
	return 0;
}
/**
Code Walkthrough
Code Inspection:
N
return value of function
Overflow
**/


