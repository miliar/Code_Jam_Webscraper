#include<bits/stdc++.h>
using namespace std;
int main()
{
	int test;
	cin>>test;
	for(int  t=1;t<=test ;t++ )
	{
		double c,f,x;
		cin>>c>>f>>x;
		double tt=0 , pcr=2.0 ;
		
		while( 	(x-c) /pcr > x/(pcr+f) )
		{
			tt += c/pcr;
			pcr+=f;
		}
		tt+= x/pcr;
		cout<< fixed << setprecision(7);
		cout<< "Case #"<<t<<": "<<tt<<endl;
		
	}
	return 0;
}

