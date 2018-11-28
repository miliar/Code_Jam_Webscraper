#include <iostream>
using namespace std;

int main() {
int t,i,c1,c2,a[4],b[4],z,j,c,x,f=1;
cin>>t;
while(t--)	
{
cin>>c1;
for(i=0;i<((c1-1)*4);i++)
 cin>>z;
for(i=0;i<4;i++)
  {
cin>>a[i];
}
for(i=0;i<(16-(c1)*4);i++)
 cin>>z;
cin>>c2;
for(i=0;i<((c2-1)*4);i++)
 cin>>z;
for(i=0;i<4;i++)
  {
cin>>b[i];
}
for(i=0;i<16-(c2)*4;i++)
 cin>>z;
c=0;
for(i=0;i<4;i++)
for(j=0;j<4;j++)
{
if(a[i]==b[j])
{
c++;
x=i;
}
}
if(c==1)
cout<<"Case #"<<f<<": "<<a[x];
else if(c==0)
cout<<"Case #"<<f<<": "<<"Volunteer cheated!";
else if(c>=2)
cout<<"Case #"<<f<<": "<<"Bad magician!";
cout<<"\n";
f++;
}
return 0;
}