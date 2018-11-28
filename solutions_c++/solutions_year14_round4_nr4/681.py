//TC

#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include <cstdio>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <list>
#include <set>
#include <map>

#define forn(a,b,c) for(int (a)=(b);(a)<=(c);(a)++)
#define forr(a,b,c) for(int (a)=(b);(a)>=(c);(a)--)
#define foreach(a,b) for( typeof( (b).begin() ) a=(b).begin(); (a)!=(b).end() ; (a)++ )
#define foreachr(a,b) for( typeof( (b).rbegin() ) a=(b).rbegin(); (a)!=(b).rend() ; (a)++ )
#define dg(x)  cerr <<#x<<':'<<x<<" "
#define dbg(x)  cerr <<#x<<':'<<x<<endl
#define SET(A,b) memset(A,b,sizeof (A) )
#define SIZE(A) ((int)(A).size())
#define ALL(A) (A).begin(),(A).end()
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define num(a) (1LL<<(a))
using namespace std;

typedef double dbl;
typedef long long Lint;
typedef pair<int,int> ii;
typedef pair<Lint,Lint> Lii;

const Lint mod = 1e9;

const int MAXN = 200010;

int N,S,T;

vector<string> V[20];
vector<string> R[20];

string str[20];

int Max,cnt;

void kont(){
	
	forn(i,1,S)
		if( SIZE( V[i] )==0 )
			return ;
	
	vector<string> tmp;
	
	int cur=0;
	
	forn(i,1,S)
	{
		tmp.clear();
		forn(j,0,SIZE(V[i])-1)
			tmp.pb( V[i][j] );
		cur++;
		sort( ALL( tmp ) );
		forn(i,0,SIZE(tmp)-1)
			cur+=SIZE( tmp[i] );
		forn(i,1,SIZE(tmp)-1)
			for(int j=0;j<SIZE(tmp[i]) && j<SIZE(tmp[i-1]) && tmp[i][j]==tmp[i-1][j];j++)
				cur--;
	}
	
	if(cur>Max)
		Max=cur,cnt=1;
	else if(cur==Max)
		cnt++;
	/*if(cur==8)
		forn(i,1,S){
			forn(j,0,SIZE(V[i])-1)
				cout << V[i][j] << " ";
			puts("");
		}*/
	
}

void build(int k){
	
	if(k==N+1){
		kont();
		return;
	}
	
	forn(i,1,S)
	{
		V[i].pb( str[k] );
		build(k+1);
		V[i].pop_back();
	}
	
}

int main(){
	
	scanf(" %d",&T);
	
	forn(test,1,T){
		
		Max=cnt=0;
		
		scanf("%d %d",&N,&S);
		
		forn(i,1,N)
			cin >> str[i];
		
		build( 1 );
		
		printf("Case #%d: %d %d\n",test,Max,cnt);
		
	}
	
}
