#include <bits/stdc++.h>
using namespace std;

#define eprintf(...) fprintf(stderr,__VA_ARGS__)

const int N=100010;
const int INF=1e9;
const int Mod=1e9+7;

int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int tc; scanf("%d",&tc);
    for(int t=1;t<=tc;t++) {
        printf("Case #%d: ",t);
        int x; scanf("%d",&x);
        vector<bool> f(10,false);
        auto fun = [&]() {
            bool ok=true;
            for(int i=0;i<=9;i++) ok&=f[i];
            return ok;
        };
        auto g = [&](int y) {
            while(y) f[y%10]=true,y/=10;
        };
        if(x==0) puts("INSOMNIA");
        else {
            long long p;
            for(p=x;!fun();p+=x) g(p);
            printf("%lld\n",p-x);
        }
    }
    return 0;
}
