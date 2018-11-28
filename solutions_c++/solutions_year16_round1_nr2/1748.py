#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
int t,n;
cin>>t;
for(int z=1;z<=t;z++)
{
cin>>n;
int arr[2505],mini=9999;
memset(arr,0,sizeof(arr));
for(int i=0;i<(2*n-1);i++)
{
for(int j=0;j<n;j++)
{
int a;
cin>>a;
arr[a]++;
}
}
int cnt=0;
cout<<"Case #"<<z<<": ";
for(int i=1;i<=2500;i++)
{
if(arr==0)
continue;

if(arr[i]%2!=0)
{
cout<<i;
cnt++;
if(cnt!=n)
cout<<" ";
}
}
cout<<endl;

}

return 0;
}
