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
string t[10];
vector < VI > V;
void rek(int x,VI X)
{
if(x==m+1)
	{
	V.PB(X);	
	return;
	}
for(int i=1;i<=n;i++)
	{
	X.PB(i);
	rek(x+1,X);
	X.pop_back();
	}
}
map<string,int> M[5];
void add(string a,int x)
{
string b="";
M[x][b]=1;
for(int i=0;i<a.size();i++)
	{
	b=b+a[i];
	M[x][b]=1;
	}
}
void solve()
{
scanf("%d%d",&m,&n);
for(int i=1;i<=m;i++)
	{
	cin>>t[i];
	}
rek(1,VI());
int wynik=0;
int ile=0;
for(int i=0;i<V.size();i++)
	{
	for(int j=0;j<V[i].size();j++)
		{
		add(t[j+1],V[i][j]);
		}
	a=0;
	for(int i=1;i<=n;i++)
		{
		a+=M[i].size();
		M[i].clear();
		}
	if(a>wynik)
		{
		wynik=a;
		ile=0;
		}
	if(wynik==a)ile++;
	}
printf("%d %d\n",wynik,ile);
V.clear();
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
