#include<iostream>
#include<stdio.h>
using namespace std;
main()
{
    int t,i,j,p,r,k;
    char A[4][4];
    cin>>t;
    for(i=1;i<=t;i++)
    {
        p=0;
        r=0;
        for(j=0;j<4;j++){
                    cin>>A[j];
                }
        for(j=0;j<4;j++){
            if((A[j][0]=='X'||A[j][0]=='T')&&(A[j][1]=='X'||A[j][1]=='T')&&(A[j][2]=='X'||A[j][2]=='T')&&(A[j][3]=='X'||A[j][3]=='T'))
            {
                printf("Case #%d: X won\n",i);
                p=1;
                break;
            }
        else if((A[j][0]=='O'||A[j][0]=='T')&&(A[j][1]=='O'||A[j][1]=='T')&&(A[j][2]=='O'||A[j][2]=='T')&&(A[j][3]=='O'||A[j][3]=='T'))
                    {   
                                printf("Case #%d: O won\n",i);
                p=1;  
                break;
            }
        }
        if(p==0){
        for(j=0;j<4;j++){
                 if((A[0][j]=='X'||A[0][j]=='T')&&(A[1][j]=='X'||A[1][j]=='T')&&(A[2][j]=='X'||A[2][j]=='T')&&(A[3][j]=='X'||A[3][j]=='T'))
                    {   
                        printf("Case #%d: X won\n",i);
                p=1;
                break;
                    }
                 else if((A[0][j]=='O'||A[0][j]=='T')&&(A[1][j]=='O'||A[1][j]=='T')&&(A[2][j]=='O'||A[2][j]=='T')&&(A[3][j]=='O'||A[3][j]=='T'))
                    {
                        printf("Case #%d: O won\n",i);
                p=1;
                break;
                   }
            }
        }
        if((A[0][0]=='X'||A[0][0]=='T')&&(A[1][1]=='X'||A[1][1]=='T')&&(A[2][2]=='X'||A[2][2]=='T')&&(A[3][3]=='X'||A[3][3]=='T'))
            {
                      printf("Case #%d: X won\n",i);
                    p=1;
            }
        else if((A[0][3]=='X'||A[0][3]=='T')&&(A[1][2]=='X'||A[1][2]=='T')&&(A[2][1]=='X'||A[2][1]=='T')&&(A[3][0]=='X'||A[3][0]=='T'))
            {
                    printf("Case #%d: X won\n",i);
                    p=1;
            }
        if((A[0][0]=='O'||A[0][0]=='T')&&(A[1][1]=='O'||A[1][1]=='T')&&(A[2][2]=='O'||A[2][2]=='T')&&(A[3][3]=='O'||A[3][3]=='T'))
            {
                    printf("Case #%d: O won\n",i);
                    p=1;
            }
        if((A[0][3]=='O'||A[0][3]=='T')&&(A[1][2]=='O'||A[1][2]=='T')&&(A[2][1]=='O'||A[2][1]=='T')&&(A[3][0]=='O'||A[3][0]=='T'))
            {
                    printf("Case #%d: O won\n",i);
                    p=1;
        }
        if(p==0){
        for(j=0;j<4;j++){
                    if(A[j][0]=='.'||A[j][1]=='.'||A[j][2]=='.'||A[j][3]=='.'){
                r=1;
                printf("Case #%d: Game has not completed\n",i);
                break;
           }
        }
        if(r==0)
             printf("Case #%d: Draw\n",i);
        }
    }
    return 0;
}
