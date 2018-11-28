#include<iostream>
#include<cmath>
using namespace std;

bool is_palin(long long int x)
{
string t="";
char y;
while(x>0)
{
y='0'+(x%10);
t+=y;
x/=10;
}
for(int i=0;i<(t.length())/2;i++)
{
if(t[i]!=t[t.length()-i-1])
return false;
}
return true;
}

int main()
{
long long int t,a,b,cnt;
cin>>t;
for(int i=0;i<t;i++)
{
cin>>a>>b;
cnt=0;
for(int j=sqrt(a);j*j<=b;j++)
{
if(j*j<a)
continue;
if(is_palin(j) && is_palin(j*j))
cnt++;
}
cout<<"Case #"<<i+1<<": "<<cnt<<endl;
}
return 0;
}
