#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
    int t;
    scanf("%d",&t);
    
    for(int tt=1;tt<=t;tt++)
    {
            int n,m;
            scanf("%d%d",&n,&m);
            int a[n][m];
            int rm[n];
            int cm[m];
            for(int i=0;i<n;i++)
               rm[i]=0;
            for(int j=0;j<m;j++)
               cm[j]=0;   
            for(int i=0;i<n;i++)
            {
                    for(int j=0;j<m;j++)
                    {
                            scanf("%d",&a[i][j]);                
                            if(a[i][j]>rm[i])
                               rm[i]=a[i][j];
                            if(a[i][j]>cm[j])
                               cm[j]=a[i][j];
                            
                    }
            }
            int po=0;
            for(int i=0;i<n;i++)
            {
                    for(int j=0;j<m;j++)
                    {
                            if((a[i][j]!=rm[i])&&(a[i][j]!=cm[j]))
                            {          po=1;
                                       i=n;
                                       j=m;
                            }                            
                    }
            }
            if(po==0)
                 printf("Case #%d: YES\n",tt);
            else printf("Case #%d: NO\n",tt);
    }
    system("pause");
    return 0;
}
