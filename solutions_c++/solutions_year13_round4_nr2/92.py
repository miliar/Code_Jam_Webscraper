#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
using namespace std;
typedef long long ll;
typedef double du;
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define FOR(i, s, t) for(i = (s); i < (t); i++)
#define RFOR(i, s, t) for(i = (s)-1; i >= (t); i--)

int main()
{
    #ifdef __FIO
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    #endif
    int T, i0;
    scanf("%d", &T);
    for(i0 = 1; i0 <= T; i0++){
        printf("Case #%d: ", i0);
        int n;
        ll p;
        int i, j, k;
        ll ans1, ans2;
        
        cin>>n>>p;
        
        if(p == (1LL<<n)){
            ans1 = ans2 = (1LL<<n)-1;
        }
        else{
            p--;
            i = 1;
            while((1LL<<(n-i)&p) != 0)
                i++;
            ans1 = (1LL<<i)-2;
            p++;
            p = (1LL<<n)-p;
            p--;
            i = 1;
            while((1LL<<(n-i)&p) != 0)
                i++;
            ans2 = (1LL<<i)-2;
            p++;
            ans2 ^= (1LL<<n)-1;
            ans2--;
        }
        cout<<ans1<<" "<<ans2<<endl;
    }
    return 0;
}
