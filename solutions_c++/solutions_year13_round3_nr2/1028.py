#include<iostream>
#include<string>

using namespace std;

char alt(char a)
{
if(a=='N')
return 'S';
if(a=='S')
return 'N';
if(a=='E')
return 'W';
if(a=='W')
return 'E';
}

int main(){
int t;
cin>>t;

for(int k=1;k<=t;k++)
{
int x,y;
cin>>x>>y;

char a='W';
if(x<0)
{a='E';
x=-x;
}

cout<<"Case #"<<k<<": ";
while(x--)
{
cout<<a<<alt(a);
}

a='S';
if(y<0)
{
a='N';
y=-y;
}

while(y--)
{
cout<<a<<alt(a);
}

cout<<endl;
}
}