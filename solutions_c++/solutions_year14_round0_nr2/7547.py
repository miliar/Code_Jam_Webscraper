#include<iostream>
#include<iomanip>
using namespace std;

int main(){
	int testcases;
	double c=0.0;
	double f=0.0;
	double x=0.0;
	double tot_sec=0.0;
	double tot_sec2=0.0;
	double delta=2.0;
	double C=0.0;

	cin>>testcases;
	
	for(int kcounter=1;kcounter<=testcases;kcounter++)
	{

		cin>>c;
		cin>>f;
		cin>>x;
		tot_sec=0;
		tot_sec2=0;
		delta=2.0;
		C=0.0;
		tot_sec=x/delta;
		if((c/delta)<tot_sec)
		{
			C=c/delta;	
			while(1){
				tot_sec2=C+x/(delta+f);
				if(tot_sec2<tot_sec){
					tot_sec=tot_sec2;
					delta+=f;
					C+=c/delta;
				}
				else
					break;
			}
		}
		cout<<setprecision(7)<<fixed;
		cout<<"Case #"<<kcounter<<": "<<tot_sec<<endl;
	}
	return 0;
}
