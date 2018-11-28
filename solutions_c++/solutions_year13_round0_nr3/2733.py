// Danger! Too many bugs! HadronWave (c)
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <queue>
#include <deque>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <cmath>
#include <iomanip>
#include <functional>


using namespace std;

typedef unsigned int uint;
typedef long long ll;
typedef unsigned long long ull;

const long long mod = 1000000007;

ll nums[39] ={ 1,4,9,121,484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001ll, 10221412201ll, 12102420121ll, 12345654321ll, 
40000800004ll, 1000002000001ll, 1002003002001ll, 1004006004001ll, 1020304030201ll, 1022325232201ll, 1024348434201ll, 1210024200121ll, 1212225222121ll, 1214428244121ll, 1232346432321ll, 1234567654321ll, 4000008000004ll, 4004009004004ll} ;

int size = 39;

int main() {
    
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int T,L,R;
    ll a,b;
    scanf("%d",&T);
    
    for(int c = 1;c<=T;++c){
        scanf("%lld %lld",&a,&b);
        L = 0,R = 0;
        int l=0,r = size+1;
        while(l<r){
            int m = (l+r)/2;
            if(nums[m]<a) l = m+1;
            else {
                L = m;
                r = m;
            }
        }
        if(nums[l]>=a) L = l;
        l=0,r = size+1;
        while(l<r){
            int m = (l+r)/2;
            if(nums[m]<=b){
                R = m;
                l = m+1;
            }
            else r = m;
        }
        if(nums[l]<=b) R = l;
        int ans = R-L+1;
        printf("Case #%d: %d\n",c,ans);
    }       

    return 0;
}