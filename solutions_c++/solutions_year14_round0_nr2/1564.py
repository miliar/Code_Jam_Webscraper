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
		double c,f,x;
		cin >> c >> f >> x;
		double curStatus =0;
		double t = 0;
		double p = 2;
		while (curStatus < x)
		{
			if (x - curStatus <= c)
			{
				t = (x-curStatus)/p +t;
				break;
			}
			double t1 = c /p ;
			t = t + t1;
			if ((x -curStatus) /(p+f) < (x-c-curStatus)/p)
			{
				p = p+f;
			}
			else
				curStatus += c;
		}
		cout.setf(ios::fixed);
		cout << "Case #" << i +1 << ": " << setprecision(7)<< t;
		cout << endl;
	}

	return 1;
}
