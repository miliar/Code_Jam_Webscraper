#include<cstdio>
int min(int a,int b);
int main()
{
    int t;
    scanf("%d",&t);
    for(int k=1;k<=t;k++)
    {
              int m,n,check=0;
              scanf("%d%d",&m,&n);
              int a[m][n],max=0,row[m],col[n];
              for(int i=0;i<m;i++)
              {
                      for(int j=0;j<n;j++)
                      {
                              scanf("%d",&a[i][j]);
                              if(max<a[i][j])max=a[i][j];
                      }
                      row[i]=max;
                      max=0;
              }
              for(int i=0;i<n;i++)
              {
                      for(int j=0;j<m;j++)
                      {
                              if(max<a[j][i])max=a[j][i];
                      }
                      col[i]=max;
                      max=0;       
              }
              for(int i=0;i<m;i++)
              {
                      for(int j=0;j<n;j++)
                      {
                              if(min(row[i],col[j])>a[i][j])check=1;
                      }
              }
              if(check==0)printf("Case #%d: YES\n",k);
              else printf("Case #%d: NO\n",k);
    }
}
int min(int a,int b)
{
    if(a<b)return a;
    else return b;
}
              
              
