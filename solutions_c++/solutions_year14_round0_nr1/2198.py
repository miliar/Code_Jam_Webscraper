#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#include <iostream>
using namespace std;

int main() {
    int T=0, t, i, j, r, n;
    int vis[20];
    scanf("%d", &t);
    while(t--) {
        memset(vis, 0, sizeof(vis));
        for(int x=0; x<2; x++) {
            scanf("%d", &r);
            for(i=1; i<=4; i++)
                for(j=1; j<=4; j++) {
                    scanf("%d", &n);
                    if(i==r) vis[n]++;
                }
        }
        int dup=0, ans=0;
        for(i=1; i<=16; i++)
            if(vis[i]>1) dup++, ans=i;
        
        printf("Case #%d: ", ++T);
        if(dup>1) printf("Bad magician!\n");
        else if(dup==0) printf("Volunteer cheated!\n");
        else printf("%d\n", ans);
    }
    return 0;
}
