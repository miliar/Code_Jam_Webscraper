#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <set>
#include <string>
#include <iostream>

using namespace std;

int tcase;
double c,f,x,v,res,t;

int main() {
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);

    scanf("%d",&tcase);

    for (int tid=1; tid<=tcase; ++tid) {
        scanf("%lf%lf%lf",&c,&f,&x);

        v=2; res=x/v; t=0;

        while (true) {
            t+=c/v; v+=f;
            if (t+x/v>res) break;
            res=t+x/v;
        }

        printf("Case #%d: %0.7f\n",tid,res);
    }

    return 0;
}
