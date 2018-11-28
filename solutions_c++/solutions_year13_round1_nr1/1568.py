//made by kuailezhish
//gl && hf
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <utility>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <bitset>
#include <cstdlib>
#include <string>
#include <stack>
#include <sstream>
#include <cstring>
#include <ctime>
#define mem(a,b) memset(a,b,sizeof(a));
#define INF 0x3f3f3f3f
#define lldINF 0x3f3f3f3f3f3f3f3fll
#define eps 1e-8
#define lld long long
#define sqr(x) ((x)*(x))
#define ab(x) (((x)>0) ? (x) : -(x))
#define PI 3.14159265358979323846
#define psl pair<sting,lld>
#define pll pair<lld,lld>
#define pii pair<int,int>
#define MP make_pair
#define er(i) (1ll<<(i))
#define pb push_back
#define lb lower_bound
#define ub upper_bound
#define rin freopen("in.txt","r",stdin)
#define pout freopen("out.txt","w",stdout)
#pragma comment(linker, "/STACK:102400000,102400000")
using std::bitset;
using namespace std;

lld low,high,mid,ans;
lld r,n;

int judge(lld x){
    double ans;
    ans=1.0*(2*r+2*x-1)*x;
    if (ans-eps<=n) return 1;
    return 0;
}

int main(){
    lld i,j,tem,T,cas=0;
freopen("A.in","r",stdin);
pout;
    cin>>T;
    for (cas=1; cas<=T; cas++){
        cin>>r>>n;
        low=1; high=n; ans=1;
        while (low<=high){
            mid=(low+high)/2;
            if (judge(mid)){
                ans=mid; low=mid+1;
            }else high=mid-1;
        }
        printf("Case #%lld: %lld\n",cas,ans);
    }
    return 0;
}


























