#include<stdio.h>
#include<string>
#include<math.h>
#include<errno.h>
#include<ctype.h>
#include<limits>
#include<stdlib.h>
#include<valarray>
#include<conio.h>
#include<iterator>
#include<numeric>
#include<iomanip>
#include<set>
#include<iostream>
#include<algorithm>
#include<vector>
#include <iostream>
#include <iomanip>

using namespace std;
double long A,B,C,F,X,rate,sec;
int t,c=1;

void calcA()
{
	A=sec+(X/rate);
}
void calcB()
{
	B=(sec+(C/rate))+(X/(rate+F));
}

int main(int argc,char* argv[])
{
	cin>>t;
	while(t--)
	{
		cin>>C>>F>>X;
		rate=2.0;
		sec=0.0;
		A=B=0;
		while(A>=B)
		{
			calcA();
			calcB();
			sec=sec+(C/rate);
			rate=rate+F;
		}
		cout<<"Case #"<<c<<": "<<std::setprecision(7)<<A<<endl;
		//printf("Case #%d: %.7ll\n",c,sec);
		c++;
	}
	//getch();
	return 0;
}