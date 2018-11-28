#include <iostream>
#include <iomanip>

using namespace std;

main()
{
	double test,d,c,f,x,t,i;
	cin>>test;
	
	i=0;
	while(test>i)
	{
		cin>>c;
		cin>>f;
		cin>>x;
		t=0;
		d=2;
		while(1)
		{
			if(x/d>((c/d)+(x/(d+f))))
			{
				t+=(c/d);
				d+=f;
			}
			else
			{
				t+=(x/d);
				break;
			}
		}
		i++;
		cout<<"Case #"<<i<<": " ;
		cout<<setprecision(8)<<t<<endl;
		
	}
}
