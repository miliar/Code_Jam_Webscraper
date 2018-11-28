#include<iostream>
#include<cstdio>
using namespace std;
int main(){
    long long int t,j;
    freopen ("input.txt","r",stdin);
    freopen ("output.txt","w",stdout);
    cin>>t;
    for(j=1;j<=t;j++)
    {
              long long int m,i,b=0;
              cin>>m;
              long long int arr[m];
              for(i=0;i<m;i++){
                               cin>>arr[i];
                               }
              long long int diff=0,a=0;
              for(i=0;i<m-1;i++){
                                 //cout<<i<<':'<<arr[i]<<':'<<arr[i+1]<<";";
                                 long long int d=arr[i+1]-arr[i];
                                 if(-d>diff)
                                 diff=-d;
                                 if(d<0)
                                 a-=d;
                                 //cout<<d<<endl;
                                 }
              for(i=0;i<m-1;i++){
                                 if(arr[i]<diff)
                                 b+=arr[i];
                                 else
                                 b+=diff;
                                 }
              cout<<"Case #"<<j<<": "<<a<<" "<<b<<endl;
    }
    cin.get();
    cin.get();
    }
