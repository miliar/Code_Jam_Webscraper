#include <bits/stdc++.h>
using namespace std;

#define debug(args...) fprintf(stderr,args)

typedef long long lint;
typedef pair<int,int> pii;
typedef pair<lint,lint> pll;

const int INF = 0x3f3f3f3f;
const lint LINF = 0x3f3f3f3f3f3f3f3fll;

int main() {
    int t=1,T;
    for(scanf("%d",&T);t<=T;++t) {
        int n,x;
        scanf("%d%d",&n,&x);
        multiset< int,greater<int> > cj;
        for(int a=0;a<n;++a) {
            int d;
            scanf("%d",&d);
            cj.insert(d);
        }
        int ans = 0;
        while(!cj.empty()) {
            ++ans;
            int large = *cj.begin();
            cj.erase(cj.begin());
            if(cj.empty()) break;
            int left = x - large;
            multiset< int,greater<int> >::iterator it = cj.lower_bound(left);
            if(it != cj.end()) cj.erase(it);
        }
        printf("Case #%d: %d\n",t,ans);
    }    
    return 0;
}
