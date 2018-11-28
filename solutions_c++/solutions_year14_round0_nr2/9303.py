#include<iostream>
#include<iomanip>
#include<stdio.h>
#include<fstream>
using namespace std;
int main()
{
	ifstream fin;
	fin.open("B-large.in",ios::in);
	FILE *ptr;
	ptr=fopen("output.txt","w");
	int t;
	double c,f,x;
	fin>>t;
	int i=1;
	while(t--)
	{
		double rate=2;
		double additional=0;
		double time=0;
		fin>>c>>f>>x;
		double prevtim=x;
		while(1)
		{
			time=(x/rate)+additional;
			if(prevtim>time)
			{
				prevtim=time;
				additional+=(c/rate);
				rate+=f;				
			}
			else
				break;
			//cout<<"time"<<prevtim<<setprecision(10)<<endl;
			//cout<<"additional"<<additional<<endl;
		}
		fprintf(ptr,"Case #%d: %0.7f\n",i,prevtim);
		i++;
	}
	return 0;
}
