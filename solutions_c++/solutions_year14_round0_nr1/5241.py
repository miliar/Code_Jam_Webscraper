#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
    int T,m,n,a[4][4],b[4][4],ct,k;
    cin>>T;
    for(int l=0;l<T;l++)
    {
              cin>>m;
              ct=0;
              for(int i=0;i<4;i++)
              {
                      for(int j=0;j<4;j++)
                      {
                              cin>>a[i][j];
                      }
              }
              cin>>n;
              for(int i=0;i<4;i++)
              {
                      for(int j=0;j<4;j++)
                      {
                              cin>>b[i][j];
                      }
              }
              k=0;
              for(int i=0;i<4;i++)
              {
                      for(int j=0;j<4;j++)
                      {
                              if(a[m-1][i]==b[n-1][j])
                              {
                                                         ct++;
                                                         k=a[m-1][i];
                              }
                      }
              }
              if(ct==0)
              {
                       printf("Case #%d: Volunteer cheated!\n",l+1);
              }
              else if(ct==1)
              {
                   printf("Case #%d: %d\n",l+1,k);
              }
              else if(ct>1)
              {
                   printf("Case #%d: Bad magician!\n",l+1);
              }
    }
}
