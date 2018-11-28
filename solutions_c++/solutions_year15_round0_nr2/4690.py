#include<bits/stdc++.h>
using namespace std;



int a[1200];

int main(){


int t ,x=1 ;
int n ,max1,min1,sum;

cin>>t;

while(t--){
              cin>>n;
             for(int i=0;i<n; i++)
             {
              cin>>a[i];
              max1 = max(max1,a[i]);
              }

             min1 = max1;

             for(int i=1;i<=max1;i++)
             {
              sum=i;
             for(int j=0;j<n;j++)
             {
                 if(a[j]>i)
                  {
                    if( a[j]%i == 0 )
                    {sum +=(a[j]/i-1);}
                    else
                     {sum +=(a[j]/i);}
                  }
             }
               min1 = min(min1,sum) ;
             }
             cout<<"Case #"<<x<<": "<< min1<<endl;
             x++;
            }
            }














