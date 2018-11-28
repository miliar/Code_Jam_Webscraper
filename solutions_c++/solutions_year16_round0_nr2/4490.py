#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<iostream>
#include<sstream>
#include<map>
#include<set>
#include<string>
using namespace std;

#define MAX(a,b) a>b?a:b
#define MIN(a,b) a<b?a:b
#define PI acos(-1.0)
#define SQ(x) ((x)*(x))
#define CUBE(x) ((x)*(x)*(x))
#define MAX_INT 2147483647
#define inf 1<<30
#define FOR(i,a,b) for(i=(a);i<=(b);i++)
#define FORV(i,a,b) for(i=(a);i>=(b);i--)
#define REP(i,n) for(i=0;i<(n);i++)
#define pb push_back
#define pf push_front
#define ppb pop_back
#define ppf pop_front
#define nl printf("\n")
#define set(A,x) memset(A,x,sizeof(A))
#define in(x) scanf("%d",&x)
#define inll(x) scanf("%lld",&x)
#define LL long long
//#define LL __int64
#define MX 10000

template<class T>inline T _abs(T n){return n<0?-n:n;}
template<class T>inline T _gcd(T a, T b){return b==0?a:_gcd(b,a%b);}
template<class T>inline T _lcm(T a, T b){return a/_gcd(a,b)*b;}

int setb(int N,int pos){return N= N | (1<<pos);}
int resetb(int N,int pos){return N= N & ~(1<<pos);}
bool checkb(int N,int pos){return (bool)(N & (1<<pos));}

char change(char ch)
{
    if(ch=='+')
        return '-';
    if(ch=='-')
        return '+';
}

void swap(char *s, int start, int end)
{
    while(end>=start)
    {
        char end_ch = change(s[end]);
        char start_ch = change(s[start]);
        s[start] = end_ch;
        s[end] =start_ch;
        start++;
        end--;
    }
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output_b_large.txt","w",stdout);
    int test,cases=0;
    char s[110];
    in(test);
    getchar();
    while(test--)
    {
        gets(s);
        int start= 0;
        int end = strlen(s)-1;
        int _count=0;
        while(true)
        {
            while(end>=0 && s[end]=='+')
                end--;
            if(end<0)
                break;
            if(s[end]=='-' && s[start]=='-')
            {
                swap(s,start,end);
                _count++;
            }
            else if(s[end]=='-' && s[start]=='+')
            {
                int temp = start;
                while(s[temp]=='+')
                    temp++;
                swap(s, start, temp-1);
                swap(s, start, end);
                _count+=2;
            }
        }
        printf("Case #%d: %d\n",++cases, _count);
    }


    return 0;
}
