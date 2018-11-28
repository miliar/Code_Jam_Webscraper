#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	int T;
	cin>>T;
	for(int t=0;t<T;t++)
	{
		double C,F,X;
		cin>>C>>F>>X;
		double rate=2;
		double total_time=0;
		bool p=true;
		while(p)
		{
			double ftime=C/rate ;
			double nptime= X/(rate+F);
			double ptime=X/rate;
			//cout<<ftime<<"  "<<nptime<<"  "<<ptime<<endl;
			if(ftime+nptime<ptime)
			{
				total_time+=ftime;
				rate+=F;
			} 
			else
			{
				total_time+=ptime;
				p=false;
			}	

		}
		printf("Case #%d: %.7lf\n", t+1, total_time);
	}
	return 0;		

}