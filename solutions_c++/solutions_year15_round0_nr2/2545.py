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

int ans;
int mm;

void solve(vector<int> a, int cost)
{
    if(cost >= ans) return;
    int m,half,i,j,n,k,c,cut;
    vector<int> x;
    m = -1;
    n = a.size();
    for(i=0;i<n;i++)
    {
        //cout << a[i] << " ";
        if(a[i] > m)m = a[i];
    }
    //pn;
    c = cost + m;
    if(c < ans)
    {
        ans = c;
        return;
    }
    half = m/2;
    for(i=1;i<=half;i++)
    {
        x.clear();
        c = 0;
        for(j=0;j<n;j++)
        {
            if(a[j]!=m) x.push_back(a[j]);
            else
            {
                x.push_back(i);
                x.push_back(a[j]-i);
                c++;
            }
        }
        solve(x,cost+c);
    }
}

int main()
{
    int t,n,i,m,half,ct,x;
    vector<int> a;
    scan(t);
    for(int xx=1;xx<=t;xx++)
    {
        scan(n);
        a.clear();
        mm = -1;
        for(i=0;i<n;i++)
        {
            scan(x);
            if(x > mm) mm = x;
            a.push_back(x);
        }
        ans = mm;
        solve(a,0);
        printf("Case #%d: ",xx);
        cout << ans << endl;
    }
    return 0;
}

