#include <iostream>
#include <cstdio>
using namespace std;
int main()
{
	int test;
	cin>>test;
	int i;
	for(i=0;i<test;i++)
	{
		double c,f,x;
		cin>>c>>f>>x;
		cout<<"Case #"<<i+1<<": ";
		if(c>x)
		{
			printf("%.7lf\n",x/2);
			//cout<<x/2<<endl;
		}
		else
		{
			double cutoff=0.0;
			double rate=2.0;
			double tme=55500.0;
			double temp;
			while(1){
				temp=cutoff+x/rate;
				//printf("%.7lf\t",temp);			
				//cout<<temp<<"\t";
				if(temp<tme)
					tme=temp;
				if(temp>tme)
					break;
				cutoff+=c/rate;
				rate+=f;
			}
			printf("%.7lf\n",tme);			
//			cout<<tme<<endl;
		}
	}
}