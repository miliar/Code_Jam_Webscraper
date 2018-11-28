#include <iostream>
#include<iomanip>
typedef unsigned long long int llui;
using namespace std;

int main() {
	int T,noc,i,j,k,l;
	long double C=0.0,F=0.0,X=0.0,NF=2.0,NT=0.0,t1=0.0,t2=0.0,diff=0.0;
	cin>>T;
	for(noc=1;noc<=T;noc++)
	{
		cin>>C;
		cin>>F;
		cin>>X;
		NT=0.0;
		NF=2.0;
		while(true)
		{
			t1=X/NF;
			t2=(C/NF)+(X/(NF+F));
			diff=(t1-t2);// 
			if(diff>0)//means t1 takes more time and its better to get C
			{
				NT+=(C/NF);
				NF+=F;
			}
			else
			{
			  NT+=(X/NF);
			  break;
			}
		}
		cout<<"Case #"<<setprecision(10)<<noc<<":"<<" "<<NT<<endl;
	}
	return 0;
}