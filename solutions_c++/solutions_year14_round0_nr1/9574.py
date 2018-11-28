#include<cstdio>
#include<iostream>
using namespace std;

int main()
   {
       int t;
       cin>>t;

       for(int k=1;k<=t;k++)
       {
           int count=0;
           int ans;
           int a[4][4],b[4][4];
           int xc[4],yc[4];
           int x,y;
           cin>>x;
           for(int i=0;i<4;i++)
           {
               for(int j=0;j<4;j++)
               {
                   cin>>a[i][j];
                   if(i==x-1)
                       xc[j]=a[i][j];
               }
           }

           cin>>y;
           for(int i=0;i<4;i++)
           {
               for(int j=0;j<4;j++)
               {
                   cin>>b[i][j];
                   if(i==y-1)
                       yc[j]=b[i][j];
               }
           }
           for(int i=0;i<4;i++)
           {
               for(int j=0;j<4;j++)
               {
                   if(xc[i]==yc[j])
                   {
                       count++;
                       ans=xc[i];
                       if(count>1)
                          break;

                   }

                   if(count>1)
                      break;
               }
           }
           if(count>1)
               cout<<"Case #"<<k<<":"<<' '<<"Bad magician!"<<endl;
           else if(count==0)
                cout<<"Case #"<<k<<":"<<' '<<"Volunteer cheated!"<<endl;
           else
                  cout<<"Case #"<<k<<":"<<' '<<ans<<endl;
       }
   }
