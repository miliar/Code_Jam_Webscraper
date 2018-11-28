#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
int t;
cin>>t;
for(int i=1;i<=t;i++)
{
int n;
cin>>n;
double arr1[n];
double arr2[n];
for(int k=0;k<n;k++)
{
cin>>arr1[k];
}
sort(arr1,arr1+n);
for(int j=0;j<n;j++)
{
cin>>arr2[j];
}
sort(arr2,arr2+n);
int a=0;
int b=0;
int ans=0;
int ans1=0;
while(1)
{
if(arr2[b]>arr1[a])
{
ans++;
a++;
b++;
}
else
{
b++;
}
if(a==n||b==n)
break;
}
ans=n-ans;
a=0;
b=0;
while(1)
{
if(arr2[b]<arr1[a])
{
ans1++;
a++;
b++;
}
else
{
a++;
}
if(a==n||b==n)
break;
}
cout<<"Case #"<<i<<": "<<ans1<<" "<<ans<<endl;
}
return 0;
}
