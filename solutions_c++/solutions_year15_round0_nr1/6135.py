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


int getans(int k,string S)
{
    int sum_so_far,ans=0,diff=0;
    int i,val;
    sum_so_far=S.at(0)-'0';
    for(i=1;i<S.size();i++)
    {
        val=S.at(i)-'0';
        if(i>sum_so_far)
            {
                diff=i-sum_so_far;
                ans+=diff;
            }
        sum_so_far+=(val+diff);
        diff=0;
    }

    return ans;
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T,k,ctr=1,Smax,ans;
    string S;
    cin>>T;
    while(T--)
    {
        cin>>k>>S;
        ans=getans(k,S);
        cout<<"Case #"<<ctr<<": "<<ans<<endl;
        ctr++;
    }
}
