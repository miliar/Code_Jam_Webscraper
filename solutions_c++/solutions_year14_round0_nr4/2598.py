#include <cstdio>
#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;
double arr[1011],brr[1011];
bool mark[1011];
int main()
{
    freopen("qns.txt","r",stdin);
    freopen("ans.txt","w",stdout);
    int t,lans,rans,N;
    double x,y;
    scanf("%d",&t);
    for(int test=1;test<=t;test++)
    {
      lans=rans=0;
      scanf("%d",&N);
      for(int i=0;i<N;i++)
        scanf("%lf",&arr[i]);
      sort(arr,arr+N);
      for(int i=0;i<N;i++)
        scanf("%lf",&brr[i]);
      sort(brr,brr+N);
      memset(mark,true,sizeof mark);
      for(int i=0;i<N;i++)
      {
          int flag=0;
          for(int j=0;j<N;j++)
          {
            if(brr[j]>arr[i] && mark[j]==true)
            {
              mark[j]=false;
              flag=1;
              break;
            }
          }
          if(flag)
                rans++;
      }
      memset(mark,true,sizeof mark);
      for(int i=N-1;i>=0;i--)
      {
          int flag=0;
          for(int j=0;j<N;j++)
          {
             if(arr[j]>brr[i] && mark[j]==true)
             {
                 mark[j]=false;
                 flag=1;
                 break;
             }
          }
             if(flag)
                lans++;
      }
      printf("Case #%d: %d %d\n",test,lans,N-rans);
    }
    return 0;
}
