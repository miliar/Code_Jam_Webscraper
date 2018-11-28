#include<iostream.h>
#include<fstream.h>
#include<stdio.h>
void main()
{
	int t,z;
	char s[38];
	ifstream fin("C:\\TC\\BIN\\VijitD\\GcodeJam\\i2.txt");
	ofstream fout("C:\\TC\\BIN\\VijitD\\GcodeJam\\outB.txt");
	fin>>t;
	fin.get();
	z=t;
while(t--)
{
	int k=0;
	double C,F,X,r=2,t2,t1;
	fin.getline(s,38,'\n');
	sscanf(s,"%lf %lf %lf",&C,&F,&X);
	t1=t2=X/r;
	while(t2<=t1)
	{
		t1=t2;
		t2=0;
		r=2;
		for(int i=0;i<=k;i++)
		{
			t2+=C/r;
			r+=F;
		}
		t2+=X/r;
		if(t2<=t1)
		++k;
	}
	fout.precision(7);
	fout<<"Case #"<<(z-t)<<": "<<t1<<endl;
}
}