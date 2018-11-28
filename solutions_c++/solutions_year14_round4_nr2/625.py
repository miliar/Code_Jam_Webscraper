#include<cstdio>
#include<iostream>
#include<algorithm>
#include<vector>
#include<tr1/unordered_map>
#include<queue>
#include<cstdlib>
#include<list>
#include<set>
#include<map>
#define MP make_pair
#define PB push_back
#define s second
#define f first
#define PII pair<int,int>
#define VPII vector <pair<int,int> >
#define VI vector <int>
#define abs(a) max((a),-(a))
#define LL long long
#define LD long double
#define ALL(x) x.begin(),x.end()
#define PU putchar_unlocked
#define GU getchar_unlocked
#define DBG(x) cerr<<#x<<" "<<(x)<<endl;
using namespace std;
int a,b,c,d,e,f,n,m,mx,l,z,r,k,x;
int wynik;
char ch;
int INF=1e9+1;
const int MXN=1e3+3;
int in[MXN];
void solve()
{
VPII V;
scanf("%d",&n);
for(int i=1;i<=n;i++)
	{
	scanf("%d",&in[i]);
	V.PB(MP(in[i],i));
	}
	wynik=0;
sort(ALL(V));
for(int i=0;i<V.size();i++)
	{
	PII a=V[i];
	b=0;
	c=0;
	for(int j=a.s-1;j>=1;j--)
		{
		if(in[j])b++;
		}
	for(int j=a.s+1;j<=n;j++)
		{
		if(in[j])c++;
		}
	wynik+=min(b,c);
	in[a.s]=0;
	}
printf("%d\n",wynik);
}
main()
{
scanf("%d",&z);
for(int i=1;i<=z;i++)
	{
	printf("Case #%d: ",i);
	solve();
	}

}
