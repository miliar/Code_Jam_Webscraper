#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int t,T,n,m,a[200][200],maxx[200][200],maxy[200][200];
bool ch;
char c[6][6];

int main(){
    int i,j;
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        ch=true;
        scanf("%d%d",&n,&m);
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
                scanf("%d",&a[i][j]);
            }
        }
        for(i=0;i<n;i++)
        {
            maxx[t][i]=a[i][0];
        }
        for(i=0;i<m;i++)
        {
            maxy[t][i]=a[0][i];
        }
        for(i=0;i<n;i++)
        {
            for(j=1;j<m;j++)
            {
                if(a[i][j]>maxx[t][i])maxx[t][i]=a[i][j];
            }
        }
        for(i=1;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
                if(a[i][j]>maxy[t][j])maxy[t][j]=a[i][j];
            }
        }
        /*//
        for(i=0;i<n;i++)
        {
            printf("%d ",maxx[t][i]);
        }
        printf("\n");
        for(i=0;i<m;i++)
        {
            printf("%d ",maxy[t][i]);
        }
        printf("\n");
        //*/
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
                if(a[i][j]<maxx[t][i] && a[i][j]<maxy[t][j])ch=false;
            }
        }
        if(ch)printf("Case #%d: YES\n",t);
        else printf("Case #%d: NO\n",t);
    }    
    scanf(" ");
    return 0;
}
/*
5 5
3 3 2 1 4
1 2 1 3 2
1 2 1 3 2
1 1 1 2 2
3 2 1 3 1

*/
