
#include<iostream>
#include<fstream>
#include<stdio.h>
#include<vector>
#include<time.h>
using namespace std;

double CacuMinTime(double buyFarmc,double extentNumberf,double endofgamex)
{
	/*1 = C = 500.
      1 = F = 4.
      1 = X = 2000.*/
	const double startCookies = 0;
	const double producingCookies =2;
	double result=endofgamex/producingCookies;

	
	//if buyfarm large, do not need buy farm
	if(buyFarmc>=endofgamex)
		return endofgamex/producingCookies;
	
	//may be need buy farm
	//result is min(sum(c/(2+fy)+x/(2+fy)));
	//assume y is 1000
	double sum = 0;
	double sumofBuyFarm =0;
	for(int i=1;i<1000000;i++)
	{
	
		sumofBuyFarm+=buyFarmc/(2+extentNumberf*(i-1));

		sum=endofgamex/(producingCookies+extentNumberf*i)+sumofBuyFarm;
		if(sum<result)
			result=sum;
	}

	return result;
}
int main()
{
	int start=clock();
 
	fstream input;
	input.open("B-large.in");
    ofstream out("b-large.txt"); 
	
	int n;//number of test case n
	input>>n;

	for(int i=0;i<n;i++)
	{
	
		double buyFarmc=0.0;
		double extentNumberf=0.0;
		double endofgamex=0.0;
	
		input>>buyFarmc;
		input>>extentNumberf;
		input>>endofgamex;
		double minTime=CacuMinTime(buyFarmc,extentNumberf,endofgamex);

	    char szBufffer[255];
		sprintf(szBufffer, "%10.7f", minTime);
		out<<"Case #"<<i+1<<": "<<szBufffer<<endl;
	
	

	}
	input.close();
	out.close();
    int end=clock();
	cout<<"the total time of running is :"<<end-start<<endl;
	return 0;
}