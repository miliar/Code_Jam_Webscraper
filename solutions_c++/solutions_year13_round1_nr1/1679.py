# include<iostream>
using namespace std;
int main()
{
int y,x,r,t,d,j,i;
cin>>y;
for(x=1;x<=y;x++)
{
cin>>r>>t;
j=0;
for(i=1;true;i=i+2)
{
d=((r+i)*(r+i))-((r+i-1)*(r+i-1));
if(d<=t)
{
t=t-d;
j++;
}
else
break;
}
cout<<"Case #"<<x<<": "<<j<<"\n";
}
return 0;
}
