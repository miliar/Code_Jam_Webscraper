#include<iostream>
#include<cstdlib>
#include<iomanip>
using namespace std;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output7.in","w",stdout);
	int t;
	cin>>t;
	int al=t;
	
	while(t--)
	{
		double c,f,x;
		cin>>c>>f>>x;
		double ans1=0,ans2=0,alpha=0;
		double fac=2;
		
		ans1=x/2;

		do
		{
			ans2=ans1;
			double prev=fac;
			fac=fac+(f);
			ans1=double(c/prev)+double(x/fac)+alpha;
			alpha=alpha+double(c/prev);
			
	//		cout<<ans1<<" "<<ans2<<endl;
		
	//		system("pause");
			
		}while(ans1<=ans2);
		
		cout<<"Case #"<<al-t<<": "<<setprecision(7)<<fixed<<ans2<<endl;
	}
}
