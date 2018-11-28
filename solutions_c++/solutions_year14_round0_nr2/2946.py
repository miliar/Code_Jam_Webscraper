#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

//¾«¶È²»¹»

int main()
{
	ifstream is;
	ofstream os;
	os.precision(15);
	is.open("F:\\B-large.in");
	os.open("F:\\B-large.out");
	//is.open("F:\\test.txt");
	//os.open("F:\\test.out");
	int t;
	is>>t;
	for(int ca=1;ca<=t;ca++)
	{
		double c,f,x;
		is>>c>>f>>x;
		double k=(f*x-2*c-f*c)/c/f;
		int round=(int)floor(k);
		double time=0.000000000;
		double effi=2.000000000;
		for(int i=0;i<=round;i++)
		{
			time+=c/effi;
			effi+=f;
		}
		time+=x/effi;
		os<<"Case #"<<ca<<": ";
		os<<time;
		os<<endl;
	}
	is.close();
	os.close();
	return 0;
}