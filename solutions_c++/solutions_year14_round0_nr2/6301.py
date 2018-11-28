#include<iostream>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		double c,f,x,cpc=2;
		cin>>c>>f>>x;
		double time=0,least_time=x/cpc;
		while(1)
		{
			time += c/cpc;
			cpc += f;
			if( time + x/cpc < least_time )
				least_time = time + x/cpc;
			else
				break; 
		}
		cout.precision(7);
		cout<<"Case #"<<i<<": "<<fixed<<least_time<<"\n";
	}
	return 0;
}
