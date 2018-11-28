#include <iostream>
using namespace std;
const int maxN=10+5;
const int maxM=10+5;
int main()
{
    freopen("B-small-attempt1.in","r",stdin);
    freopen("B-small-attempt1.out","w",stdout);
    //freopen("B-large.in","r",stdin);
    //freopen("B-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int k=0;k<T;k++){                                                     //int k=0;
            int w=1;
            printf("Case #%d: ",k+1);
            int N, M, a[maxN][maxM];
            scanf("%d%d",&N,&M);                                                 //printf("N=%d,M=%d\n",N,M);
            for(int i=0;i<N;i++)
                for(int j=0;j<M;j++)
                     scanf("%d",&a[i][j]);
            for(int i=0;i<N;i++){
                for(int j=0;j<M;j++){                                            //if((i==1)&&(j==0)) printf("WAH-WAH");
                        if(a[i][j]==2)
                             continue;
                        else for(int l=0;l<M;l++){
                             if(a[i][l]==1)
                                 continue;
                             else for(int m=0;m<N;m++)
                                     if(a[m][j]==1)
                                          continue;
                                     else{
                                         printf("NO\n");
                                         w=0;
                                         break;
                                     }
                             break;
                             }
                        if(w==0)                                                 //{printf("2nd break");
                           break;                                                // }
                }
                if(w==0)                                                        // {printf("3rd break");
                   break;                                                         //}
            }    
                if(w==1)
                printf("YES\n");
    }
    return 0;
}
