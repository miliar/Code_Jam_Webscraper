#include<iostream>
#include<fstream>

using namespace std;

ofstream write("output1.txt");
void farm(long double c,long double r,long double x,long double f,long double T,long double tr,int i)
{
	
	long double t,t1,t2;
		t1=c/r;
		tr+=t1;
		r+=f;
		t2=x/r;
		t=t2+tr;
	if(T<t)
		{

			write<<"Case #"<<i+1<<": "<<T<<"\n";
		}
	else
		farm(c,r,x,f,t,tr,i);
}
void main()
{
	write.precision(8);
	long double C,F,X;float test=0;
	long double rate=2;
	long double t1,t2=0;
	ifstream read("B-small-attempt3.in");
	read.precision(8);
	read>>test;
	for(int i=0;i<test;i++)
	{
		read>>C;
		read>>F;
		read>>X;
		t1=X/rate;
		farm(C,rate,X,F,t1,t2,i);
	}
}