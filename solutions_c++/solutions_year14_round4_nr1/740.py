#pragma comment(linker, "/STACK:65000000")
#include<cstdio>
#include<iostream>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<cstring>
#include<string>
#include<cmath>
#include<complex>
#include<ctime>

using namespace std;

typedef long long ll;
typedef pair<ll,ll> pii;
typedef vector<int> vi;
typedef vi::iterator vit;
typedef set<ll> si;
typedef si::iterator sit;
typedef vector<pii> vpi;

#define sq(x) ((x)*(x))
#define all(x) (x).begin(),(x).end()
#define cl(x) memset(x,0,sizeof(x))
//#define LL "%I64d"
#define RLL(x) scanf(LL,&(x))

int n,t;

int mas[100100];

void test(int T)
{
    cin>>n>>t;
    for(int i=0; i<n; ++i)
        scanf("%d",&mas[i]);
    sort(mas,mas+n);
    int l = 0, r = n-1;
    int answ = 0;
    while(l < r)
    {
        if(mas[l] + mas[r] <= t)
        {
            ++answ;
            ++l;
            --r;
        }
        else
        {
            ++answ;
            --r;
        }
    }
    if(l == r)
        ++answ;
    printf("Case #%d: %d\n", T, answ);
}

int main(int argc, const char * argv[])
{
    
    freopen("/Users/olpet/Downloads/GCJ/a.in", "r", stdin);
    freopen("/Users/olpet/Downloads/GCJ/a.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int t = 0; t < T; ++t)
        test(t+1);
    return 0;
}