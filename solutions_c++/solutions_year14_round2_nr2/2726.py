#include <iostream>
using namespace std;

int main() {
int an,i,j,t,n,a,b,k,cnt;
cin>>t;
for(i=1;i<=t;i++)
{
	cnt=0;
	cin>>a>>b>>k;
	for(j=0;j<a;j++)
		for(n=0;n<b;n++)
		{
			an=j&n;
			if(an<k)
			{
				cnt++;
			}	
		}
	cout<<"Case #"<<i<<": "<<cnt<<endl;
}
	return 0;
}
