#include <iostream>
using namespace std;

int main() {
	int t,n1,n2,k,p,i,j,c,x,z=1;
cin>>t;
while(t--)
{
c=0;
cin>>n1>>n2>>k;
for(i=0;i<n1;i++)
for(j=0;j<n2;j++)
{
if((i&j)<k )
c++;
}
cout<<"Case #"<<z<<": "<<c<<"\n";
z++;
}
	return 0;
}