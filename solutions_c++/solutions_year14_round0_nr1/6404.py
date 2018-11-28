#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    freopen("C:\\Users\\Shaival\\Desktop\\A-small-attempt0.in","r",stdin);
    freopen("C:\\Users\\Shaival\\Desktop\\OP1.txt","w",stdout);
    int t,I;
    scanf("%d",&t);
    for(I=1;I<=t;I++)
    {
        int p,q;
        int A[4][4];
        int i,j,c1,c2,c3,c4;
        scanf("%d",&p);
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
               scanf("%d",&A[i][j]);
        c1=A[p-1][0];
        c2=A[p-1][1];
        c3=A[p-1][2];
        c4=A[p-1][3];
        int cnt=0;
        int idx=-1;
        scanf("%d",&q);
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                scanf("%d",&A[i][j]);
        for(j=0;j<4;j++)
        {
            if(A[q-1][j]==c1 || A[q-1][j]==c2 || A[q-1][j]==c3 || A[q-1][j]==c4)
            {
                cnt++;
                idx=j;
            }
        }
        if(cnt==0)
        {
            printf("Case #%d: Volunteer cheated!\n",I);
        }
        else if(cnt==1)
        {
            printf("Case #%d: %d\n",I,A[q-1][idx]);
        }
        else
        {
            printf("Case #%d: Bad magician!\n",I);
        }
    }
    return 0;
}
