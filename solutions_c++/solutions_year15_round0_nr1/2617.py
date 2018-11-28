#include<stdio.h>
#include<iostream>
#include<vector>
#include<cstdlib>
#include<cstring>
#include<math.h>
#include<map>
#include<algorithm>
#include<queue>
#include<string>
#include<climits>
#include<bitset>
#include<set>
#include<functional>

using namespace std;
typedef long long int LL;

#ifdef _WIN32
#define gx getchar
#define px putchar
#define ps putchar(' ')
#define pn putchar('\n')
#else
#define gx getchar_unlocked
#define px putchar_unlocked
#define ps putchar_unlocked(' ')
#define pn putchar_unlocked('\n')
#endif

//input
void scan(int &n)
{
    int sign = 1;
    n = 0;
    char c = gx();
    while( c < '0' || c > '9' )
    {
        if( c == '-' ) sign = -1;
        c = gx();
    }
    while( c >= '0' && c <= '9' ) n = (n<<3) + (n<<1) + c - '0', c = gx();  n = n * sign;
}
void lscan(LL &n)
{
    int sign = 1;
    n = 0;
    char c = gx();
    while( c < '0' || c > '9' )
    {
        if( c == '-' )
        sign = -1;
        c = gx();
    }
    while( c >= '0' && c <= '9' ) n = (n<<3) + (n<<1) + c - '0', c = gx();  n = n * (LL)(sign);
}
int sscan(char a[])
{
    char c = gx();
    while(c==' ' || c=='\n') c=gx();
    int i=0;
    while(c!='\n')a[i++] = c,c=gx();
    a[i]=0;
    return i;
}
int wscan(char a[])
{
    char c = gx();
    while(c==' ' || c=='\n') c=gx();
    int i=0;
    while(c!='\n' && c!=' ')a[i++] = c,c=gx();
    a[i]=0;
    return i;
}

//output
void print(int n)
{
    if(n<0)
    {
        n=-n;
        px('-');
    }
    int i=10;
    char o[10];
    do{o[--i] = (n%10) + '0'; n/=10;}while(n);
    do{px(o[i]);}while(++i<10);
}
void lprint(LL n)
{
    if(n<0LL)
    {
        n=-n;
        px('-');
    }
    int i=21;
    char o[21];
    do{o[--i] = (n%10LL) + '0'; n/=10LL;}while(n);
    do{px(o[i]);}while(++i<21);
}
void sprint(const char a[])
{
    const char *p=a;
    while(*p)px(*p++);
}

int main()
{
    LL t,i,tot,n,ans,temp;
    string s;
    lscan(t);
    int x;
    for(x=1;x<=t;x++)
    {
        s.clear();
        lscan(n);
        n++;
        cin >> s;
        tot = 0;
        ans = 0;
        tot = s[0]-'0';
        for(i=1;i<n;i++)
        {
            temp = s[i]-'0';
            if(i > tot)
            {
                ans += i-tot;
                tot += i-tot;
            }
            tot += temp;
        }
        printf("Case #%d: ",x);
        lprint(ans);
        pn;
    }
    return 0;
}
