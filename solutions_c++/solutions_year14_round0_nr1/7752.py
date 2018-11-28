#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int a[5][5], b[5][5];
main() {
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int T,t, n, m;
    cin >> T;
    for(t=1;t<=T;t++) {
        int k, cnt =0, i, j;
        cin >> n; n--;

        for(i=0;i<4;i++) for(j=0;j<4;j++) cin >> a[i][j];
        cin >> m; m--;
        for(i=0;i<4;i++) for(j=0;j<4;j++) cin >> b[i][j];
        for(i=0;i<4;i++) for(j=0;j<4;j++) if(a[n][i] == b[m][j]) {cnt++;k=a[n][i];}
        printf("Case #%d: ",t);
        if(cnt==0) printf("Volunteer cheated!\n");
        else if(cnt==1) printf("%d\n",k);
        else printf("Bad magician!\n");
    }
}
