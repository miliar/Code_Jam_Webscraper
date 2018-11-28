#include <iostream>
#include<string>
using namespace std;
int main()
{
int test,cas=1;
cin>>test;
while(test--)
{
string str; int c=0,q;
cin>>str;
q=str.length();
//cout<<q<<endl;
while(q--)
{
if(str.at(q)=='-')
{
c++;
for(int i=0;i<=q;i++)
{
if(str.at(i)=='-')
{str.at(i)='+';}
else
{str.at(i)='-';}
}
}
}
cout<<"Case #"<<cas<<": "<<c<<endl;
cas++;
}
}

