#include <iostream>
#include <fstream>
using namespace std;

int main(void)
{
	ifstream fin;
	fin.open("B-large.in");
	ofstream fout;
	fout.open("B-large.out");
	int t;
	fin>>t;
	double c,f,x;
	double t1,t2;
	
	for(int i=0;i<t;i++)
	{
		//cin
		fin>>c>>f>>x;
		double tr=0;
		int m=0;

		while(true)
		{
			double t1=x/(2+(m+1)*f)+c/(2+m*f);
			double t2=x/(2+m*f);
			if(t1<t2) 
			{
				tr=tr+c/(2+m*f);
				m++;
			}
			else
			{
				tr=tr+t2;
				break;
			}
		}
		fout<<"Case #"<<i+1<<": ";
		fout.setf(ios::fixed);
		fout.precision(7);
		//fout<<setiosflags(ios::fixed); 
		fout<<tr<<endl;
	}
	return 0;
}