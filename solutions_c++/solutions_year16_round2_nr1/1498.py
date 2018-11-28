#include<stdio.h>
#include<algorithm>
using namespace std;
int dg[10];
char in[2005];
int ans[2005];
int main(){
    int n,t,i,j,k;

    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    scanf("%d",&t);

    for(k=1;k<=t;k++) {
        scanf("%s",&in);
        for(i=0;i<10;i++) dg[i] = 0;

        for(n=0;in[n]!='\0';n++) {
            if(in[n] == 'Z') dg[0]++;
            else if(in[n] == 'W') dg[1]++;
            else if(in[n] == 'X') dg[2]++;
            else if(in[n] == 'S') dg[3]++;
            else if(in[n] == 'V') dg[4]++;
            else if(in[n] == 'F') dg[5]++;
            else if(in[n] == 'O') dg[6]++;
            else if(in[n] == 'G') dg[7]++;
            else if(in[n] == 'I') dg[8]++;
            else if(in[n] == 'R') dg[9]++;
        }
        int cur=0;
        for(i=0;i<dg[0];i++) {
            ans[cur++] = 0;
            dg[6]--;
            dg[9]--;
        }

        for(i=0;i<dg[1];i++) {
            ans[cur++] = 2;
            dg[6]--;
        }

        for(i=0;i<dg[2];i++) {
            ans[cur++] = 6;
            dg[3]--;
            dg[8]--;
        }

        for(i=0;i<dg[3];i++) {
            ans[cur++] = 7;
            dg[4]--;
        }

        for(i=0;i<dg[4];i++) {
            ans[cur++] = 5;
            dg[5]--;
            dg[8]--;
        }

        for(i=0;i<dg[5];i++) {
            ans[cur++] = 4;
            dg[6]--;
            dg[9]--;
        }

        for(i=0;i<dg[6];i++) {
            ans[cur++] = 1;
        }

        for(i=0;i<dg[7];i++) {
            ans[cur++] = 8;
            dg[8]--;
        }

        for(i=0;i<dg[8];i++) {
            ans[cur++] = 9;
        }

        for(i=0;i<dg[9];i++) {
            ans[cur++] = 3;
        }
        sort(ans,ans+cur);
        printf("Case #%d: ",k);
        for(i=0;i<cur;i++)
            printf("%d",ans[i]);
        printf("\n");
    }
}
