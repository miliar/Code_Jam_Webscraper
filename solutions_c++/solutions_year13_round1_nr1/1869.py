#include<iostream>
#include<conio.h>
using namespace std;
void main()
{
	int T;
	cin>>T;
	int r,t;
	int n,t1;
	for(int i=1;i<=T;++i)
	{
		cin>>r>>t;
		n=0;
		while(t>0)
		{
			t1=(r+1)*(r+1)-r*r;
			if(t>=t1)
				++n;
			else
				break;
			t=t-t1;
			r+=2;
		}
		cout<<"Case #"<<i<<": "<<n<<"\n";
	}
	getch();
}