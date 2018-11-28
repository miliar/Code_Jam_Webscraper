#include<bits/stdc++.h>
using namespace std;
 
 
 
 
 
int main(){
int a[1200];
 
int t ,x=1 ;
int n ,maxx,minn,time;
 
cin>>t;
 
while(t--){
              cin>>n;
             for(int i=0;i<n; i++)
             {
              cin>>a[i];
              maxx = max(maxx,a[i]);
              }
 
             minn = maxx;
 
             for(int i=1;i<=maxx;i++)
             {
              time=i;
             for(int j=0;j<n;j++)
             {
                 if(a[j]>i)
                  {
                    if( a[j]%i == 0 )
                    {time+=(a[j]/i-1);}
                    else
                     {time+=(a[j]/i);}
                  }
             }
               minn =min(minn,time);
             }
             cout<<"Case #"<<x<<": "<< minn<<endl;
             x++;
            }
            }
