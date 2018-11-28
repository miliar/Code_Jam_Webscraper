/* ----Akash Agarwal---- */

#include<stdio.h>
#include<iostream>
#include<string.h>
#include<algorithm>
#include<stdlib.h>
#include<fstream>
#include<string>
#include<cmath>
#include <utility> 
#include <iomanip> 
#include <vector>
#include<stack>
#include<queue>
#include <sstream>


using namespace std;

#define LL long long int
#define iin(a) int a;cin >> a;
#define lin(a) LL a;cin >> a;
#define sin(a) string a;cin >> a;

#define myf(a,b,i) for(int i=a;i<b;i++)

#define mod 1000000007

int main()
{
	iin(t);
	for (int i = 0; i < t; ++i)
	{
		double c,f,x;
		cin >> c >> f >> x;
		double currentRate=2;
		double time=0;
		while(1)
		{
			double time_c=x/currentRate;
			double time_ex=c/currentRate;

			if (time_ex + x/(currentRate+f) < time_c )
			{
				time+=time_ex;
				currentRate+=f;
			}
			else
			{
				time+=time_c;
				break;
			}

		}
		cout.precision(15);
		cout << "Case #" << i+1 << ": " << time << endl;
	}
	return 0;
}
