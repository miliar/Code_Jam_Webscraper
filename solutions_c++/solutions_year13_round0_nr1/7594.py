#include <stdio.h>

/* MAP
1 : O
2 : X
3 : T
4 : .
*/

int solveCase()
{
    int map[4][4];
    int i,j;
    int notfillcount=0;
    char temp;
    int ccO=0,ccX=0;
    int answer=-1;
    for(i=0; i<4; i++) {
        ccO=0;
        ccX=0;
        for(j=0; j<4; j++) {
            scanf("%c",&temp);
            switch(temp) {
            case 'O':
                map[i][j]=1;
                ccO++;
                break;
            case 'X':
                map[i][j]=2;
                ccX++;
                break;
            case 'T':
                map[i][j]=3;
                ccO++;
                ccX++;
                break;
            case '.':
                map[i][j]=4;
                notfillcount++;
                break;
            }
        }
        scanf("\n");
        if(ccO==4) {
            answer=1;
        }
        if(ccX==4) {
            answer=2;
        }
    }
    if(answer!=-1) return answer;
    for(i=0; i<4; i++) {
        ccO=0;
        ccX=0;
        for(j=0; j<4; j++) {
            switch(map[j][i]) {
            case 1:
                ccO++;
                break;
            case 2:
                ccX++;
                break;
            case 3:
                ccO++;
                ccX++;
                break;
            }
        }
        if(ccO==4) {
            return 1;
        }
        if(ccX==4) {
            return 2;
        }
    }
    for(i=0; i<4; i++) {
        ccO=0;
        ccX=0;
        for(j=0; j<4; j++) {
            switch(map[j][i]) {
            case 1:
                ccO++;
                break;
            case 2:
                ccX++;
                break;
            case 3:
                ccO++;
                ccX++;
                break;
            }
        }
        if(ccO==4) {
            return 1;
        }
        if(ccX==4) {
            return 2;
        }
    }
    int ccO2=0,ccX2=0;
    ccO=0;
    ccX=0;
    for(i=0; i<4; i++) {
        switch(map[i][i]) {
        case 1:
            ccO++;
            break;
        case 2:
            ccX++;
            break;
        case 3:
            ccO++;
            ccX++;
            break;
        }
        switch(map[i][3-i]) {
        case 1:
            ccO2++;
            break;
        case 2:
            ccX2++;
            break;
        case 3:
            ccO2++;
            ccX2++;
            break;
        }
    }
    if(ccO==4) {
        return 1;
    }
    if(ccX==4) {
        return 2;
    }
    if(ccO2==4) {
        return 1;
    }
    if(ccX2==4) {
        return 2;
    }
    if(notfillcount==0) return 4;
    return 3;
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int i;
    int n;
    int answer;
    scanf("%d\n",&n);
    for(i=1; i<=n; i++) {
        answer=solveCase();
        switch(answer) {
        case 1:
            printf("Case #%d: O won",i);
            break;
        case 2:
            printf("Case #%d: X won",i);
            break;
        case 3:
            printf("Case #%d: Game has not completed",i);
            break;
        case 4:
            printf("Case #%d: Draw",i);
            break;
        }
        printf("\n");
        scanf("\n");
    }
    return 0;
}
