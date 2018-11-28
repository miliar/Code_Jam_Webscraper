#include <fstream>
#include <math.h>
#include <stdio.h>
#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <algorithm>
#include <limits.h>
#include <stdlib.h> 
#include <set>
#include <queue>
using namespace std;
#pragma comment(linker, "/STACK:999999999")
#define ll long long
const long long MAXN = 102;
const long double eps=0.00000000001;




int main()
{
	ifstream cin("input.txt");
	ofstream cout("output1.txt");
	int t;
	cin>>t;
	for (int q=0;q<t;q++)
	{
		long double c,f,x;
		cin>>c>>f>>x;
		long double r=x/2;
		long double e=2;
		long double time=c/2;
		while (time<r)
		{
			e+=f;
			r=min(r,time+(x/e));
			time+=c/e;
		}
		cout<<"Case #"<<q+1<<": "<<std::fixed  << std::setprecision(7) << r<<endl;
	}
					
	return 0;
}