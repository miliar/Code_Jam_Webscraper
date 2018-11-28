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

lld n,p;

lld f(lld n,lld x,lld y){
    lld ans=0,nx,ny=y;
    if (n<1) return 1;
    if (ny>=1){
        ny--;
        ans=f(n-1,er(n-1)-(ny/2),ny/2);
    }else {
        nx=x-1;
        ans=er(n-1)+f(n-1,nx/2,y);
    }
    return ans;
}

lld judge1(lld m){
    lld ans;
    ans=f(n,m-1,er(n)-m);
    return ans<=p;
}

lld g(lld n,lld x,lld y){
    lld ans=0,nx=x,ny=y;
    if (n<1) return 1;
    if (nx>=1){
        nx--;
        ans+=er(n-1);
        ans+=g(n-1,nx/2,er(n-1)-(nx/2));
    }else {
        ny=y-1;
        ans=g(n-1,x,ny/2);
    }
    return ans;
}

lld judge2(lld m){
    lld ans;
    ans=g(n,m-1,er(n)-m);
//printf("m:%lld p:%lld ans:%lld\n",m,p,ans);
    return ans<=p;
}

int main(){
freopen("B-large.in","r",stdin);
pout;
    lld i,j,tem,T,cas=0;
    cin>>T;
    while (T--){
        cin>>n>>p;
        lld low,high,mid,ans1,ans2;
        ans1=1;
        low=1; high=er(n);
        while (low<=high){
            mid=(low+high)/2;
            if (judge1(mid)){
                ans1=mid; low=mid+1;
            }else high=mid-1;
        }

        ans2=1;
        low=1; high=er(n);
        while (low<=high){
            mid=(low+high)/2;
            if (judge2(mid)){
                ans2=mid; low=mid+1;
            }else high=mid-1;
        }
        printf("Case #%lld: %lld %lld\n",++cas,ans2-1,ans1-1);
    }
    return 0;
}
























