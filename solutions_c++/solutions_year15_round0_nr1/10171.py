#include<bits/stdc++.h>
#include<iostream>
using namespace std;
#define s(x) scanf("%lld",&x)
#define ll long long int
int main()
{
 ll t,k;
 s(t);
 for(k=0;k<t;k++)
 {
 ll n,j=0,sum=0,i;
 s(n);
 string s1;
 ll a[n+1];
 cin>>s1;
 a[0]=(int)s1[0]-48;
 for(i=1;i<=n;i++)
 {
     sum=sum+(int)s1[i-1]-48;
     a[i]=sum+j;
  if(a[i]<i && s1[i]-'48'!=0)
  j=j+i-a[i];
}
printf("Case #%lld: %lld\n",k+1,j);
 }

}

