#include<iostream>
using namespace std;

int main()
{    int tc,i,y,x;
	cin>>tc;
	for(x=1;x<=tc;x++)
	{	int smax,n=0,a=0;
		cin>>smax;
		char s[smax];
		for(i=0;i<=smax;++i)
			cin>>s[i];
		for(y=0;y<=smax;y++)
		{	if(y<=n)
			{	n=n+(int)s[y]-48;
			}
			else
			{	a=a+(y-n);
				n=y+((int)s[y]-48);
			}		
		}
		cout<<"Case #"<<x<<": "<<a<<"\n";	
	}
	return 0;
}
