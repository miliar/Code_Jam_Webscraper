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
int r, p, s;

string R[15], P[15], S[15];
int rcount[15][3], pcount[15][3], scount[15][3];

string ret_first( string a, string b ) {
    string res;
    if( a < b ) {
        res = a;
        res += b;
    }
    else {
        res = b;
        res += a;
    }
    return res;
}

void pre() {
    // precompute 3 string arrays to depth 12
    R[0] = "R";
    P[0] = "P";
    S[0] = "S";
    for( int i = 1; i <= 13; ++i ) {
        R[i] = ret_first( R[i-1], S[i-1] );
        P[i] = ret_first( P[i-1], R[i-1] );
        S[i] = ret_first( S[i-1], P[i-1] );
    }
    for( int i = 0; i <= 13; ++i ) {
        rcount[i][0] = rcount[i][1] = rcount[i][2] = 0;
        pcount[i][0] = pcount[i][1] = pcount[i][2] = 0;
        scount[i][0] = scount[i][1] = scount[i][2] = 0;

        for( int j = 0; j < R[i].size(); ++j ) {
            if( R[i][j] == 'R' ) {
                ++rcount[i][0];
            }
            if( R[i][j] == 'P' ) {
                ++rcount[i][1];
            }
            if( R[i][j] == 'S' ) {
                ++rcount[i][2];
            }
        }

        for( int j = 0; j < P[i].size(); ++j ) {
            if( P[i][j] == 'R' ) {
                ++pcount[i][0];
            }
            if( P[i][j] == 'P' ) {
                ++pcount[i][1];
            }
            if( P[i][j] == 'S' ) {
                ++pcount[i][2];
            }
        }

        for( int j = 0; j < S[i].size(); ++j ) {
            if( S[i][j] == 'R' ) {
                ++scount[i][0];
            }
            if( S[i][j] == 'P' ) {
                ++scount[i][1];
            }
            if( S[i][j] == 'S' ) {
                ++scount[i][2];
            }
        }
    }
}

int main() {
    cin >> T;
    for( t = 1; t <= T; ++t ) {
        cin >> n;
        cin >> r >> p >> s;
        pre();
        if( r == rcount[n][0] && p == rcount[n][1] && s == rcount[n][2] ) {
            cout << "Case #" << t << ": " << R[n] << endl;
        }
        else if( r == pcount[n][0] && p == pcount[n][1] && s == pcount[n][2] ) {
            cout << "Case #" << t << ": " << P[n] << endl;
        }
        else if( r == scount[n][0] && p == scount[n][1] && s == scount[n][2] ) {
            cout << "Case #" << t << ": " << S[n] << endl;
        }
        else {
            cout << "Case #" << t << ": IMPOSSIBLE" << endl;
        }
    }
    return 0;
}
