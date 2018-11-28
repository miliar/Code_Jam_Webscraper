#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>

#define forn(i,n) for(int i = 0; i < n; i++)
#define forn1(i,n) for(int i = 1; i <= n; i++)
#define forall(it, vec) for(typeof(vec.begin()) it = vec.begin(); it != vec.end(); it++)
#define ON(mask,i) (mask | (1L << (i)))
#define OFF(mask,i) (mask &  (-1 ^ (1L<<(i))) )
#define TOGGLE(mask,i) (mask ^ (1L << (i)))
#define isON(mask, i) (mask & (1L<<(i)))
#define mp make_pair
using namespace std;
typedef pair<int, int> pii;
char str[1000];
int main(){
	int T;
	scanf("%d", &T);
	forn1(t,T){
		printf("Case #%d: ",t);
		//long long A = 1L << 40;
		long long P,Q;
		scanf("%s", str);
		int p = 0;
		while(str[p] != '/') p++;
		str[p] = 0;
		sscanf(str,"%lld", &P);
		sscanf(str+p+1,"%lld", &Q);
		int a = P, b = Q;
		while(b % 2 == 0) b /= 2;
		while(a < b) a = a << 1; 
		if(a % b != 0){
			printf("impossible\n");
			continue;
		}
			
		p = P;
		
		int res = 0;

		while(P%2 == 0){
			res++;
			P /= 2;
		}
		while(Q%2 == 0 && Q > P){
			res++;
			Q /= 2;
		}
		
		//int aux = Q + Q;
		//while(P >= aux) {
		//	P /= 2;
		//	res--;
		//}
		//printf("P:%lld Q:%lld\n",P,Q);		
		
		
		printf("%d\n", res);
		
	}

	return 0;
}
