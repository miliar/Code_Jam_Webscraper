#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;
#define pb push_back
#define MP make_pair
#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,l,h) for(int i=(l);i<=(h);++i)
#define DWN(i,h,l) for(int i=(h);i>=(l);--i)
typedef pair<int,int> PII;
typedef long long LL;

bool check(LL x, LL y){
    if(x>y) return 0;
    LL temp=y;
    while(temp>1) {
        if(temp&1)  return 0;
        temp>>=1;
    }
    return 1;
}


int main()
{
    freopen("in","r",stdin);
    freopen("out","w",stdout);
    int casnum;
    cin>>casnum;
    LL x,y;
    FOR(cas,1,casnum){
        scanf("%lld/%lld",&x,&y);
        printf("Case #%d: ",cas);

        LL temp = __gcd(x,y);
        x/=temp; y/=temp;

        temp = y;
        while(temp>1)   temp>>=1;



        if(!check(x,y)) {
            puts("impossible");
            continue;
        }

        int ans=0;
        while(x<y) {
            ans++;
            x<<=1;
        }

        if(ans > 40){
            puts("impossible");
            continue;
        }

        cout<<ans<<endl;
    }
    return 0;
}
