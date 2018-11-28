#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
ll t,n,z,m,k;
scanf("%lld",&z);
for(ll t=1;t<=z;t++)
{
scanf("%lld",&n);

if(n==0)
{
printf("Case #%lld: INSOMNIA\n",t);
continue;
}
k=2;
m=n;

int arr[10];
memset(arr,0,sizeof(arr));

while(1)
{
bool flag=true;
//cout<<m<<"pk";
//store digits
while(m>0)
{
arr[m%10]=1;
m/=10;
}
//for(ll i=0;i<10;i++)
//cout<<i<<" "<<arr[i]<<endl;
//check if all visited
for(ll i=0;i<10;i++)
{
if(arr[i]==0)
{
flag=false;
break;
}
}


if(flag==true)
{
printf("Case #%lld: %lld\n",t,n*(k-1));
flag=false;
break;
}
m=k*n;
k++;
}

}

return 0;
}
