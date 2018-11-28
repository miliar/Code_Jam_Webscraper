//Tirth Maniar
#include<bits/stdc++.h>
using namespace std;

#define TRACE
#ifdef TRACE
#define trace(...) __f(#__VA_ARGS__, __VA_ARGS__)
template <typename Arg1>
void __f(const char* name, Arg1 && arg1){
	cerr << name << " : " << arg1 << endl;
}
template <typename Arg1, typename... Args>
void __f(const char* names, Arg1 && arg1, Args &&... args){
	const char* comma = strchr(names+1,','); cerr.write(names,comma-names) << " : " << arg1 << " | "; __f(comma+1, args...);
}
#else
#define trace(...)
#endif

#define all(c) c.begin(),c.end()
#define tr(container,it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define present(container, element) (container.find(element) != container.end()) 
				// For Set and Map
#define cpresent(container, element) (find(all(container),element) != container.end())
				// For Vector
				// Use v.clear() to remove all elements
#define pb push_back
#define mp make_pair
#define sz(a) int((a).size())
				// Better to use v.empty() instead of comparing with 0 to check if empty
#define F first
#define S second		
			// For pair
#define mod 1000000007
#define scand(x) scanf("%d",&x)
#define printd(x) printf("%d\n",x)
#define scanll(x) scanf("%lld",&x)
#define printll(x) printf("%lld\n",x)

typedef long long ll;
typedef vector<int> vi;		
typedef vector< vi > vvi;    	// 2-d array
typedef pair<int,int> pii;
typedef vector<pii> vpii;

inline int mult(int x,int y){return ((ll)x*y)%mod;}
int power(int x,int y){int ret=1; while(y){ if(y&1) ret = mult(ret,x); x = mult(x,x); y = y/2;} return ret;}
int gcd(int a,int b){ if(b) return gcd(b,a%b); return a;}
vi prime;
void generateprime(int n){ int i,j; vi num(n+5); num[1]=1; for(i=4;i<n;i=i+2) num[i]=1;
	for(i=3;i<n;i++){ if(num[i]==0) { for(j=3*i;j<n;j=j+2*i) num[j] = 1;}} num[0] = 0;
	for(i=2; i<n; i++){ if(num[i]==0) prime.pb(i); num.clear();} 
}

int main()
{
	int t,n,j;
	scand(t);
	while(t--)
	{
		scand(n);
		scand(j);
		printf("Case #1:\n");
		printf("1000000000000001 3 2 5 2 7 2 3 2 7\n"); 
		printf("1000000000000101 13 11 3 4751 173 3 53 109 3\n");
		printf("1000000000000111 3 2 5 2 7 2 3 2 11\n"); 
		printf("1000000000001001 73 5 3 19 19 3 5 19 3\n"); 
		printf("1000000000001101 3 2 5 2 7 2 3 2 11\n"); 
		printf("1000000000010011 3 2 5 2 7 2 3 2 7\n"); 
		printf("1000000000011001 3 2 5 2 7 2 3 2 11\n"); 
		printf("1000000000011011 5 1567 15559 6197 5 5 1031 7 83\n");
		printf("1000000000011111 3 2 3 2 7 2 3 2 3\n"); 
		printf("1000000000100101 3 2 5 2 7 2 3 2 7\n"); 
		printf("1000000000101011 3 7 13 3 5 43 3 73 7\n"); 
		printf("1000000000101111 5 2 3 2 37 2 5 2 3\n");
		printf("1000000000110001 3 2 5 2 7 2 3 2 11\n"); 
		printf("1000000000110101 23 17 11 23 5 299699 43 239 59\n"); 
		printf("1000000000110111 3 2 3 2 7 2 3 2 3\n"); 
		printf("1000000000111011 17 2 3 2 73 2 17 2 3\n"); 
		printf("1000000000111101 3 2 3 2 7 2 3 2 3\n"); 
		printf("1000000001000011 3 2 5 2 7 2 3 2 11\n"); 
		printf("1000000001001001 3 2 5 2 7 2 3 2 7\n"); 
		printf("1000000001001111 3 2 3 2 7 2 3 2 3\n"); 
		printf("1000000001010101 3 7 13 3 5 17 3 53 7\n"); 
		printf("1000000001010111 5 2 3 2 37 2 5 2 3\n"); 
		printf("1000000001011001 11 5 281 101 5 67 5 13 19\n"); 
		printf("1000000001011011 3 2 3 2 7 2 3 2 3\n"); 
		printf("1000000001011101 17 2 3 2 1297 2 11 2 3\n"); 
		printf("1000000001011111 59 113 7 157 19 1399 7 43 107\n"); 
		printf("1000000001100001 3 2 5 2 7 2 3 2 11\n"); 
		printf("1000000001100011 23 19 11 105491 5 47 11117 1787 127\n"); 
		printf("1000000001100111 3 2 3 2 7 2 3 2 3\n"); 
		printf("1000000001101011 5 2 3 2 37 2 5 2 3\n"); 
		printf("1000000001101101 3 2 3 2 7 2 3 2 3\n"); 
		printf("1000000001110011 3 2 3 2 7 2 3 2 3\n"); 
		printf("1000000001110101 5 2 3 2 37 2 5 2 3\n"); 
		printf("1000000001111001 3 2 3 2 7 2 3 2 3\n"); 
		printf("1000000001111011 31 557 7 19 23 1129 7 5441 241\n"); 
		printf("1000000001111101 7 19 43 17 55987 23 7 7 31\n"); 
		printf("1000000001111111 3 2 5 2 7 2 3 2 7\n"); 
		printf("1000000010000011 167 2 11 2 58427 2 23 2 839\n"); 
		printf("1000000010000101 3 2 5 2 7 2 3 2 11\n"); 
		printf("1000000010001001 5 2 7 2 1933 2 29 2 157\n"); 
		printf("1000000010010001 3 2 5 2 7 2 3 2 7\n"); 
		printf("1000000010010111 3 2 3 2 7 2 3 2 3\n"); 
		printf("1000000010011001 7 1667 179 13 5 11 23 7 311\n"); 
		printf("1000000010011011 11 2 3 2 13 2 47 2 3\n"); 
		printf("1000000010011101 3 2 3 2 7 2 3 2 3\n"); 
		printf("1000000010100011 3 1259 421 3 5 8893 3 67 17\n"); 
		printf("1000000010100111 5 2 3 2 37 2 5 2 3\n"); 
		printf("1000000010101001 3 5 13 3 5 43 3 73 7\n"); 
		printf("1000000010110011 47 2 3 2 11 2 204311 2 3\n"); 
		printf("1000000010110101 3 2 3 2 7 2 3 2 3\n"); 
	}	
return 0;
}
