#include <iostream>
#include <cstdio>
#include <iomanip>
#include <cmath>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <fstream>
using namespace std;

int main()
{

	long long tc;
    string s;
ifstream infile;
ofstream outfile;
infile.open ("input.in");
outfile.open("output.txt");
getline(infile,s);
	 tc=stoi(s);
	for(long long i=1;i<=tc;i++)
	{
		 double c,f,x,rate=2.0;
		 getline(infile,s);
		 stringstream ss(s);
		 ss >> c >> f>> x;
		 double ans=0.0;
		 while(true)
		 {
			 while(c/rate + x/(rate+f) < (x)/rate)
			 {
				ans+=c/rate;
				rate+=f;
			 }
			 ans+=x/rate;
			 break;

		 }
		outfile<<"Case #"<<i<<": "<<setprecision(7)<<fixed<<ans<<endl;
	}
	infile.close();
	outfile.close();
	return 0;
}
