#include<iostream>
#include<cstdio>
#include<cmath>
#include<fstream>
using namespace std;
int main()
{
	ifstream fin("a.txt");
	ofstream fout("b.in");
	int t,k;
	double c,f,rate,x,seconds,s1,s2;
	fin>>t;
	for(k=1;k<=t;k++)
	{
		fin>>c>>f>>x;
		//fout<<c<<' '<<f<<' '<<x<<endl;
		seconds=0.0;
		rate=2.0;
		while(1)
		{
			s1=x/rate;
			s2=c/rate+x/(rate+f);
			//fout<<"seconds: "<<seconds<<" s1: "<<s1<<" s2: "<<s2<<endl;
			if(s1>s2)
			{
				seconds+=(c/rate);
				rate+=f;
				continue;
			}
			else
			{
				seconds+=s1;
				break;
			}
		}
		fout.precision(15);
		fout<<"Case #"<<k<<": "<<seconds<<endl;
	}
}
