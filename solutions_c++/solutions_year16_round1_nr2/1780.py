#include<iostream>
#include<string.h>
#include<vector>
#include<algorithm>
using namespace std;



int main()
{
long long i,j,k,l,h,m,n,o,t,c,s,arr[100][50];
cin>>t;
for(o=1;o<=t;o++)
{
cin>>n;
cout<<"Case #"<<o<<": ";
long long h[2501]={0};
for(i=0;i<2*n-1;i++)
{
    for(j=0;j<n;j++)
        {
            cin>>arr[i][j];
            h[arr[i][j]]++;
        }
}
for(i=1;i<2501;i++)
    if(h[i]%2==1)
    cout<<i<<" ";
cout<<endl;


}



}
