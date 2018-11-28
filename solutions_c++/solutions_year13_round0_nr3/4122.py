// c.cpp:
// By Andrew Moskalchuk (HorgH) 
//
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <map>
#include <set>
#pragma comment(linker,"/STACK:16777216")
using namespace std;

//Loops
#define FOR(i,a,b) for(int (i) = (a); (i) <= (b); ++(i))
#define ROF(i,a,b) for(int (i) = (a); (i) >= (b); --(i))
#define rep(i,n) for (int (i) = 0; (i) < (n); ++(i))
#define fe(i,a) for (int (i) = 0; (i) < int((a).size()); ++(i))
#define MEM(a,b) memset((a),(b),sizeof(a))

//Constants
#define inf 1000000000
#define pi 2*acos(0.0)
#define N 100010
#define  MAX 10000000
#define eps 1e-9

//Functions
#define pb push_back
#define ppb pop_back
#define all(c) (c).begin(), (c).end()
#define sz(x) int((x).size())
#define sqr(a) (a)*(a)

//Pairs
#define mp(a,b) make_pair((a), (b))
#define X first
#define Y second

//Input-Output
#define FREOPEN(a,b) freopen(a,"r",stdin); freopen(b,"w",stdout);

typedef vector<int> vint;
typedef long long ll;
typedef pair<int, int> pii;


vector<ll> pal;
bool pali[MAX+10]={0};
bool good(ll x)
{
	ll y=ll(sqrt(double(x)));
	if(y*y == x) return  pali[y];
	return false;
}
int main()
{
    FREOPEN("input.txt","output.txt");
    int test,ans;
	ll l,r,x,y,i;
	scanf("%d",&test);
	FOR(i,1,9)
	{
		pali[i]=true;
		if(good(i))pal.pb(i);
	}
	i=1;
	while(i<=MAX)
	{
		x=y=i;
		while(y)
		{
			x=x*10+y%10;
			y/=10;
		}
		if(x<=MAX)pali[x]=true;
		if(good(x))pal.pb(x);
		if(i<=MAX/10)
		{
			rep(c,10)
			{
				x=y=i;
				x=x*10+c;
				while(y)
				{
					x=x*10+y%10;
					y/=10;
				}
				if(x<=MAX)pali[x]=true;
				if(good(x))pal.pb(x);
			}
		}
		i++;
	}
	//fe(i,pal)printf("%I64d\n",pal[i]);
	rep(tt,test)
	{
		scanf("%I64d%I64d",&l,&r);
		ans=0;
		fe(i,pal)
			if(pal[i]>=l && pal[i]<=r)ans++;
		printf("Case #%d: %d\n",tt+1,ans);
	}
	return 0;   
}
/*
1
2
3
4
5
6
7
8
9
121
484
10201
12321
14641
40804
44944
1002001
1234321
4008004
100020001
102030201
104060401
121242121
123454321
125686521
400080004
404090404
10000200001
10221412201
12102420121
12345654321
40000800004
1000002000001
1002003002001
1004006004001
1020304030201
1022325232201
1024348434201
1210024200121
1212225222121
1214428244121
1232346432321
1234567654321
4000008000004
4004009004004

*/
