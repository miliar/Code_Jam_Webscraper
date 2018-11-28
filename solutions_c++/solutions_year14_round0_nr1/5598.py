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

int used[20];

int main(){
	
	int T,ans,tmp;

	scanf(" %d",&T);
	
	vector<int> res;
	
	forn(test,1,T){
		
		SET(used,0);
		res.clear();
		
		forn(step,1,2){
			scanf(" %d",&ans);		
			forn(i,1,4)
				forn(j,1,4)
				{
					scanf(" %d",&tmp);
					if(i==ans)
						used[tmp]++;
				}
		}
		
		forn(i,1,16)
			if( used[i]==2 )
				res.pb(i);
		
		if(SIZE(res)==0)	printf("Case #%d: Volunteer cheated!\n",test);
		if(SIZE(res)>1)		printf("Case #%d: Bad magician!\n",test);
		if(SIZE(res)==1)	printf("Case #%d: %d\n",test,res[0]);
		
	}
	
	return 0;
	
}
