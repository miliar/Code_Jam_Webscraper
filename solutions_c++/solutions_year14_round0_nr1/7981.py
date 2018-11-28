#include <cstdio>
#include <cstring>
using namespace std;

int sel[17];
int a[5][5];
int main(){
    freopen("1.in","r",stdin);
    freopen("out.txt","w",stdout);
    int tt, i, j, cas=0;
    scanf("%d",&tt);
    while(tt--){
        printf("Case #%d: ", ++cas);
        int ca = 2, ans = 0;
        memset(sel,0,sizeof(sel));
        while(ca--){
            int now;
            scanf("%d",&now);
            for(i=1;i<=4;++i) for(j=1;j<=4;++j)
            scanf("%d",&a[i][j]);
            for(i=1;i<=4;++i) sel[a[now][i]]++;
        }
        for(i=1;i<=16;++i) if(sel[i]==2){
            if(ans==0) ans=i;else
            ans = -1;
        }
        if(ans==0) puts("Volunteer cheated!");
        else if(ans==-1) puts("Bad magician!");
        else printf("%d\n", ans);
    }
    return 0;
}
