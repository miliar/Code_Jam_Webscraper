#include<cstdio>
#include<iostream>
#include<iomanip>
#include<algorithm>
#include<cmath>
#include<string>
#include<cstring>
#include<vector>
#include<utility>
#include<queue>
#include<set>
#include<map>
#include<climits>
using namespace std;
typedef long long LL;
#define MOD 1000000007LL

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
LL minv(LL a,LL m=MOD){LL c,t,q,x,y;c=m;x=0;y=1;while(a>1){q=a/c;t=c;c=a%c;a=t;t=x;x=y-q*x;y=t;}if(y<0)y+=m;return y;}
LL absll(LL x){if(x<0)return -x;return x;}

#include<unordered_map>
#include<unordered_set>

int table[5][5] =
{
    {0, 0, 0, 0, 0},
    {0, 1, 2, 3, 4},
    {0, 2,-1, 4,-3},
    {0, 3,-4,-1, 2},
    {0, 4, 3,-2,-1},
};

string a;
string k;
int p[10002];
int neg[10002];

int yolo( char a ) {
    switch(a) {
        case 'i' : return 2;
        case 'j' : return 3;
        case 'k' : return 4;
    }
}

int main() {
    int t, i, j, k, tt, L, X, prev, negger;
    scan(t);
    for( tt = 1; tt <= t; ++tt ) {
        scan(L); scan(X);
        cin >> a;
        for( i = L; i < L*X; ++i ) {
            a += (char)(a[i%L]);
        }

        prev = 1;
        negger = 0;
        L = L*X;

        if( L < 3 ) {
            sprint("Case #");
            lprint(tt);
            sprint(": NO\n");
            continue;
        }

        for( i = 0; i < L; ++i ) {
            p[i] = table[prev][yolo(a[i])];
            if( p[i] < 0 ) {
                p[i] = -1 * p[i];
                ++negger;
            }
            neg[i] = negger;
            prev = p[i];
        }

        bool flag = 0;
        int s1, s2;
        for( i = 0; i < L-2; ++i ) {
            if( p[i] != 2 || (neg[i]&1) ) continue;
            for( j = i+1; j < L-1; ++j ) {
                s1 = neg[j] - neg[i];
                if( s1 & 1 ) s1 = -1; else s1 = 1;
                s2 = neg[L-1] - neg[j];
                if( s2 & 1 ) s2 = -1; else s2 = 1;
                if( table[p[i]][3] != s1*p[j] ) continue;
                if( table[p[j]][4] != s2*p[L-1] ) continue;
                flag = 1; break;
            }
            if( flag ) break;
        }
        if( flag == 0 ) {
            sprint("Case #");
            lprint(tt);
            sprint(": NO\n");
        }
        else {
            sprint("Case #");
            lprint(tt);
            sprint(": YES\n");
        }
    }
	return 0;
}
