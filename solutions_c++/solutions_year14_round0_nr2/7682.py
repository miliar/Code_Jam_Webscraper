#include<iostream>
#include<cmath>
#include<fstream>
#include<iomanip>
using namespace std;
int main(int argc, char const *argv[])
{
	int T;
	double C,F,X,f,a,b,c,d,res,t;
	ifstream ifs("B-small-attempt0.txt");
	ofstream ofs("output.txt");
	ifs>>T;
//	cin>>T;
	for(int I=1;I<=T;I++)
	{
		ifs>>C>>F>>X;
//		cin>>C>>F>>X;
		res=X;
		a=X/2;
		f=0;
		t=0;
		while(a<res)
		{
			res=a;
			t+=(C/(2+f*F));
			f++;
			a=t+(X/(2+f*F));
		}
//		cout<<fixed;
//		cout<<setprecision(7);
//		cout<<res<<"\n";
		ofs<<fixed;
		ofs<<setprecision(7);
		ofs<<"Case #"<<I<<": "<<res<<"\n";
	}



	return 0;
}