#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen ("in.txt","r",stdin);
    freopen ("out.txt","w",stdout);
  int t,val,l,i,sum,n;
char str[100003];
cin>>t;
for(l=0;l<t;l++)
{
cin>>n;
cin>>str;
val=str[0]-'0';
sum=0;
for(i=1;i<=n;i++)
{
if(val<i)
{
sum+=i-val;
val+=(i-val);
}
val+=(str[i]-'0');
}
cout<<"Case #"<<(l+1)<<": "<<sum<<endl;
}
return 0;
}
