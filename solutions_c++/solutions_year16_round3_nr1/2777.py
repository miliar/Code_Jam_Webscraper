#include<iostream>
#include<string>
#include<fstream>

using namespace std;

int fmax(int cost[][100],int n){  int m=cost[1][1],c=1;
                               for(int i=1;i<n+1;i++)
                                 { if(cost[i][1]>m)
                                     {m=cost[i][1];
                                        c=i;  }
                                     }

                                     return c;}

int main(){   fstream in("input.in");
               ofstream out("output.in");
                  int t;
               in>>t;
               for(int a=1;a<t+1;a++)
               {

              int n,cost[27][100];
              in>>n;
              for(int i=1;i<n+1;i++)
              {
                 cost[i][0]=64+i;
              }
               for(int i=1;i<n+1;i++)
              {
                 in>>cost[i][1];
              }
            int xx=1;
            out<<"Case #"<<a<<":"<<" ";
            while(xx)  {  int mcol=fmax(cost,n);
            int cnt=0,arr[27];

            for(int i=1;i<n+1;i++)
            {    if(cost[i][1]==cost[mcol][1])
                   {  cnt++;
                       arr[cnt]=i;
                   }}
              if(cnt==1 || cnt==3)
              {  char as = char(cost[arr[1]][0]);
                  out<<as<<" ";
                  cost[arr[1]][1]=cost[arr[1]][1]-1;

              }
              else {  char as1 = char(cost[arr[1]][0]);
                      char as2 = char(cost[arr[2]][0]);
                        out<<as1<<as2<<" ";
                        cost[arr[1]][1]=cost[arr[1]][1]-1;
                        cost[arr[2]][1]=cost[arr[2]][1]-1;
                         }
                int cx=0;

                    for(int ii=1;ii<n+1;ii++)
                         {
                           if(cost[ii][1]==0)
                                cx++;
                         }
                         if(cx==n)
                            {xx=0;
                              out<<endl;}   }
               }
               return 0;    }
