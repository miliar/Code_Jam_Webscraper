#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector < int > vi;
typedef pair< int ,int > pii;
#define SIZE(X) ((int)(X.size()))
#define X first
#define Y second
#define LENGTH(X) ((int)(X.length()))
#define pb push_back
#define MP(X,Y) make_pair(X,Y)
#define MEM(a,b) memset(a,(b),sizeof(a))
#define tr(c,it) for(typeof((c).begin()) it = (c).begin(); it != (c).end(); it++)
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define ain(a,n) int ((a)[(n)]); for(int i=0; i<(n); i++) cin>>((a)[i])
typedef long long int int64;
typedef unsigned long long uLL;
#define FOR(i,n) for(int i=0;i<n;i++)
#define FU(i,a,n) for(int i=a;i<=n;i++)
#define FD(i,a,n) for(int i=n;i>=a;i--)
#define GI(n) int (n); scanf("%d",&(n))
#define GS(n) scanf("%s"&s)
#define PII(n,m) printf("%d %d\n",n,m)
#define PL(n) printf("%I64d\n",n)
#define F(i,L,R) for (int i = L; i < R; i++)
#define GII(n,m) int (n),(m); scanf("%d %d",&(n),&(m))
#define IN GI(t);while(t--)
#define PLL(n) printf("%I64d\n",n)
#define GLL(n) scanf("%I64d",&n)
#define GL(n) scanf("%I64d",&n)
#define PN printf("\n")
# define mod 1000000007

#define pr16
 
#ifdef pr16
  #define pr(x)                 cerr << #x << ": " << x << endl;
  #define pr2(x, y)             cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
  #define pr3(x, y, z)          cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
  #define pr4(a, b, c, d)       cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << endl;
  #define pr5(a, b, c, d, e)    cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << endl;
  #define pr6(a, b, c, d, e, f) cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << " | " << #f << ": " << f << endl;
  #define prdd(a,r,c) for(int i=0;i<(r);i++) { for(int j = 0;j<(c);j++) cerr<<a[i][j]<<" "; cerr<<endl; } cerr<<endl;
  #define prc(a) tr(a, it) cerr<<*(it)<<" "; cerr<<endl
  #define pra(a,n) for(int i=0; i<(n); i++) cerr<<((a)[i])<<" "; cerr<<"\n"
  #define prdd(a,r,c) for(int i=0;i<(r);i++) { for(int j = 0;j<(c);j++) cerr<<a[i][j]<<" "; cerr<<endl; } cerr<<endl; 
  #define prddd(a,x,y,z) for(int i=0;i<x;i++) {cerr<<"layer "<<i<<":\n";prdd(a[i],y,z)}
 
#else
  #define pr(x)
  #define pr2(x, y)
  #define pr3(x, y, z)
  #define pr4(a, b, c, d)
  #define pr5(a, b, c, d, e)
  #define pr6(a, b, c, d, e, f)
  #define tr(c,it)
  #define prc(a)
  #define pra(a,n)
  #define prdd(a, r, c)
  #define prddd(a,x,y,z)
#endif

#define MAXN 107

int t;

int main(){	
    freopen ("D-small-attempt2.in", "r", stdin);
	freopen ("D-small-attempt2.out", "w", stdout);
    int i,a,b,c;
    scanf("%d",&t);
    for(i=1;i<=t;i++){
        scanf("%d %d %d",&a,&b,&c);
        printf("Case #%d: ",i);
        if((b*c)%a){
            printf("RICHARD\n");
        }else{
            if(a<=2){
                printf("GABRIEL\n");
            }else if(a==3){
                if(b*c==3) printf("RICHARD\n");
                else printf("GABRIEL\n");
            }else{
                if(b*c==4) printf("RICHARD\n");
                if(b*c==8) printf("RICHARD\n");
                if(b*c==12) printf("GABRIEL\n");
                if(b*c==16) printf("GABRIEL\n");
            }
        }
 	}   
 	return 0;
 }
