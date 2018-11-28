#include <iostream>
#include <iomanip>
using namespace std;


int main ()
{
	int T,noOfTitaration,i;
	double cockies,target1,target2,rate,currentRate,C;
	cin>>T;

	for(int itr=1;itr<=T;itr++)
	{	
		cin>>C;
		cin>>rate;
		cin>>cockies;

		currentRate=2.0;
		noOfTitaration=1;
		target1=cockies/currentRate;
		target2=0;

		while (target1>target2)
		{
			if(target2!=0)
				target1=target2;
			target2=0;
			currentRate=2;
			for(i=0;i<noOfTitaration;i++)
			{
				target2=target2+C/currentRate;
				currentRate=currentRate+rate;
			}
			noOfTitaration++;
			target2=target2+cockies/currentRate;
		}


	
		cout<<"Case #"<<itr<<": "<< setiosflags(ios::fixed | ios::showpoint)
        << setprecision(7)<<target1<<endl;
	
	}
	return 0;
}