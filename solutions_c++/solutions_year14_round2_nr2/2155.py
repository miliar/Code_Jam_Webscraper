#include <cstdio>
#include <cstring>
#include <algorithm>
#define forn(i,n) for(int i = 0; i < n; i++)
#define forn1(i,n) for(int i = 1; i <= n; i++)
#define forall(it, vec) for(typeof(vec.begin()) it = vec.begin(); it != vec.end(); it++)
#define ON(mask,i) (mask | (1L << (i)))
#define OFF(mask,i) (mask &  (-1 ^ (1L<<(i))) )
#define TOGGLE(mask,i) (mask ^ (1L << (i)))
#define isON(mask, i) (mask & (1L<<(i)))
#define mp make_pair
#define INF 100000000
using namespace std;
typedef pair<int, int> pii;

int main(){
	int T,A,B,K;
	scanf("%d",&T);
	forn1(t,T){
		scanf("%d%d%d",&A,&B,&K);
		long long res  = 0;
		forn(a,A)
			forn(b,B)
				if( (a&b) < K) res++;
				
		printf("Case #%d: %lld\n",t,res);
	}
	
}
