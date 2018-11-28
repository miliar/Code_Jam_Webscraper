#include<cstdio>
#include<cstring>

using namespace std;

typedef long long ll;

bool f[15];
ll res = -1;

int main() {
    //freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    int cs = 1;
    while(T--) {
        ll N;
        res = -1;
        memset(f, 0, sizeof(f));
        scanf("%I64d",&N);
        for(ll i = N, j = 1; j <= 1000; j++, i += N) {
            ll temp = i;
            while(temp) {
                f[temp%10] = true;
                temp /= 10;
            }
            bool fin = true;
            for(int j = 0; j <= 9; j++) {
                if(!f[j]) fin = false;
            }
            if(fin) {
                res = i;
                break;
            }
        }
        printf("Case #%d: ",cs++);
        if(res == -1) printf("INSOMNIA\n");
        else printf("%I64d\n",res);
    }
    return 0;
}
