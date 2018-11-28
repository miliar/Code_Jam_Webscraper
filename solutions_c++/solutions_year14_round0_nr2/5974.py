#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for (int l=0;l<t;l++)
	{
		double c,f,x;
		cin>>c;
		cin>>f;
		cin>>x;
		
		double f1=2;
		double time=0;
		double min=(x/2),pre=0;
		int cook=0;
		while (1)
		{
//			cout<<"While Loop\n";
			time+=(c/f1);
			f1+=f;
			cook+=c;
			if (min<time)
			{
				cout<<fixed;
				cout<<"Case #"<<l+1<<": "<<setprecision(7)<<min;
				cout<<endl;
				break;
			}
			pre=time+(x/f1);
			if (min>pre)
			min=pre;
		}		
	}
}
