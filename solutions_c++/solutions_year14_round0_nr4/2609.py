#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <stack>
#include <ctime>
#include <deque>
#include <queue>
#include <cmath>
#include <climits>
#include <algorithm>
#include <utility>

typedef long long i64;
typedef unsigned int u32;
typedef double lf;
typedef float ft;

#define ss second
#define ff first
#define xoa erase
#define chen insert
#define ii pair <int, int>
#define ll pair <long long , long long>
#define mp make_pair
#define fIn(file) freopen(file".inp","r",stdin);
#define fOut(file) freopen(file".out","w",stdout);
#define max(a,b) (a>b?a:b)
#define min(a,b) (a<b?a:b)
#define pow2(x) (x*x)

#define MAXL LLONG_MAX
#define MINL LLONG_MIN
#define inf 1000111222

int times;
static const unsigned Mod37BitPosition[] = // map a bit value mod 37 to its position
{
    -1, 0, 1, 26, 2, 23, 27, 0, 3, 16, 24, 30, 28, 11, 0, 13, 4,
    7, 17, 0, 25, 22, 31, 15, 29, 10, 12, 6, 0, 21, 14, 9, 5,
    20, 8, 19, 18
};

i64 ctz(i64 n) {
    return Mod37BitPosition[(-n & n) % 37];
}

i64 gcd( i64 x, i64 y )
{
    if(x==y) return x;
    if(x==0) return y;
    if(y==0) return x;
    i64 cf2=ctz(x|y);
    x>>=ctz(x);
    for(;;)
    {
        y>>=ctz(y);
        if(x==y)
            break;
        if(x>y)
            std::swap(x,y);
        if(x==1)
            break;
        y-=x;
    }
    return x<<cf2;
}

using namespace std;

long long revN(long long a)
{
    long long b=0;
    while(a)
    {
        b=b*10+a%10;
        a/=10;
    }
    return b;
}

bool checkPalin(long long a)
{
    long long n=a;
    long long m=revN(a);
    while(n)
    {
        if(n%10!=m%10)
            return false;
        n/=10;m/=10;
    }
    return true;
}

bool checkSqr(long long a)
{
    long long t = sqrt(a);
    return (t*t==a);
}

#define mxN

int dx[]={0,0,1,-1};
int dy[]={1,-1,0,0};
vector<float> nao,ken;

int main ()
{
    #ifndef ONLINE_JUDGE
    fIn("D"); fOut("D2");
    times=clock();
    #endif // ONLINE_JUDGE
    int t;cin>>t;
    for (int o=1; o<=t; o++)
    {
        nao.clear();ken.clear();
        int n;cin>>n;
        for (int i=1; i<=n;i++)
        {
            float x; cin>>x; nao.push_back(x);
        }
        for (int i=1; i<=n;i++)
        {
            float x; cin>>x; ken.push_back(x);
        }
        sort(nao.begin(),nao.end());sort(ken.begin(),ken.end());
        int kq1,kq2;kq1=kq2=0;
        int before=0;
        for (int i=0;i<nao.size();i++)
        {
            int lf, rg; lf=before, rg=ken.size()-1;int res=-1;
            while(lf<=rg)
            {
                int mid=(lf+rg)/2;
                if(ken[mid]>nao[i])
                {
                    res=mid;
                    rg=mid-1;
                }
                else lf=mid+1;
            }
            before=res+1;

            if(res==-1) break;
            kq2++;
        }
        kq2=n-kq2;
        before=0;
        for(int i=0; i<ken.size();i++)
        {
            int lf,rg;lf=before;rg=nao.size()-1;int res=-1;
            while(lf<=rg)
            {
                int mid=(lf+rg)/2;
                if(nao[mid]>ken[i])
                {
                    res=mid; rg=mid-1;
                }
                else lf=mid+1;
            }
            before=res+1;
            if(res==-1) break;
            //cout<<ken[i]<<" "<<nao[res]<<endl;
            kq1++;
        }
        printf("Case #%d: %d %d\n",o,kq1,kq2);
    }
    return 0;
}
