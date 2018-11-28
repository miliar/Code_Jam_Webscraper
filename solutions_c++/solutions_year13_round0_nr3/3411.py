#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define pb push_back
#define clean(a,b) memset(a,b,sizeof(a))
#define oo 1<<20
#define dd double
#define ll long long
#define ull unsigned long long
#define ff float
#define EPS 10E-10
#define fr first
#define sc second
#define MAXX 100000
#define PRIME_N 1000000
#define INFI 1<<30
#define SZ(a) ((int)a.size())
#define all(a) a.begin(),a.end()
#define MODD 1000000007
#define bpcnt(a) __builtin_popcount(a)
#define REP(i,n) for (i=0;i<n;i++)
#define FOR(i,p,k) for (i=p; i<k;i++)

//int rx[] = {0,-1,0,1,1,-1,-1,0,1}; //four direction x
//int ry[] = {0,1,1,1,0,0,-1,-1,-1};   //four direction y
//int rep[] = {1,1,4,4,2,1,1,4,4,2}; //repet cycle for mod
//void ullpr(){printf("range unsigned long long : %llu\n",-1U);} //for ull
//void ulpr(){printf("range unsigned long : %lu\n",-1U);} //for ull
//void upr(){printf("range unsigned : %u\n",-1U);} //for ull

vector<ll>v;

int lbond(ll target)
{
    int low = 0,high = SZ(v)-1;
    while(low<high)
    {
        int mid = (low+high)>>1;
        if(v[mid]<target)
            low = mid+1;
        else high = mid;
    }
    return low;
}

int hbond(ll target)
{
    int low = 0,high = SZ(v)-1;
    while(low<high)
    {
        int mid = (low+high+1)>>1;
        if(v[mid]>target)
            high = mid-1;
        else low = mid;
    }
    return low;
}

int main()
{
    freopen("cs1.in","r+",stdin);
    freopen("out.out","w+",stdout);
    for(ll i = 1 ; i<=1000 ; i++)
    {
        ll val = i*i;
        string str;
        stringstream ss;
        ss<<val;
        ss>>str;
        int low = 0 , high = SZ(str)-1;
        int flag = 1;
//        cout <<str<<endl;
        while(low<=high)
        {
            if(str[low]!=str[high]) {flag = 0 ; break;}
            low++,high--;
        }
        ss.clear();
        str.clear();
        ss<<i;
        ss>>str;
        low = 0 , high = SZ(str)-1;

        while(flag && low<=high)
        {
            if(str[low]!=str[high]) {flag = 0 ; break;}
            low++,high--;
        }
        if(flag) v.pb(val);
    }
//    cout<<"OK"<<endl;
//
//    for(int i = 0 ;  i<SZ(v); i++)
//        cout<<v[i]<<endl;
    int tcase,cas=1;
    scanf(" %d",&tcase);
    while(tcase--)
    {
        ll a,b;
        scanf(" %lld %lld",&a,&b);
        int sol = hbond(b) - lbond(a)+1;
        printf("Case #%d: %d\n",cas++,sol);
    }
    return 0;
}
