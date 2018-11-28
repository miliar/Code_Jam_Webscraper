#include <cstdio>
#include <iostream>
using namespace std;
int main() {
    freopen("lot.in","r",stdin);
    freopen("lot.out","w",stdout);
    int tc, a, b, k, t = 1, cnt, temp;
    scanf("%d",&tc);
    while (tc--) {
        cnt = 0;
        scanf("%d %d %d",&a,&b,&k);
        for (int i=0; i<a; i++) {
            for (int j=0; j<b; j++) {
                temp = i & j;
                if (temp < k) {
                    //cout<<"a : "<<a<<"   b : "<<b<<endl;
                    cnt += 1;
                }
            }
        }
        printf("Case #%d: %d\n",t,cnt);
        t++;
    }
    return 0;
}
