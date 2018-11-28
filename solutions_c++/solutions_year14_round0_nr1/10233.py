#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std;
int T;
int N,M;
int A[10][10],B[10][10];
int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int i,j,k;
    scanf("%d",&T);
    for(int tt=1;tt<=T;tt++)
    {
        scanf("%d",&N);
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
                scanf("%d",&A[i][j]);
        scanf("%d",&M);
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
                scanf("%d",&B[i][j]);
        int sum=0,num;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                if(A[N][i]==B[M][j])
                {
                    sum++;
                    num=A[N][i];
                }
            }
        }
        printf("Case #%d: ",tt);
        if(sum==0)
        {
            printf("Volunteer cheated!\n");
        }
        else if(sum==1) printf("%d\n",num);
        else printf("Bad magician!\n");
    }
    return 0;
}
