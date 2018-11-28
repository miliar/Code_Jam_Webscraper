
#include<bits/stdc++.h>

/*** Template Starts ***/
#define       ff                first
#define       ss                second
#define       pb                push_back
#define       in                insert
#define       mp                make_pair
#define       NL                '\n'
#define       FOR(i,a,b)        for(int i = a; i < b; i++)
#define       REV(I,a,b)        for(int i = a-1; i >= b; i--)
#define       sfi(n)            scanf("%d",&n)
#define       sf                scanf
#define       pfi(x)            printf("%d",x)
#define       pf                printf
using namespace std;

const double PI = 2 * acos(0.0);
const double EPS = 1e-11;
const int    MOD = 1000000009;
typedef unsigned long long ULL;
typedef long long LL;

template<class T> inline T sqr(T x){ return x * x; }
template<class T> inline T MAX(T a, T b){ return (a > b) ? a : b; }
template<class T> inline T MIN(T a, T b){ return (a < b) ? a : b; }
template<class T> inline T fABS(T a) { return a< 0 ? a * (-1) : a; }
template<class T> inline void SWAP(T &a, T &b) { T t = a; a = b; b = t; }
inline LL POW(LL base, LL power){
	LL I, res = base; if (power == 0) return 1;
	for (I = 0; I < power - 1; I++) res *= base;
	return res;
}
LL GCD(LL a,LL b){ if(b == 0) return a; return GCD(b,a%b);}
LL LCM(LL a,LL b){ return a*b/GCD(a,b);}

bool isUpperCase(char c){ return c >= 'A' && c <= 'Z'; }
bool isLowerCase(char c){ return c >= 'a' && c <= 'z'; }
bool isVowel(char c) { return (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U'); }
bool isLetter(char c){ return c >= 'A' && c <= 'Z' || c >= 'a' && c <= 'z'; }
bool isDigit(char c){ return c >= '0' && c <= '9'; }
char toLowerCase(char c){ return (isUpperCase(c)) ? (c + 32) : c; }
char toUpperCase(char c){ return (isLowerCase(c)) ? (c - 32) : c; }
int toInt(string s){ int r = 0; istringstream sin(s); sin >> r; return r; }
double toDouble(string s){ double r = 0; istringstream sin(s); sin >> r; return r; }
string toString(int n){ string s; stringstream convert; convert << n; s = convert.str(); return s; }

#define MAX 10005

/************** Code starts *******************/

int main()
{
    freopen ("input.txt","r",stdin);
    freopen ("output.txt","w",stdout);
   int t;
   LL n,x,ans;
   sfi(t);
   for(int ts=1;ts<=t;ts++)
   {
       set<int>S;
       bool flag = false;
        scanf("%lld",&n);
        printf("Case #%d: ",ts);
        for(int i=1;i<=100000;i++)
        {
            x=n*i;
            ans=x;
            while(x)
            {
                S.insert(x%10);
                x/=10;
            }
            if(S.size()==10)
            {
               flag=true;
                break;
            }

        }
        if(flag)printf("%lld\n",ans);
        else printf("INSOMNIA\n");


   }

    return 0;
}
