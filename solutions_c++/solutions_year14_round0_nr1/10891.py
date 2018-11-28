#include <stdio.h>

const char bm[] = "Bad magician!";
const char vc[] = "Volunteer cheated!";

void work(int casenum){
    int i,j,k;
    int first, second;
    int rbef[4], table[4][4];
    int buf;
    scanf("%d",&first); first--;
    for(i=0;i<4;i++){
        if(i==first) {
            for(j=0;j<4;j++) scanf("%d",&rbef[j]);
        } else for(j=0;j<4;j++) scanf("%d",&buf);
    }
    scanf("%d",&second); second--;
    int matchcount = 0;
    int matchnum;
    for(i=0;i<4;i++){
        for(j=0;j<4;j++){
            scanf("%d",&table[i][j]);
            if(i == second) {
                for(k=0;k<4;k++){
                    if(table[i][j]==rbef[k]){
                        matchcount++;
                        matchnum=rbef[k];
                    }
                }
            }
        }
    }
    if(matchcount >= 2){
        printf("Case #%d: %s\n",casenum,bm);
    } else if(matchcount == 0){
        printf("Case #%d: %s\n",casenum,vc);
    } else {
        printf("Case #%d: %d\n",casenum,matchnum);
    }
}

int main()
{
    int t;
    int c=1;
    scanf("%d",&t);
    while(t--) {
        work(c);
        c++;
    }
    return 0;   
}
