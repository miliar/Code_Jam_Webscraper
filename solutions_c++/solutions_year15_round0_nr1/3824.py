#pragma comment(linker,"/STACK:10000000")

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

const int MAXN = 10010;

int main(){

	char ch;
	int Test;
	int N;

	scanf(" %d",&Test);

	forn(test,1,Test){
		scanf(" %d",&N);
		int cur=0;
		int need=0;
		forn(i,0,N)
		{
			scanf(" %c",&ch);
			if( i>cur ){
				need+=i-cur;
				cur=i;
			}
			cur+=ch-'0';
		}
		printf("Case #%d: %d\n",test,need);
	}

	return 0;

}

