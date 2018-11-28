#include <iostream>
#include <stdio.h>
#include <string.h>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <math.h>
#include <utility>
#include <sstream>
#include <queue>
#include <stack>
#include <iomanip>
#include <ctime>
#include <limits.h>
#include <bitset>
#include <functional>
#include <numeric>
#include <complex>
#include <fstream>
#define DELIM   '\0'

using namespace std;

int main()
{
	ifstream read ("B-Large.in");
	int t;
	read>>t;
	ofstream myfile;
    myfile.open ("output.txt");
    cout<<fixed;
    myfile<<fixed;
    cout.precision(7);
    myfile.precision(26);
	for(int j=1;j<=t;j++)
	{
	 double c,f,x,cost=0.0;
	 read>>c>>f>>x;
    //cout<<x<<endl;
	double s=2.0;
	while((double)x/s > ((double)c/s+(double)x/(s+f)))
	{
	    cost+=(double)c/s;
		s+=f;
       //cout<<cost<<endl;
	}
	cost+=(double)x/s;
	myfile<<"Case #"<<j<<": "<<std::setprecision(7)<<cost<<endl;

	 }


}
