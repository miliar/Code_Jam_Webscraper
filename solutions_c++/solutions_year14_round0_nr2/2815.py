#include<iostream>
#include<stdio.h>
#include<conio.h>
using namespace std;
int main()
{
		unsigned int T =0,i;
		double C,F,X;
		double prevResult, result;
		double curRate;
		double addTime = 0;
		
		cin >> T;
		for(i=1 ; i <=T;i++)
		{
			curRate = 2.0;
			addTime = 0;
			cin >> C >> F >> X;
			result = prevResult = X / curRate;
			do
			{
				prevResult = result;
				addTime += C / curRate;
				curRate+=F;
				result = X / curRate + addTime;
				
				//cout << prevResult <<"-->"<<result<<endl;
				
				}while(result < prevResult);
			cout.precision(10);
			cout<<"Case #"<<i<<": "<<prevResult<<endl;
			}
	return 0;
}


