#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

double block[2][1010];

int compare(const void *a,const void *b)
{
    double aa=*(double *)a,bb= *(double *)b;
    if(aa>bb)return 1;
    if(aa<bb)return -1;
    else return 0;
}

int main()
{
    int N,n,c,i,j,ans,ans2,cur;
    scanf("%d",&N);
    for(c=1;c<=N;c++){
        scanf("%d",&n);
        for(i=0;i<2;i++){
            for(j=0;j<n;j++){
                scanf("%lf",&block[i][j]);
            }
        }
        qsort(block[0],n,sizeof(double),compare);
        qsort(block[1],n,sizeof(double),compare);

        cur=0;
        ans=n;
        ans2=0;
        for(i=0;i<n;i++){
            if(block[1][i]>block[0][cur]){
                ans--;
                cur++;
            }
        }
        cur=0;
        for(i=0;i<n;i++){
            if(block[0][i]>block[1][cur]){
                ans2++;
                cur++;
            }
        }
        printf("Case #%d: ",c);
        printf("%d %d\n",ans2,ans);
    }
    return 0;
}
