#include <iostream>
using namespace std;

int main() {
	int t;
	int ms,a,c,i,j,x=0;
	char b;
	cin>>t;
	while(t--)
	{
		ms=0,j=0;
		cin>>a;
		for(i=0;i<=a;i++)
		{
			cin>>b;
			c=(b-'0');
			if(i!=0)
			{
				if(i-ms>0)
				{
					j=j+(i-ms);
					ms+=(i-ms);
				}
			}
				ms+=c;
		}
		x++;
		cout<<"Case #"<<x<<": "<<j<<'\n';
	}
	return 0;
}
