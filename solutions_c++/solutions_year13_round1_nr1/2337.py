#include<iostream>

int main()
{
using namespace std;
int r,n,i,j;
int t,black;
cin>>n;

for(i=1;i<=n;i++)
{
black=0;
cin>>r>>t;
//paint-=r*r;
t-=((r+1)*(r+1))-(r*r);
black++;
r+=2;
while(t>0)
{
t-=((r+1)*(r+1))-(r*r);
if(t>=0)
{
r+=2;
black++;
}

else 
break;
}

cout<<"Case #"<<i<<": "<<black<<"\n";
}
return 0;
}
