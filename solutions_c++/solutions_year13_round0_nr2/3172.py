#include<iostream>
#include<string.h>
#include<stdio.h>
using namespace std;
int i,j,k,n,m,a[104][103],b[104][104];
int main()
{
    int cs,t=0;
    freopen("B-large.in","r",stdin);
    freopen("B.txt","w",stdout); 
    scanf("%d",&cs);
    while (t++<cs)
    {
          scanf("%d%d",&n,&m);
          for (int i = 0;  i<n; i++)
          {
              for (int j = 0 ; j < m ; j++){
              scanf("%d",&a[i][j]);b[i][j]=103;}
          }
          for (int i = 0 ; i < n ; i++)
          {
              int d= 0;
              for (int j = 0 ; j < m ; j++)
                  if  (a[i][j] > d)
                    d=a[i][j];
              for (int j = 0 ; j < m; j++)
                  if (b[i][j] > d)
                  b[i][j]=d;
          }
          for (int i = 0 ; i < m ; i++)
          {
              int d= 0;
              for (int j = 0 ; j < n ; j++)
                  if  (a[j][i] > d)
                    d=a[j][i];
              for (int j = 0 ; j < n; j++)
                  if (b[j][i] > d)
                  b[j][i]=d;
          }
          int ok = 1;
          for (int i = 0 ; i < n ; i++){
          for (int j = 0; j < m ; j++){
          ok&=(a[i][j]==b[i][j]);}}
          printf("Case #%d: ", t);
          if (ok==1) puts("YES");
          else puts("NO");
    }
}
