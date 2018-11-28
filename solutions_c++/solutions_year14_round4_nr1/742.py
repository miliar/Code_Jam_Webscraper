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

int ar[MAXN];

int main(){
	
	int T;
	
	scanf(" %d",&T);
	
	int N,X;
	
	forn(test,1,T){
		
		scanf("%d %d",&N,&X);
		
		forn(i,1,N)
			scanf(" %d",ar+i);
		
		sort( ar+1,ar+N+1 );
		
		int res=0;
		
		for(int i=1,j=N; i<=j ;){
			
			if( i!=j ){
				if( ar[i]+ar[j]<=X )
					res++,i++,j--;
				else
					res++,j--;
			}
			else{
				res++,i++,j--;
			}
			
		}
		
		printf("Case #%d: %d\n",test,res);
		
	}
	
	return 0;
}
