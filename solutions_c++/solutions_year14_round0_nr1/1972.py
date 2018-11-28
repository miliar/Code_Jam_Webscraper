#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
using namespace std;
int T,C,i,j,x,p,ans,a[10][10],f[50];
int main()
{
    freopen("A-small-attempt2.in","r",stdin);
    freopen("A-small-attempt2.out","w",stdout);
    scanf("%d",&T);
    for (C=1;C<=T;C++)
    {
        scanf("%d",&x);    
        for (i=1;i<=4;i++) 
        for (j=1;j<=4;j++) scanf("%d",&a[i][j]);
        memset(f,0,sizeof(f));
        for (j=1;j<=4;j++) f[a[x][j]]++;
        
        scanf("%d",&x);    
        for (i=1;i<=4;i++) 
        for (j=1;j<=4;j++) scanf("%d",&a[i][j]);
        for (j=1;j<=4;j++) f[a[x][j]]++;        
        p=0;
        for (i=1;i<=16;i++)
        if (f[i]==2)
        {
            p++; ans=i;
        }
        printf("Case #%d: ",C);
        if (p==1) printf("%d\n",ans);
        else if (p<1) printf("Volunteer cheated!\n");
        else printf("Bad magician!\n");
    }
    
    return 0;    
}
