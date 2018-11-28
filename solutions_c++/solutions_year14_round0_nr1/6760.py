#include <stdio.h>

int main()
{
    int caseNum;
    scanf("%d", &caseNum);

    int caseCounter = 1;
    while(1){
        if(caseCounter>caseNum) break;
        int row1, arrangement1[4][4], row2, arrangement2[4][4];
        
        // input stage
        scanf("%d", &row1); row1--;
        for(int i=0; i<4; i++)
            for(int j=0; j<4; j++)
                scanf("%d", &arrangement1[i][j]);
        scanf("%d", &row2); row2--;
        for(int i=0; i<4; i++)
            for(int j=0; j<4; j++)
                scanf("%d", &arrangement2[i][j]);

        // processing stage
        int flag=0, ans;
        for(int i1=0; i1<4; i1++)
            for(int i2=0; i2<4; i2++)
                if(arrangement1[row1][i1]==arrangement2[row2][i2]){
                    flag++;
                    ans=arrangement1[row1][i1];
                }

        // output stage
        printf("Case #%d: ", caseCounter);
        if(flag==0) printf("Volunteer cheated!\n");
        else if(flag==1) printf("%d\n", ans);
        else printf("Bad magician!\n");

        caseCounter++;
    }

    return 0;
}
