#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <fstream>
#include <boost/regex.hpp>

using namespace std;

typedef vector<string>::iterator vst;
typedef vector<int>::iterator vit;

int main(int argc, char** argv)
{
	if(argc<2)
		exit(0);

	//file input
	ifstream in;
	in.open(argv[1]);

	vector< vector<int> > v;

	int N = 0;
	in >> N;
	for(int _i=0; _i<N; _i++)
	{
		cout << "Case #" << _i+1 << ": ";
		//cout << endl;

		long long r,t,ringCount=0,sum=0;
		in >> r >> t;

		//double t_overPi = t/M_PI, sum=0;
		//cout << "t: " << t << "\tt_overPi: " << t_overPi << endl;

		while(sum < t)
		{
			sum += (2*(r+1)-1);
			//cout << "r: " << r+1 << "\tsum: " << sum << endl;
			r += 2;
			if(sum<=t)
				ringCount++;
		}

		cout << ringCount << endl;
	}

	//cout << "Hello!" << endl;
	in.close();
	return 0;
}

