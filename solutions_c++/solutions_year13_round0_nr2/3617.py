#include<stdio.h>
int max[100];
int main()
{
    freopen ("a.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t,n,m,a[100][100],q=0,temp[100][100];
    scanf("%d",&t);
    while(t--)
    {
              q++;
              scanf("%d %d",&n,&m);
              for(int i=0;i<n;i++)
              {
                      max[i]=0;
                      for(int j=0;j<m;j++)
                      {
                                          scanf("%d",&a[i][j]);
                                          temp[i][j]=100;
                                          if(max[i]<a[i][j])
                                                            max[i]=a[i][j];
                      }
              }
              
              for(int i=0;i<n;i++)
                      for(int j=0;j<m;j++)
                              temp[i][j]=max[i];
              
              for(int j=0;j<m;j++)
              {
                      max[j]=0;
                      for(int i=0;i<n;i++)
                      {
                              if(max[j]<a[i][j])
                                                max[j]=a[i][j];
                      }
              }
              
              for(int j=0;j<m;j++)
                      for(int i=0;i<n;i++)
                       {
                              if(temp[i][j]>max[j])
                                     temp[i][j]=max[j];
                       }
              
              int check=0;
              //Matching
              for(int i=0;i<n;i++)
              {
                      for(int j=0;j<m;j++)
                              if(a[i][j]!=temp[i][j])
                              {
                                                     check=1;
                                                     break;
                              }
                      if(check==1)
                                  break;
              }
              if(check==0)
                          printf("Case #%d: YES\n",q);
              else
                  printf("Case #%d: NO\n",q);
    }
    return 0;
}
