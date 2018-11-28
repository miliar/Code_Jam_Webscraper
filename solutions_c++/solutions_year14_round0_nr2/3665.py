#if 1
#pragma comment(linker, "/STACK:66777216")
#include <math.h>
#include <iostream>
#include <deque>
#include <set>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <string>
#include <ctime>
#include <vector>
#include <iomanip>
using namespace std;
typedef long double LD; 
typedef long long LL; 

#define PROBLEM "B-large"
double c,f,x;
double click(double add)
{
	double r=x/add;
	double cl=c/add;

	if(r<cl+x/(add+f))
		return r;
	cl+=click(add+f);
	return min(r,cl);
}
int main()
{
    freopen(PROBLEM ".in","r",stdin); freopen(PROBLEM ".out","w",stdout);
    //freopen("input.txt","r",stdin); //freopen("output.txt","w",stdout);
    time_t START = clock(); 
    
	int t;
	cin>>t;
	cout<<fixed<<setprecision(10);
	cout.sync_with_stdio();
	for(int i=1; i<=t; i++)
	{
		cin>>c>>f>>x;
		cout<<"Case #"<<i<<": "<<click(2)<<endl;
	}

    time_t FINISH = clock(); 
    cerr << "Time = " << double(FINISH - START) / CLOCKS_PER_SEC << endl;
    return 0;
}
#endif