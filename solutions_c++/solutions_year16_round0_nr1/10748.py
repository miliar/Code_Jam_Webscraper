#include <bits/stdc++.h>

using namespace std;

int ci[10];

int main() {
    freopen("A-large.in","r",stdin);
    freopen("tt2.in","w",stdout);

    int T, kase=1; cin>>T;
    while(T--) {
        printf("Case #%d: ", kase++);
        int N;
        cin>>N;
        if(N==0) {
            puts("INSOMNIA");
            continue;
        }
        memset(ci,0,sizeof ci);
        for(int j=N;;j+=N) {
        //    printf("%d\n", j);
            int t=j;
            while(t) ci[t%10]++, t/=10;
            int f=0;
            for(int k=0;k<10;k++) if(!ci[k]) f=1;
            if(!f) {
                printf("%d\n", j);
//                printf("%d %d\n", i, j/i );
                break;
            }
        }
    }
    return 0;
}

