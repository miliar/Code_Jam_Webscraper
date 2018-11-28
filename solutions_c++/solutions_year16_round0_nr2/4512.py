#include <iostream>
#include <string>
using namespace std;

int main()
{
int t;int c=1;
string s;
cin>>t;
getline(cin,s);
while(c<=t)
{
getline (cin,s);
int n=s.length();
int i;
int a[n];
int b[n];
for(i=0;i<n;i++)
{
a[i]=0;
b[i]=0;
}
if(s[0]=='-')
{
a[0]=1;
}
else
{
b[0]=1;
}
for(i=1;i<n;i++)
{
if(s[i]=='+')
{
a[i]=a[i-1];
b[i]=a[i-1]+1;
}
else
{
a[i]=b[i-1]+1;
b[i]=b[i-1];
}
}
cout<<"Case #"<<c<<": "<<a[n-1]<<endl;
c++;
}

return 0;
}
