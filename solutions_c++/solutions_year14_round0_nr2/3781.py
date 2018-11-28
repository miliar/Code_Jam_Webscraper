#include <fstream>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <algorithm>
#include <math.h>
#include <iomanip>
using namespace std;

int main()
{
	ifstream curFile("B-large.in");
	vector<double> result;
	int T; // testcases count
	double C;
	double F;
	double X;
	double MAGIC = 2.0;
	double rate;
	if(curFile.is_open())
	{
		curFile >> T;
		for(int c = 0 ; c < T ; c++)
		{
			curFile >> C;
			curFile >> F;
			curFile >> X;
			rate = MAGIC;
			double ret = 0;
			double finish;
			double buytime;
			double nextfinish;
			double nextrate;
			while(true)
			{	
				finish = X/rate;
				buytime = C/rate;
				nextrate = rate + F;
				nextfinish = X/nextrate;					
				if(finish < buytime + nextfinish)
				{
					ret += finish;
					result.push_back(ret);
					break;	
				}
				ret += buytime;
				rate = nextrate;
			}	
		}	
	}
	curFile.close();
	ofstream outfile;
	outfile.open("result.txt");
	outfile << std :: fixed;
	if(outfile.is_open())
	{
		for(int i = 0; i < result.size() ; i++)
			outfile << "Case #" << i + 1<< ": " <<std::setprecision(7) << result[i] << endl;
	}
	outfile.close();
	return 0;
}
