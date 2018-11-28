
//Author : Ujjawal Dixit  , ABV-IIITM
//Task : gca Question 1

#include <bits/stdc++.h>
#define MOD 1000000007
#define MAX 1e9
#define MIN -1e9
using namespace std;
typedef double ld;
typedef long long ll;
typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> ii; 
#define FOR(i,n,m) for(int i=0;i<n;i+=m)
#define For(i,n,m) for(int i=1;i<=n;i+=m)
#define max(a,b)    (a>=b?a:b)
#define min(a,b)    (a<b?a:b)
#define countbits(num)   __builtin_popcount(num)
#define countbitsll(num)   __builtin_popcountll(num)
#define s(a) scanf("%d",&a)
#define sll(a) scanf("%lld",&a)
#define p(a) printf("%d",a)
#define pll(a) printf("%lld",a)
#define pln()  printf("\n")
#define getstr(in) getline(cin,in)
#define getc() getchar()
#define uj() int t; scanf("%d",&t); while(t--)
template<typename T> T gcd(T a, T b) {
    if(!b) return a;
    return gcd(b, a % b);
}
template<typename T> T lcm(T a, T b) {
    return a * b / gcd(a, b);
}
char a[10000];
int main() {
	int T, t = 0;
	scanf("%d", &T);
	
	while(T--){
		int S;
		scanf("%d", &S);
		
		
		scanf("%s", a);
		
		int invi = 0, claping = (a[0]-'0');
		
		for(int i=1; i<=S; i++){
			if(claping < i){
				invi += (i - claping);
				claping = i;
			}
			
			claping += (a[i]-'0');
		}
		
		printf("Case #%d: %d\n", ++t, invi);
	}
	return 0;
}