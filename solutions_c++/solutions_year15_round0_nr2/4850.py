#include<bits/stdc++.h>
using namespace std;
int main(){
int a[1200];
int t ,x=1 ;
int n ,M,mn,tm;
cin>>t;
while(t--){
              cin>>n;
             for(int i=0;i<n; i++)
             {
              cin>>a[i];
              M = max(M,a[i]);
              }

             mn = M;

             for(int i=1;i<=M;i++)
             {
              tm=i;
             for(int j=0;j<n;j++)
             {
                 if(a[j]>i)
                  {
                    if( a[j]%i == 0 )
                    {tm+=(a[j]/i-1);}
                    else
                     {tm+=(a[j]/i);}
                  }
             }
               mn =min(mn,tm);
             }
             cout<<"Case #"<<x<<": "<< mn<<endl;
             x++;
            }
            }