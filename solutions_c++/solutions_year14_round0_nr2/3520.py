
#include<iostream>
using namespace std;
int main()
{
	int t,count=0,cnum=1;
	cin>>t;
	while(t!=0)
	{
		double Crate=2,Freq,Frate,X,Time=0;
		cin>>Frate;
		cin>>Freq;
		cin>>X;
		Time=X/Crate;
		while(Frate/Crate+X/(Crate+Freq)<X/Crate)
		{
			if(count==0&&Time>Frate/Crate)
			Time=0;
			Time=Time+Frate/Crate;
			Crate=Crate+Freq;
			count++;
		}
		if(count>0)
			Time+=X/Crate;
		cout<<"Case #"<<cnum<<": ";
		printf("%.7lf\n",Time);
		
		t--;
		cnum++;
		count=0;
	}
}
