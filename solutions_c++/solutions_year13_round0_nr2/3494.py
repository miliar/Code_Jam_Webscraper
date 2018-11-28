#include<iostream>
#include<cstdio>
int main()
{
    freopen("B1.in","r",stdin);
	freopen("B1.out","w",stdout);
    int arr[200][200],n,m,t,i,j,ii,flag,w1,w2,min,k;
    scanf("%d",&t);
    for(ii=0;ii<t;ii++)
    {
         flag=0;
         scanf("%d %d",&n,&m);
         for(i=0;i<n;i++)
         {
             for(j=0;j<m;j++)
                 scanf("%d",&arr[i][j]);
         }
         for(i=0;i<n;i++)
         {
             for(j=0;j<m;j++)
             {
                 min=arr[i][j];
                 w1=0;w2=0;
                 for(k=0;k<m;k++)
                 {
                     if(min<arr[i][k])
                           w1=1;
                 }
                 for(k=0;k<n;k++)
                 {
                      if(min<arr[k][j])
                           w2=1;
                 }
                 if((w1==1)&&(w2==1))
                 {
                       printf("Case #%d: NO\n",ii+1);
                       flag=1;
                       break;
                 }
             }
             if(flag==1)
                 break;
         }
         if(i==n&&j==m)
            printf("Case #%d: YES\n",ii+1);  
    }
}                
