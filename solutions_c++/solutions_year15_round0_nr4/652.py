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
void solve()
{
	int r,c,x;
	scanf("%d%d%d",&x,&r,&c);
	//printf("%d %d %d ---> ",x,r,c);
	if(r>c)swap(r,c);
	if(  ((r*c)%x>0)  ||  (c<x)  ||  (r<(x+1)/2) )
		printf("RICHARD\n");
	else if(r==(x+1)/2)
	{
		if(x%4)printf("GABRIEL\n");
		else printf("RICHARD\n");
	}
	else printf("GABRIEL\n");
}
int main()
{
	freopen("D-small-attempt3.in","r",stdin);
	//freopen("answer2.out","w",stdout);

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


