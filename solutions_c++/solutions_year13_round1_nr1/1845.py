#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

typedef struct longInt
{
	int digit[100];
	int length;
}longInt;


int main(void)
{
	ifstream ifs;
	ofstream ofs;
	ifs.open("A-small-attempt0.in",ios_base::in);
	ofs.open("A-small-attempt0.out",ios_base::trunc);
	int T;
	double t,r;
	ifs>>T;
	for(int i=0;i<T;i++)
	{
		ifs>>r>>t;
		double need=(r+1)*(r+1)-r*r;
		int count=0;
		while(need<=t)
		{
			count++;
			r+=2;
			t-=need;
			need=(r+1)*(r+1)-r*r;
		}
		ofs<<"Case #"<<i+1<<": "<<count<<endl;
	}

	return 0;
}