#include<iostream>
#include<cstdio>
#include<iomanip>
#include<fstream>

using namespace std;

int main()
{
	double time = 0;
	double pert = 2,c,f,x;
	ifstream fin("B-large.in");
	ofstream fout("cookieout1.txt");
	int i, t;
	
	fin.seekg(0);
	
	fin >> t;
	
	for(i = 1; i <= t; i++) {
		time=0;
		pert=2;
		
		fin >> c;
		fin >> f;
		fin >> x;
		
		while(x/pert > (c/pert+x/(pert+f))) {
			
			time = time + c/pert;
			pert = pert + f;
		}
		time = time + x/pert;
		fout<<"Case #"<<i<<": ";
		fout<<fixed;
		fout<<setprecision(7)<<time<<"\n";
		
		
	}
	
	//fout<<"Case #"<<i<<": "<<time<<"\n";
	return 0;
	
	
}


