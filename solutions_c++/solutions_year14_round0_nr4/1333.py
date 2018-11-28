// test1.cpp : 定义控制台应用程序的入口点。
//

//#include "stdafx.h"
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <sstream>
#include <iterator>

using namespace std;
vector<string> splitStr(string line)
{
	istringstream iss(line);
		vector<string> tokens;
		copy(istream_iterator<string>(iss),
         istream_iterator<string>(),
		  back_inserter<vector<string> >(tokens));
	return tokens;
}
int main(int argc, char * argv[])
{
	freopen(argv[1],"r",stdin);
	freopen(argv[2],"w",stdout);
	int nCaseNum;
	cin >> nCaseNum;
	char buf[1000];
	for (int i = 0; i < nCaseNum; i ++)
	{
		int size;
		cin >> size;
		vector<double> n(size,0);
		vector<double> k(size,0);
		for ( int i = 0; i < size; i ++)
			cin >> n[i];
		for (int i=0; i < size; i ++)
			cin >> k[i];
		sort(n.begin(), n.end());
		sort(k.begin(),k.end());
		int dscore, score;
		dscore =  score = 0;
		vector<double> tmp = k;
		for ( int i = size -1; i >= 0; i --)
		{
			double t = n[i];
			for ( int j = size -1; j >=0; j --)
			{
				if (t > tmp[j])
				{
					tmp[j] = 1;
					dscore ++;
					break;
				}
			}
		}
		tmp = n;
		for ( int i = size -1; i >= 0; i --)
		{
			double t = k[i];
			for ( int j = size -1; j >=0; j --)
			{
				if (t > tmp[j])
				{
					tmp[j] = 1;
					score ++;
					break;
				}
			}
		}

		//cout.setf(ios::fixed);
		cout << "Case #" << i +1 << ": " << dscore << " " << size -score;
		cout << endl;
	}

	return 1;
}
