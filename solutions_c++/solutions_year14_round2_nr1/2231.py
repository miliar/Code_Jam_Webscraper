#define _CRT_SECURE_NO_DEPRECATE
#define _SECURE_SCL 0
#pragma comment(linker, "/STACK:200000000")

#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <complex>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <functional>
#include <fstream>
#include <iostream>
#include <map>
#include <memory.h>
#include <numeric>
#include <iomanip>
#include <queue>
#include <set>
#include <stack>
#include <list>
#include <string>
#include <sstream>
#include <vector>
#include <utility>
#include <cmath>
#include <limits.h>
using namespace std;

#define pb push_back
#define mp make_pair
#define mset(mas,val) memset(mas,val,sizeof(mas))
#define sz(a) (int)(a).size()
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()

#define forn(i,n) for (int i=0; i<int(n); ++i)
#define fornd(i,n) for (int i=int(n)-1; i>=0; --i)
#define forab(i,a,b) for (int i=int(a); i<int(b); ++i)

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;

#define getcx getchar //getchar_unlocked
inline void s( ll &n )
{
    n=0;

    ll ch=getcx();
    while( ch < '0' || ch > '9' )
    {
        ch=getcx();

    }

    while(  ch >= '0' && ch <= '9' )
        n = (n<<3)+(n<<1) + ch-'0', ch=getcx();

}
inline void s( int &n )
{
    n=0;

    int ch=getcx();
    while( ch < '0' || ch > '9' )
    {
        ch=getcx();

    }

    while(  ch >= '0' && ch <= '9' )
        n = (n<<3)+(n<<1) + ch-'0', ch=getcx();

}
class str
{
    public: char s[100];
    public:int a[100];
}x[100];
int main()
{
     freopen("C:\\Users\\Nishant\\Desktop\\3.txt","r",stdin);
     freopen("C:\\Users\\Nishant\\Desktop\\1.txt","w",stdout);
    int t,u=1;
    s(t);
    string y;

    while(t--)
    {
        int n;
        cin>>n;
        int k;
        for(int i=0;i<n;i++)
        {
            cin>>y;
            x[i].s[0]=y[0];
            x[i].a[0]=1;
            k=0;
            for(int j=1;j<y.length();j++)
            {
                if(y[j]==x[i].s[k])
                {
                    x[i].a[k]++;
                }
                else
                {
                    ++k;
                    x[i].s[k]=y[j];
                    x[i].a[k]=1;
                }
            }
            x[i].s[++k]='\0';
        }
        int flag =0;
        for(int i=0;i<n-1;i++)
        {
            if(strcmp(x[i].s,x[i+1].s)!=0)
            {
                flag =1;
                break;
            }
        }

        if(flag == 1)
        {
            cout<<"Case #"<<u++<<": Fegla Won"<<endl;
            continue;
        }
        else
        {
            int count =0;
            for(int i=0;i<k;i++)
            {
              count  = count + abs(x[0].a[i]-x[1].a[i]);
            }
            cout<<"Case #"<<u++<<": "<<count<<endl;
        }


    }
}


