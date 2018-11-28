#include<bits/stdc++.h>

#define read freopen("input.txt","r",stdin)
#define write freopen("output.txt","w",stdout)

#define min3(a,b,c) min(a,min(b,c))
#define max3(a,b,c) max(a,max(b,c))
#define min4(a,b,c,d) min(min(a,b),min(c,d))
#define max4(a,b,c,d) max(max(a,b),max(c,d))

#define pb push_back
#define mk make_pair
#define all(v) v.begin(),v.end()
#define SORT(v) sort(all(v))

#define FILL(a,d) memset(a,d,sizeof(a))
#define LL long long
#define ULL unsigned long long
#define DD double
#define PI 2*acos(0.0)


#define fr(i,a,n) for(int i=a;i<n;i++)
#define fr1(i,a,n) for(int i=a;i<=n;i++)
#define frl(i,a,n) for(LL i=a;i<n;i++)

#define ln puts("")

#define eps 1e6
#define INF (1<<28)
#define mod 1000000007

/*FOR SEGMENT TREE*/
#define lft 2*idx
#define rgt lft+1

using namespace std;

using namespace std;

// INPUT

void sf(int &x){scanf("%d",&x);}
void sf(LL &x){scanf("%lld",&x);}
void sf(LL &x,LL &y){scanf("%lld%lld",&x,&y);}
void sf(float &x){scanf("%f",&x);}
void sf(double &x){scanf("%lf",&x);}
void sf(int &x,int &y){scanf("%d%d",&x,&y);}
void sf(float &x,float &y){scanf("%f%f",&x,&y);}
void sf(double &x,double &y){scanf("%lf%lf",&x,&y);}
void sf(double &x,double &y,double &z){scanf("%lf%lf%lf",&x,&y,&z);}
void sf(int &x,int &y,int &z){scanf("%d%d%d",&x,&y,&z);}
void sf(LL &x,LL &y,LL &z){scanf("%lld%lld%lld",&x,&y,&z);}
void sf(float &x,float &y,float &z){scanf("%u%u%u",&x,&y,&z);}
void sf(char &x){x=getchar();}
void sf(char *s){scanf("%s",s);}
void sf(string &s){cin>>s;}

// OUTPUT

void pf(int x) {printf("%d\n",x);}
void pf(int x,int y) {printf("%d %d\n",x,y);}
void pf(int x,int y,int z) {printf("%d %d %d\n",x,y,z);}
void pf(LL x) {printf("%lld\n",x);}
void pf(LL x,LL y) {printf("%lld %lld\n",x,y);}
void pf(LL x,LL y,LL z) {printf("%lld %lld %lld\n",x,y,z);}
void pf(float x) {printf("%u\n",x);}
void pf(double x) {printf("%.6lf\n",x);}
void pf(double x,double y) {printf("%.5lf %.5lf\n",x,y);}
void pf(char x) {printf("%c\n",x);}
void pf(char *x) {printf("%s\n",x);}
void pf(string x) {cout<<x; ln; }


template<class T> T bigmod(T b,T p,T m){if(p==0) return 1%m; T x=b; T ans=1; while(p){ if(p&1) ans=(ans*x)%m; p>>=1; x=(x*x)%m; } return ans; }
template<class T> T gcd(T x, T y){if (y==0) return x; return gcd(y,x%y);}
template <typename T> T POW(T b,T p) { if(p == 0) return 1; if (p == 1) return b; if (p%2 == 0) { T s = POW(b,p/2); return s*s; } return b*POW(b,p-1);}
template <typename T> T modinv(T num,T m) {return bigmod(num,m-2,m);}



int main()
{
    read;
    write;
    int t,K=0; sf(t);
    while(t--){
        string s;
        int l;
        cin>>l>>s;
        l++;
        int an=0;
        int bn=0;
        fr(i,0,l){
           int a=s[i]-'0';
           if(bn>=i){
               bn+=a;
           }
           else {
               int b=i-bn;
               bn+=b;
               an+=b;
               bn+=a;
           }
        }
        printf("Case #%d: ",++K);
        pf(an);
    }
    return 0;
}
