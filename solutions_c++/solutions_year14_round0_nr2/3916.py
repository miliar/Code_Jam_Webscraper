#include<iostream>
#include<stdlib.h>
using namespace std;
int main()
{
	freopen("C:\\Users\\Tarun\\Desktop\\ip.txt","r",stdin);
	freopen("C:\\Users\\Tarun\\Desktop\\op.txt","w",stdout);
	int i,j,t,k;
	double c,f,x,a,b;
	cin>>t;
	for(k=1;k<=t;k++)
	{
		a=2.0;b=0.0;
		cout<<"Case #"<<k<<": ";
		cin>>c>>f>>x;
		while(1)
		{
			if(x/a<=(x/(f+a)+c/a))
			{
				b=b+x/a;
				break;
			}
			b=b+(c/a);
			a=a+f;
		}
		printf("%.7f\n",b);
	}
	return 0;
}