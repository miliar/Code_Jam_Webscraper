#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <set>
#include <queue>
#include <map>
#include <cstdio>
#include <iomanip>
#include <sstream>
#include <iostream>
#include <cstring>
#include <complex>
#include <ctime>
#define REP(i,x,v)for(int i=x;i<=v;i++)
#define REPD(i,x,v)for(int i=x;i>=v;i--)
#define FOR(i,v)for(int i=0;i<v;i++)
#define FORE(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)
#define REMIN(x,y) (x)=min((x),(y))
#define REMAX(x,y) (x)=max((x),(y))
#define pb push_back
#define sz size()
#define mp make_pair
#define fi first
#define se second
#define ll long long
#define IN(x,y) ((y).find((x))!=(y).end())
#define un(v) v.erase(unique(ALL(v)),v.end())
#define LOLDBG
#ifdef LOLDBG
#define DBG(vari) cerr<<#vari<<" = "<<vari<<endl;
#define DBG2(v1,v2) cerr<<(v1)<<" - "<<(v2)<<endl;
#else
#define DBG(vari)
#define DBG2(v1,v2)
#endif
#define CZ(x) scanf("%d",&(x));
#define CZ2(x,y) scanf("%d%d",&(x),&(y));
#define CZ3(x,y,z) scanf("%d%d%d",&(x),&(y),&(z));
#define ALL(x) (x).begin(),(x).end()
#define tests int dsdsf;cin>>dsdsf;while(dsdsf--)
#define testss int dsdsf;CZ(dsdsf);while(dsdsf--)
using namespace std;
typedef pair<int,int> pii;
typedef vector<int> vi;
template<typename T,typename TT> ostream &operator<<(ostream &s,pair<T,TT> t) {return s<<"("<<t.first<<","<<t.second<<")";}
template<typename T> ostream &operator<<(ostream &s,vector<T> t){s<<"{";FOR(i,t.size())s<<t[i]<<(i==t.size()-1?"":",");return s<<"}"<<endl; }
int n,m;

char s[111][111];

char goup(int a,int b)
{
	a--;
	while(1)
	{
		if (s[a][b]!='.') return s[a][b];
		a--;
	}
}

char godown(int a,int b)
{
	a++;
	while(1)
	{
		if (s[a][b]!='.') return s[a][b];
		a++;
	}
}

char goleft(int a,int b)
{
	b--;
	while(1)
	{
		if (s[a][b]!='.') return s[a][b];
		b--;
	}
}

char goright(int a,int b)
{
	b++;
	while(1)
	{
		if (s[a][b]!='.') return s[a][b];
		b++;
	}
}

int main()
{
	int te;
	cin>>te;
	
	
    FOR(tnr,te)
    {
    	cin>>n>>m;
    	FOR(i,n+5)FOR(j,m+5) s[i][j]=0;
    	//FOR(i,n) scanf("%s",s[i]+1);
    	REP(i,1,n) cin>>s[i]+1;
    	
    	FOR(i,n+2)FOR(j,m+2)
    	{
    		if (i==0 || i==n+1) s[i][j]='#';
    		if (j==0 || j==m+1) s[i][j]='#';
    	}
    	//FOR(i,n+2) cout<<s[i]<<endl;
    	
    	bool zlo=0;
    	int wyn=0;
    	REP(i,1,n)REP(j,1,m)
    	{
    		if (s[i][j]!='.' && goup(i,j)=='#' && godown(i,j)=='#' && goleft(i,j)=='#' && goright(i,j)=='#') zlo=1;
    		if (s[i][j]=='<' && goleft(i,j)=='#') wyn++;
    		if (s[i][j]=='>' && goright(i,j)=='#') wyn++;
    		if (s[i][j]=='v' && godown(i,j)=='#') wyn++;
    		if (s[i][j]=='^' && goup(i,j)=='#') wyn++;
    	}
    	printf("Case #%d: ",tnr+1);
    	if (zlo) puts("IMPOSSIBLE");
    	else printf("%d\n",wyn);
    }

	return 0;
}


