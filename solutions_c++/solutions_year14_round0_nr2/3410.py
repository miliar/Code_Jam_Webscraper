#include<iostream>
#include<conio.h>
#include<fstream>
#include<iomanip>
using namespace std;

int main()
{
	ifstream fin("B-small-attempt0.in");
	ofstream fout("output.txt");
	
	int T;
	double c,f,x,t,t1,t2,r;
	fin>>T;
	
	for(int k=0;k<T;++k)
	{
		fin>>c;
		fin>>f;
		fin>>x;
		t=0.000000;
		t1=0.000000;
		t2=0.000000;
		r=2.000000;
		
		while(1)
		{
			t1=x/r;
			t2=c/r+x/(r+f);
			
			if(t2<t1)
			{
				t+=c/r;
				r+=f;
			}
			else
			{
				t+=x/r;
				break;
			}
		}		
		fout<<"Case #"<<k+1<<": "<<fixed<<setprecision(7)<<t<<endl;
	}
	return 0;
}