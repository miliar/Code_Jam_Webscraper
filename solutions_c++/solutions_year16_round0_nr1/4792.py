#define _CRT_SECURE_NO_WARNINGS

#define max(a,b) ((a) > (b) ? (a) : (b))
#include<stdio.h>
#include<queue>

using namespace std;
typedef long long ll;

typedef priority_queue<int> PQ;
struct Data{ PQ q; int t; };
Data data[100][100];

int main(void){

    int T;
    scanf("%d",&T);

    for(int r = 0;r < T;++r){
        ll ans = 0;
        ll d;
        scanf("%lld", &d);
        if (d == 0){
            printf("Case #%d: INSOMNIA\n",r+1,ans);
        } else {
            ll cv = d;
            int bit = 0;
            while(bit != 0x3FF) {
                ll t = cv;
                while (t) {
                    bit |= 1 << (t % 10);
                    t /= 10;
                }
                ans = cv;
                cv += d;
            }
            printf("Case #%d: %lld\n",r+1,ans);
        }
    }

}
