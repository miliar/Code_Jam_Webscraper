#include<fstream>
#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
	ifstream fin("in.txt");
	ofstream fout("out.txt");
	double c,f,x,cr,nr,t,t1,t2,t3;
	int test,i,finish;
	fin>>test;
	for(i=1;i<=test;i++)
	{
		fin>>c>>f>>x;
		t=0;
		finish=0;
		cr=2.0;
		while(!finish)
		{
			nr=cr+f;
			t1=c/cr;
			t2=x/nr;
			t3=x/cr;
			if((t1+t2)<t3)
			{
				cr=nr;
				t=t+t1;
			}
			else
			{
				t=t+t3;
				finish=1;
			}
		}
		fout<<"Case #"<<i<<": ";
		fout.setf(ios::fixed);
		fout<<setprecision(7)<<t<<"\n";
	}
}