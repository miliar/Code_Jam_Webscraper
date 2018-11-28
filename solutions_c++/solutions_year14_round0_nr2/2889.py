#include<iostream>
#include<fstream>
#include<algorithm>
#include<set>
#include <iomanip>
using namespace std;
int main()
{
	int T;
	ifstream fin ("/home/kidd/B-large.in", ios::in);
	ofstream fout ("/home/kidd/B-large.out", ios::out);
	fin>>T;
	for(int it=1;it<=T;it++)
	{
		double C,F,X;
		double ret=0;
		double p=2,o=0;
		fin>>C>>F>>X;
		while(true)
		{
			double c1=(X-o)/p;
			double c2=(C-o)/p;
			if(c1<=c2)
			{
				ret+=c1;
				break;
			}
			else
			{
				double c3=c2+X/(p+F);
				if(c3<c1)
				{
					p+=F;
					ret+=c2;
					o=0;
				}
				else
				{
					ret+=c1;
					break;
				}
			}
		}
		fout.setf(ios::fixed);
		fout<<"Case #"<<it<<": ";
		fout<<setprecision(7)<<ret<<endl;
	}
}
