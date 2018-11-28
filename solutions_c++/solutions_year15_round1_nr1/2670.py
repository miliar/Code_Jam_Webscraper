//includes
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <map>
#include <list>
#include <utility>
#include <algorithm>
#include <cassert>

using namespace std;

//typedefs
typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<long long> vll;
typedef pair<int, int> pii;
typedef pair<long long, long long> pll;

//defines-general
#define to(a) __typeof(a)
#define all(vec)  vec.begin(),vec.end()
#define fill(a,val)  memset(a,val,sizeof(a))

//defines-iteration
#define repi(i,a,b) for(__typeof(b) i = a;i<b;i++)
#define repii(i,a,b) for(__typeof(b) i = a;i<=b;i++)
#define repr(i,b,a) for(__typeof(b) i = b;i>a;i--)
#define repri(i,b,a) for(__typeof(b) i = b;i>=a;i--)
#define tr(vec,it)  for(__typeof(vec.begin())  it = vec.begin();it!=vec.end();++it)



//defines-pair
#define ff first
#define ss second
#define pb push_back
#define mp make_pair

// my own
#define sl(a) scanf("%lld",&a)
#define sll(a,b) scanf("%lld%lld",&a,&b)
#define slll(a,b,c) scanf("%lld%lld%lld",&a,&b,&c)
#define sllll(a,b,c,d) scanf("%lld%lld%lld%lld",&a,&b,&c,&d)
#define fastio   std::ios_base::sync_with_stdio(false)

int arr[100000];

int solve1(int N)
{
    int i;
    int sum=0;
    repi(i,0,N-1)
    {
        if(arr[i]-arr[i+1]>0)
            sum+=arr[i]-arr[i+1];
    }

    return sum;
}

int solve2(int N,int rate)
{
    int i;
    int sum=0;
    repi(i,0,N-1)
    {
        if(arr[i]>=rate)
            sum+=rate;
        else
            sum+=arr[i];
    }

    return sum;
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T,m,ans1,N;
    int ans2,rate;
    int ctr=1,i;
    cin>>T;
    while(T--)
    {
        ans1=0,ans2=0;
        memset(arr,0,sizeof(arr));
        cin>>N;
        repi(i,0,N)
        {
            cin>>arr[i];
        }

        rate=0;
        repi(i,0,N-1)
        {
            rate=max(rate,arr[i]-arr[i+1]);
        }

        ans1=solve1(N);
        ans2=solve2(N,rate);

        cout<<"Case #"<<ctr<<": "<<ans1<<" "<<ans2<<endl;
        ctr++;
    }
}
