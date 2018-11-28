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

const Lint mod = 1e9+7;


const int MAXN = 200010;

bool cnt[20];

int check(){
	bool rev = true;
	forn(i,0,9)
		rev&=cnt[i];
	return rev;
}

int main(){

	int T,N,tmp;

	scanf(" %d",&T);

	forn(i,1,T){

		scanf(" %d",&N);
		printf("Case #%d: ",i);
		forn(j,0,9)
			cnt[j]=0;
		
		if(N==0)
			printf("INSOMNIA\n");
		else
			forn(k,1,100){

				tmp = k*N;
				while(tmp)
				{
					cnt[tmp%10]=true;
					tmp/=10;
				}

				if( check() ){
					printf("%d\n",k*N);
					break;
				}
			}
	}

	return 0;
}