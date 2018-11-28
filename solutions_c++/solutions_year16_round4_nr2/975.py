// Template and program by vvneagleone

#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<iomanip>
#include<algorithm>
#include<cmath>
#include<string>
#include<cstring>
#include<climits>
#include<vector>
#include<utility>
#include<queue>
#include<set>
#include<map>
using namespace std;
typedef long long LL;
typedef long double LD;
#define MOD 1000000007LL

#ifdef __GNUC__
    #if ( __GNUC__ >= 4 && __GNUC_MINOR__ >= 7 && __cplusplus > 201100L )
        #include<unordered_set>
        #include<unordered_map>
    #endif
#endif // __GNUC__

#ifdef __WIN32
    #define gx getchar
    #define px putchar
    #define ps putchar(' ')
    #define pn putchar('\n')
#else
    #define gx getchar_unlocked
    #define px putchar_unlocked
    #define ps putchar_unlocked(' ')
    #define pn putchar_unlocked('\n')
#endif // __WIN32

void scan(int &n){int sign=1;n=0;char c=gx();while(c<'0'||c>'9'){if(c=='-')sign=-1;c=gx();}while(c>='0'&&c<='9')n=(n<<3)+(n<<1)+c-'0',c=gx();n=n*sign;}
void lscan(LL &n){int sign=1;n=0;char c=gx();while(c<'0'||c>'9'){if(c=='-')sign=-1;c=gx();}while(c>='0'&&c<='9')n=(n<<3)+(n<<1)+c-'0',c=gx();n=n*(LL)(sign);}
int sscan(char a[]){char c=gx();while(c==' '||c=='\n')c=gx();int i=0;while(c!='\n')a[i++]=c,c=gx();a[i]=0;return i;}
int wscan(char a[]){char c=gx();while(c==' '||c=='\n')c=gx();int i=0;while(c!='\n'&&c!=' ')a[i++]=c,c=gx();a[i]=0;return i;}
void print(int n){if(n<0){n=-n;px('-');}int i=10;char o[10];do{o[--i]=(n%10)+'0';n/=10;}while(n);do{px(o[i]);}while(++i<10);}
void lprint(LL n){if(n<0LL){n=-n;px('-');}int i=21;char o[21];do{o[--i]=(n%10LL)+'0';n/=10LL;}while(n);do{px(o[i]);}while(++i<21);}
void sprint(const char*a){const char*p=a;while(*p)px(*p++);}
LL power(LL b,LL e,LL m=MOD){LL r=1;while(e){if(e&1)r=(r*b)%m;b=(b*b)%m;e>>=1;}return r;}
LL minvp(LL n, LL m=MOD){return power(n,m-2,m);}
LL minv(LL a,LL m=MOD){LL c,t,q,x,y;c=m;x=0;y=1;while(a>1){q=a/c;t=c;c=a%c;a=t;t=x;x=y-q*x;y=t;}if(y<0)y+=m;return y;}
LL mmul(LL a,LL b,LL m=MOD){LL x=0,y=a%m;while(b){if(b&1)x=(x+y)%m;y=(y<<1)%m;b>>=1;}return x%m;}
LL absll(LL x){if(x<0)return -x;return x;}

int t, T, n, i, j, k, l;
LD p[250];
int mask[250];
LD P[250];
LD sumprob, maxprob, inprob;
int inmask[250];

int main() {
    cin >> T;
    for( t = 1; t <= T; ++t ) {
        cin >> n >> k;
        for( i = 0; i < n; ++i ) cin >> p[i];

        for( i = 0; i < n-k; ++i ) mask[i] = 0;
        for( i = n-k; i < n; ++i ) mask[i] = 1;

        maxprob = 0;
        do {

            j = 0;
            for( i = 0; i < n; ++i ) {
                if( mask[i] == 1 ) {
                    P[j++] = p[i];
                }
            }

            for( i = 0; i < k/2; ++i ) inmask[i] = 0;
            for( i = k/2; i < k; ++i ) inmask[i] = 1;

            sumprob = 0;
            do {
                inprob = 1;
                for( i = 0; i < k; ++i ) {
                    if( inmask[i] ) {
                        inprob = inprob * P[i];
                    }
                    else {
                        inprob = inprob * ( (LD)(1.0) - P[i] );
                    }
                }
                sumprob += inprob;
            } while( next_permutation( inmask, inmask + k ) );

            if( sumprob > maxprob ) maxprob = sumprob;

        } while( next_permutation( mask, mask + n ) );

        cout.precision(12);
        cout << "Case #" << t << ": " << fixed << maxprob << endl;
    }
    return 0;
}
