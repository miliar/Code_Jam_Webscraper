#include "stdafx.h"
#include<stdio.h>
#include<string>
#include<conio.h>
#include<iomanip>
#include <iostream>
#include <iomanip>

using namespace std;
double long value1,value2,C,F,X,rt,sec;
double test,cas=1;
int main(int argc,char* argv[])
{
	cin>>test;
	while(test--)
	{
		cin>>C>>F>>X;
		rt=2.0;
		sec=0.0;
		value1=value2=0;
		while(value2>=value1)
		{
			value1=(sec+(C/rt))+(X/(rt+F));
			value2=sec+(X/rt);
			sec=sec+(C/rt);
			rt=rt+F;
		}
		cout<<"Case #"<<cas<<": "<<std::setprecision(7)<<value2<<endl;
		cas++;
	}
	//getch();
	return 0;
}
