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
multiset <int> S;
void solve()
{
scanf("%d%d",&n,&x);
for(int i=1;i<=n;i++)
	{
	scanf("%d",&a);
	S.insert(a);
	}
wynik=0;
while(S.size())
	{
	wynik++;
	a=*(--S.end());
	S.erase(--S.end());

	if(S.size())
		{
		multiset<int>::iterator it=S.upper_bound(x-a);
		if(it==S.begin())continue;
		it--;
		S.erase(it);
		}	
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
