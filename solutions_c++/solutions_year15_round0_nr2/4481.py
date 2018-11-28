#include <stdio.h>
#include <algorithm>
using namespace std;
int check[10];
int DFS(int k)
{
    int minn=k;
    if(k==0)
        return 0;

    if(check[k]!=0)
    {
        for(int i=k-1;i>=1;i--)
        {
            check[i]+=check[k];
            check[k-i]+=check[k];
            minn = min(minn,DFS(k-1)+check[k]);
            check[i]-=check[k];
            check[k-i]-=check[k];
        }
    }
    
    else return DFS(k-1);
    return minn;
}
int main(){
    
    int t,i,j,a;
    
    freopen("B-small-attempt2.in","r",stdin);
    freopen("B-small-attempt2.out","w",stdout);
    
    scanf("%d",&t);
    for(int o=0;o<t;o++)
    {
        for(i=0;i<10;i++)
            check[i]=0;
        int temp[10];

        scanf("%d",&a);
        for(j=0;j<a;j++)
        {
            scanf("%d",&temp[j]);
            check[temp[j]]++;
        }
        printf("Case #%d: %d\n",o+1,DFS(9));
    }
}
