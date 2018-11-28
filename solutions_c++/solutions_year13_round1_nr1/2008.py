#include<iostream>
#include<cmath>
using namespace std;
int main()
{
int t;
cin>>t;
long long int r,thick,a,n,i,j;
for(int kk=1;kk<=t;kk++)
{
	cin>>r>>thick;
	a=sqrt((4*r*r)-(4*r)+(8*thick)+1);
	n=a-(2*r)+1;
	n=n/4;
	cout<<"Case #"<<kk<<": "<<n<<endl;
}
return 0;
}
