#include<iostream>
#include<stdio.h>
#include<vector>
#include<algorithm>
#include<set>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<map>
#include<deque>
using namespace std;
int arr[105][105];
int newone[105][105];
int cost[105];
int abs(int f)
{
    if(f<0)
       return 0-f;
    else
       return f;
}
int money(int N)
{
    int sum=0,i,j;
    for(i=1;i<=N;i++)
      for(j=1;j<=N;j++)
      {
          sum+=arr[i][j]*cost[abs(i-j)];
      }
    return sum;
}
int main()
{
    freopen("sampleinput.txt","r",stdin);
    freopen("sampleoutput.txt","w",stdout);
    int tnum,numtc;
    int N,M,i,j,a,b,p,k,l,num;
    scanf("%d",&numtc);
    for(tnum=1;tnum<=numtc;tnum++)
    {
        scanf("%d%d",&N,&M);
        cost[0]=0;
        for(i=1;i<=N;i++)
          cost[i]=cost[i-1]+N-i+1;
        for(i=1;i<=N;i++)
          for(j=1;j<=N;j++)
             arr[i][j]=0;
        for(i=0;i<M;i++)
        {
            scanf("%d%d%d",&a,&b,&p);
            arr[a][b]+=p;
        }
        int now=money(N),prev,after;
        prev=now;
        int flag=0;
        while(1)
        {
            flag=0;
            for(i=1;i<=N;i++)
               for(j=1;j<=N;j++)
               {
                   if(arr[i][j]==0)
                      continue;
                   else
                   {
                       if(i<j)
                       {
                           for(k=i+1;k<=j;k++)
                             for(l=1;l<k;l++)
                             {
                                 if(arr[k][l]>0)
                                 {
                                    num=min(arr[i][j],arr[k][l]);
                                    if(num>0)
                                    {
                                      arr[i][j]-=num;
                                      arr[k][l]-=num;
                                      arr[i][l]+=num;
                                      arr[k][j]+=num;
                                      flag=1;
                                    }
                                 }
                             }
                           for(k=i+1;k<=j;k++)
                             for(l=j+1;l<=N;l++)
                             {
                                 if(arr[k][l]>0)
                                 {
                                    num=min(arr[i][j],arr[k][l]);
                                    if(num>0)
                                    {
                                      arr[i][j]-=num;
                                      arr[k][l]-=num;
                                      arr[i][l]+=num;
                                      arr[k][j]+=num;
                                      flag=1;
                                    }
                                 }
                             }
                       }
                       else if(i>j)
                       {
                          for(k=j+1;k<=i;k++)
                             for(l=k+1;l<=N;l++)
                             {
                                 if(arr[k][l]>0)
                                 {
                                    num=min(arr[i][j],arr[k][l]);
                                    if(num>0)
                                    {
                                      arr[i][j]-=num;
                                      arr[k][l]-=num;
                                      arr[i][l]+=num;
                                      arr[k][j]+=num;
                                      flag=1;
                                    }
                                 }
                             }
                          for(k=j+1;k<=i;k++)
                             for(l=1;l<j;l++)
                             {
                                 if(arr[k][l]>0)
                                 {
                                    num=min(arr[i][j],arr[k][l]);
                                    if(num>0)
                                    {
                                      arr[i][j]-=num;
                                      arr[k][l]-=num;
                                      arr[i][l]+=num;
                                      arr[k][j]+=num;
                                      flag=1;
                                    }
                                 }
                             }
                       }

                   }
               }
               after=money(N);
               if(flag==0 || after==prev)
               break;
               prev=after;
        }
        after=money(N);
        printf("Case #%d: %d\n",tnum,now-after);
    }
    return 0;
}

