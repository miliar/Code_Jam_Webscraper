#include <iostream>
using namespace std;

int main()
{
int t;int m=1;
cin>>t;
while(m<=t)
{
int k,c,s;
cin>>k>>c>>s;
int i;
cout<<"Case #"<<m<<": 1";
for(i=2;i<=s;i++)
{
cout<<" "<<i;
}

cout<<endl;
m++;
}

return 0;
}
