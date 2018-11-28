#include <iostream>

using namespace std;


int main()
{
	double dC, dF, dX;
	int iCase;
	cin>>iCase;
	string *s = new string[iCase];
	char ch[100];
	for(int i=0;i<iCase;++i){
		double dTime=0;
		double dRate=2;
		cin>>dC>>dF>>dX;
		if (dC > dX){
			dTime=dX/dRate;
			sprintf(ch, "Case #%d: %.6lf\n", i+1, dTime);
		}else{
			while(dX/(dRate+dF) < (dX-dC)/dRate){
				dTime += dC/dRate;
				dRate += dF;
			}
			dTime += dX/dRate;
			sprintf(ch, "Case #%d: %.6lf\n", i+1, dTime);
		}
		s[i]=ch;
	}
	for(int i=0;i<iCase;++i){
		cout<<s[i].c_str();
	}
	return 0;
}