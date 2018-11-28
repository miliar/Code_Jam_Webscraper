#include <cstdio>

using namespace std;

int data[5][5];
int chk[17];

int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t,i,j,k,r,cnt,ans;
    scanf("%d",&t);
    for(k=1;k<=t;k++) {
        for(i=1;i<=16;i++) chk[i] = 0;
        cnt = 0;
        scanf("%d",&r);
        for(i=1;i<=4;i++) {
            for(j=1;j<=4;j++) scanf("%d",&data[i][j]);
        }
        for(j=1;j<=4;j++) chk[data[r][j]]++;

        scanf("%d",&r);
        for(i=1;i<=4;i++) {
            for(j=1;j<=4;j++) scanf("%d",&data[i][j]);
        }
        for(j=1;j<=4;j++) chk[data[r][j]]++;

        for(i=1;i<=16;i++) {
            if(chk[i]==2) {
                cnt++;
                ans = i;
            }
        }
        printf("Case #%d: ",k);
        if(cnt==0) printf("Volunteer cheated!\n");
        else if(cnt==1) printf("%d\n",ans);
        else printf("Bad magician!\n");
    }
    return 0;
}
