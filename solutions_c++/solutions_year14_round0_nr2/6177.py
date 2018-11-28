#include <iostream>
#include <iomanip>
using namespace std;
double c,f,x;
double res,currf;
int main(int argc, char const *argv[])
{
	int t,casenum;
	cin>>t;
	for(casenum=1;casenum<=t;casenum++){
		cin>>c>>f>>x;
		res = 0;
		currf = 2;
		while(x/currf > (x/(currf+f) + c/currf)){
			res += c/currf;
			currf += f;
		}
		res += x/currf;
		cout<<"Case #"<<casenum<<": "<<fixed<<setprecision(7)<<res<<endl;
	}
	return 0;
}