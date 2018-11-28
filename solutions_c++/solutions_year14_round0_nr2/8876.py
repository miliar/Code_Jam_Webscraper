#include<iomanip>
#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<ctype.h>
#include<algorithm>
#include<cmath>
#include<cstdio>
#include<fstream>

#define min(a,b) a<b?a:b;

using namespace std;

//ifstream inx("ad.txt");
ofstream onx("o.txt");

int main()
{
	double X,F,C,r;

	int ntc
		;
	cin>>ntc;
	double seconds;
	double n;
	int cas=1;
	while(ntc--)
	{
		cin>>C>>F>>X;

		n=(X/C-2/F-1);

		int N=ceil(n);

		seconds=0;r=2;
		for(int i=0;i<N;i++)
		{
			seconds+=C/r;
			r+=F;
		}

		seconds+=X/r;

		onx<<"Case #"<<cas++<<": ";
		//fprintf(onx,"%.7f\n",seconds);
	   onx << setprecision(7) << std::fixed;
		onx<<  seconds << '\n';
	}


}