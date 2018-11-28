#include<cstdio>
#include<algorithm>
using namespace std;
#define MAX 111

int mat[MAX][MAX];
int row_max[MAX],col_max[MAX];
int main()
{
    freopen("lmB.txt","r",stdin);
    freopen("lmB_out.txt","w",stdout);
    int T,N,M;
    scanf("%d",&T);
    for(int test=1;test<=T;test++)
    {
        int flag=1;
        for(int i=0;i<MAX;i++){
        row_max[i]=0;
        col_max[i]=0;
        }
        scanf("%d %d",&N,&M);
        //printf("Check: %d %d\n",N,M);

        for(int i=0;i<N;i++)
        {
            for(int j=0;j<M;j++)
            {
                scanf("%d",&mat[i][j]);
            }
        }

    //rows max
     for(int i=0;i<N;i++)
     {
         for(int j=0;j<M;j++)
         row_max[i]=max(row_max[i],mat[i][j]);
     }

     //cols max
     for(int i=0;i<M;i++)
     {
         for(int j=0;j<N;j++)
         col_max[i]=max(col_max[i],mat[j][i]);

     }

     //for(int i=0;i<N;i++)printf("%d ",row_max[i]);
     //printf("\n");

     //for(int i=0;i<M;i++)printf("%d",col_max[i]);
     //printf("\n");

    for(int i=0;i<N;i++)
    {
        for(int j=0;j<M;j++)
        {
            if(mat[i][j]==col_max[j] || mat[i][j]==row_max[i])
            flag=1;

            else{
            flag=0;
            break;
            }
        }
        if(!flag)break;
    }

    if(flag==1){
    printf("Case #%d: YES\n",test);
    }

    else{
    printf("Case #%d: NO\n",test);
    }

    }
    return 0;
}
