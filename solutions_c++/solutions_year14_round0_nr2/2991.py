#include <iostream>
#include <stdio.h>
#include <iomanip>
#include <fstream>
#include <math.h>
using namespace std;
int main(){
	int t;
	double C;
	double F;
	double X;

	ifstream fin("D:/B-small-attempt0.in");
	fin>>t;
	for(int i=0;i<t;i++)
	{
		fin>>C>>F>>X;
		int k=ceil(-1+X/C-2/F);
		double s=2;
		double time=0;
		for (int j=0;j<k;j++){
			time+=C/s;
			s+=F;
		}
		time+=X/s;
		cout<<"Case #"<<i+1<<": ";
		printf("%.7f\n",time);
	}
	system("pause");
}