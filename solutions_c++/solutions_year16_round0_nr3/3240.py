#include<bits/stdc++.h>
#include<iostream>
using namespace std;
int t,n,j,arr[70000][17]={0};
int main()
{
freopen("outputcode.txt","w",stdout);
      scanf("%d%d%d",&t,&n,&j);
      printf("Case #1:\n");
      while(t--)
      {
            int tmp,vr=1,fg;

                  for(int i=0;i<65536;i++)
                  {
                        arr[i][0]=1;
                         arr[i][15]=1;
                  }
                  for(int i=1;i<15;i++)
                  {
                        tmp=ceil(pow(2,14-i));
                        vr=1;
                        for(int k=0;k<65536;k++)
                        {
                              arr[k][i]=vr;
                              tmp--;
                              if(tmp==0)
                              {
                                    tmp=ceil(pow(2,14-i));
                                    if(vr==0)
                                    vr=1;
                                    else
                                    vr=0;
                              }
                        }
                  }


           for(int i=0;i<65536&&j>0;i++)
            {//cout<<i;
                  long long int rr[11]={0},flg=0;

                        for(int m=2;m<=10;m++)
                        {
                              long long int no=0;
                              for(int k=1;k<=n;k++)
                              {
                                    no+=(ceil(pow(m,n-k))*arr[i][k-1]);
                              }
                              for(long long int k=2;k*k<=no;k++)
                              {
                                    if(no%k==0)
                                    {
                                      rr[m]=k;
                                      break;
                                    }
                              }

                        }
                  for(int m=2;m<=10;m++)
                  {
                        if(rr[m]==0)
                        flg=1;
                  }

                  if(flg==1)
                  continue;
                  for(int m=0;m<n;m++)
                  printf("%d",arr[i][m]);printf(" ");j--;
                  for(int m=2;m<=10;m++)
                  {
                        printf("%lld ",rr[m]);
                  }
                  printf("\n");
            }

      }
}
