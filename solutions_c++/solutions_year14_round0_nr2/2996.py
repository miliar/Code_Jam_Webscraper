#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
	int t,i;
	double o[100],tm,a,tt,c,f,x,t1,t2;
	
	cin>>t;
	for(i=0;i<t;i++)
	{
		tm=2.0000000;
		a=0.0000000;
		tt=0.0000000;
		t1=0.0000000;
		cin>>c>>f>>x;
		a=x/tm;
		tt=a;
		
		
		t2=(c/tm);
		tm=tm+f;
		t1=t2+(x/tm);
		while(tt>t1)
		{
			tt=t1;
			t2=(c/tm)+t2;
			tm=tm+f;
			t1=t2+(x/tm);
			
			
		}
		o[i]=tt;
		
		
	}
	for(i=0;i<t;i++)
	cout<<"Case #"<<(i+1)<<": "<<setprecision(7)<<fixed<< o[i]<<endl;
}
