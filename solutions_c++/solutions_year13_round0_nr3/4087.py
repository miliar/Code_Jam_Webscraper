#include <algorithm>
#include <iostream>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <ctime>
#include <stack>
#include <queue>
#include <map>
#include <set>

#define f first
#define s second
#define mp make_pair
#define pb push_back

#define ll long long

#define MIN(aa,bb) ((aa) < (bb) ? (aa) : (bb))
#define MAX(aa,bb) ((aa) > (bb) ? (aa) : (bb))
#define MIN3(aa,bb,cc) MIN((aa),MIN((bb),(cc)))
#define MAX3(aa,bb,cc) MAX((aa),MAX((bb),(cc)))

#define ABS(aa) ((aa) > 0 ? (aa) : -(aa))

#define INF INT_MAX
#define LINF 1000000000000000
#define KINF 1000000000
#define eps 1e-9

#define ii pair <int,int>
#define p_q priority_queue
#define vint vector <int>
#define vii vector <ii>
#define sint set <int>
#define sii	set <ii>

#define Kare(aa)	((aa) * (aa))
#define e(aa,bb) (ABS((aa) - (bb)) < eps)
#define all(aa)	aa.begin(),aa.end()
#define sz size()
#define csz(a) strlen(aa)
#define clr(aa) memset(aa,0,sizeof aa) 

using namespace std;

ll T,A,B;
vector <ll> V;
ll Solve(ll x)
{
	ll i,s=0;
	for(i=0;i<V.size();i++)
		if(V[i] <= x)
			s++;
		else
			break;
	return s;
}
void Read()
{
	ll i;
	scanf("%lld",&T);
	for(i=1;i<=T;i++)
	{
		scanf("%lld %lld",&A,&B);
		printf("Case #%lld: %lld\n",i,Solve(B)-Solve(A-1));
	}
}
bool isPal(ll x)
{
	ll i,L=0;
	ll D[30];
	while(x)
	{
		D[++L]=x%10;
		x/=10;
	}
	for(i=1;i<=L/2;i++)
		if(D[i] != D[L-i+1])
			return 0;
	return 1;
}
void Init()
{
	ll i;
	for(i=1;i<=10000000;i++)
		if(isPal(i) && isPal(i*i))
			V.pb(i*i);
}
int main()
{
	Init();
	Read();
	return 0;
}
