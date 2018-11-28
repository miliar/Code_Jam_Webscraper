#include <stdio.h>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <string>
#include <cstring>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <algorithm>
#include <set>
#include <bitset>
using namespace std;

typedef long long ll;
typedef long long LL;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;

#ifdef DEBUG
    #define cek(x) cout<<x
#else
    #define cek(x) if(false){}
#endif // DEBUG

#define fi first
#define se second
#define INF 1000000000
#define INFLL 1000000000000000000LL
#define EPS 1e-9
#define PI acos(-1.0)
#define pb push_back
#define TC() while(tc--)
#define FOR(i,n) for(int i=0;i<n;i++)
#define FORN(i,n) for(int i=0;i<=n;i++)
#define REP(i,a,b) for(int i=a;i<b;i++)
#define REPN(i,a,b) for(int i=a;i<=b;i++)
#define reset(a,b) memset(a,b,sizeof(a))
#define sc(x) scanf("%d",&x)

 ll gcd ( ll a, ll b ) { ll c; while ( a != 0 ) { c = a; a = b%a; b = c; } return b; }

int main(void){
    #ifdef ccsnoopy
        freopen("D:/Code/in.txt","r",stdin);
    #endif
    //to compile: g++ -o foo filename.cpp -lm -Dccsnoopy for debug.
int tc,casecounter = 1;
sc(tc);ll a,b;

TC(){
	scanf("%lld/%lld",&a,&b);
	//int numtwo = 0;
	if(mapper.find(b)==mapper.end()){
		printf("Case #%d: impossible\n",casecounter++);
	}else{
		ll x = gcd(a,b);
		a/=x;b/=x;
		if(a == 1 && b == 2)printf("Case #%d: 1\n",casecounter++);
		else{
			int step = 0;
			while(true){
				step++;
				if((double)a/b < 0.5)b/=2;
				else break;
			}
			printf("Case #%d: %d\n",casecounter++,step);
		}
	}
}

return 0;
}
	
	
	

	
	
	
	
	
	
	
		












