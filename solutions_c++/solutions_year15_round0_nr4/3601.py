#include<iostream>
#include<string>
using namespace std;

int main()
{
long int t,n,r,c,i,j;
cin>>t;
string s[t+1];
for(i=1;i<=t;i++)
{cin>>n>>r>>c;
/*if(c<r)
{c=c+r;
r=c-r;
c=c-r;}*/
r=r*c;
if(n==1)
s[i]="GABRIEL";


if((n==2)&&((r==9)||(r==3)||(r==1)))
{s[i]="RICHARD";}
else if(n==2)
    s[i]="GABRIEL";

if((n==3)&&((r==9)||(r==12)||(r==6)))
{s[i]="GABRIEL";}
else if(n==3)
    s[i]="RICHARD";

if((n==4)&&((r==12)||(r==16)))
{s[i]="GABRIEL";}
else if(n==4)
    s[i]="RICHARD";
}

for(long i=1;i<=t;i++)
{
cout<<"Case #"<<i<<": "<<s[i]<<"\n";
}
return 0;}
