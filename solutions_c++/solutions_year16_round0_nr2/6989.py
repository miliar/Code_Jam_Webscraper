#include <bits/stdc++.h>
 
using namespace std;
 
#define MAXN         123456
#define HODOR        long long int
#define INF          1234567890
#define PI           3.141592653589793
#define rep(i, a, b) for(int i = (a); i < (b); ++i)
#define dwn(i, a, b) for(int i = (a); i >= (b); --i)
#define REP(c, it)   for( typeof( (c).begin()) it = (c).begin();  it != (c).end(); ++it)
#define DWN(c, it)   for( typeof( (c).end()) it = (c).end()-1;  it >= (c).begin(); --it)
#define ss(n)        scanf("\n%s",n)
#define FILL(x,y)    memset(x,y,sizeof(x))
#define pb           push_back
#define mp           make_pair
#define ALL(v)       v.begin(), v.end()
#define sz(a)        ((int)a.size())
#define SET(v, i)    (v | (1 << i))
#define TEST(v, i)   (v & (1 << i))
#define TOGGLE(v, i) (v ^ (1 << i))
#define gc           getchar_unlocked
#define pc           putchar_unlocked
 
template<typename X> inline void inp(X &n ) {
   register int ch=gc();int sign=1;n=0;
   while( ch < '0' || ch > '9' ){if(ch=='-')sign=-1; ch=gc();}
   while(  ch >= '0' && ch <= '9' ) n = (n<<3)+(n<<1) + ch-'0', ch=gc();
   n=n*sign;
}
 
template<typename X> inline void out(X a) {
   char snum[20]; int i=0,sign=0;
   if(a<0) sign=1,a=-a;
   do {snum[i++]=a%10+48; a=a/10; }while(a!=0);
   if(sign) pc('-');
   for(i--;i>=0;pc(snum[i--]));
   pc('\n');
}

#define testcases(tc)  int tc,t; for(inp(t),tc=1;tc<=t;++tc)

char ip[100+10];
int len, ans;
bool flip;

int main() {
   testcases(tc) {
   	ss(ip), len = strlen(ip), ans = 0, flip = 0;
   	for ( int i = len-1; i >= 0; ) {
   		if ( !flip && ip[i] == '-' ) {
   			++ans, flip ^= 1;
   			while ( i >= 0 && ip[i] == '-' ) 
   				--i;
   		} else if ( flip && ip[i] == '+' ) {
   			++ans, flip ^= 1;
   			while ( i >= 0 && ip[i] == '+' ) 
   				--i;
   		} else {
   			--i;
   		}
   	}
   	printf("Case #%d: %d\n", tc, ans);
   }
   return 0;
}