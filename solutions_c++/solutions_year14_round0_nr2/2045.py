#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <cstdlib>
using namespace std;

long double countTime(vector<long double>& times)	{

	long double curRate = 2.0f;
	long double target = times[2];
	long double base = 0;
	long double minTime = target/2.0f;
	long double curTime = target/2.0f;
	//int maxFactory = (int)(target/curRate);
	//cout<<"target "<<target<<" init time "<<minTime<<" maxFactory "<<maxFactory<<endl;
	//for ( int i = 1; i <= maxFactory; ++i)	{
	while (true)	{

		base += times[0]/curRate;
		curRate+= times[1];
		curTime = base + target/curRate;
		//cout<<"base "<<base<<" curRate "<<curRate<<" curTime "<<curTime<<endl;
		if (minTime - curTime > 1e-9 ) minTime = curTime;
		else break;
	}
	//}
	return minTime;
}


int main()	{

	long double N = 0;
	int testcase = 0;
	string str;
	getline(cin, str);
	stringstream(str) >> testcase;
	vector< vector<long double> > matrix(testcase, vector<long double>());
	int line = 0;
	while (getline(cin, str))
	{
		stringstream sst(str);
		
		while (sst.good())	{
			sst>>N;
			matrix[line].push_back(N);
		}
		line++;
	}
	cout.precision(7);
	cout<< std::fixed;
	for ( int i = 0; i < testcase; ++i)	{
		//if (i == 43)
		cout<<"Case #"<<i+1<<": "<<countTime(matrix[i])<<endl;;
		
	}

	return 0;
}