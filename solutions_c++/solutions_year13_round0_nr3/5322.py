#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>

#include<cmath>
#include<iostream>
#include<iomanip>
#include<fstream>

#include<string>
#include<utility>
#include<vector>
#include<list>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
#define ii long long int
#define uii unsigned long long int
#define pi 2*acos(0.0)
#define eps 1e-7
#define mem(x,y) memset(x,y,sizeof(x))
#define all(x) x.begin(), x.end()
#define pb push_back
#define sz(a) (int)a.size()
#define inf 2147483640

#define mx 100010

using namespace std;

const int debug= 0;

bool ispal(int n)
{
    int k= 0,n2= n;
    while (n)
    {
        k= k*10+n%10;
        n/= 10;
    }
    if (n2==k) return 1;
    return 0;
}

bool palsqr(int n)
{
    int sqr= sqrt(n);
    if (sqr*sqr!=n) return 0;
    if (ispal(n)&&ispal(sqr)) return 1;
    return 0;
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int n,cum[1010];
    cum[0]= 0;

    for (n=1;n<=1000;++n)
    {
        cum[n]= cum[n-1]+palsqr(n);
    }

    int t,x;
    scanf("%d",&t);
    for (x=1;x<=t;++x)
    {
        int a,b;
        scanf("%d%d",&a,&b);

        printf("Case #%d: %d\n",x,cum[b]-cum[a-1]);
    }

    return 0;
}
