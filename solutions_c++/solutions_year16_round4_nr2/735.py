#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cstring>
#include <cstdio>
#include <math.h>
#include <queue>
#include <stack>
#include <map>
#include <cassert>
#include <set>
using namespace std;


const int N=888888;

double pos[N];


int main () {
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for (int cas=1;cas<=T;cas++) {
       int n,k;
       scanf("%d %d",&n,&k);
       for (int i=0;i<n;i++) {
            scanf("%lf",pos+i);
       }
       double ret=0;
       for (int mask=0;mask<(1<<n);mask++) {
            int num=__builtin_popcount(mask);
            if (num!=k) continue;
            vector<int> vec;
            for (int i=0;i<n;i++) {
                if ((mask>>i)&1) vec.push_back(i);
            }
            double ans=0;
            for (int mama=0;mama<(1<<k);mama++) {
                int cnt=__builtin_popcount(mama);
                if (cnt!=k/2) continue;
                double now=1.0;
                for (int i=0;i<k;i++) {
                    int real=vec[i];
                    if ((mama>>i)&1) {
                        now*=pos[real];
                    }
                    else {
                        now*=(1-pos[real]);
                    }
                }
                ans+=now;
            }
            ret=max(ret,ans);
       }
       printf("Case #%d: %.10f\n",cas,ret);
    }
    return 0;
}
