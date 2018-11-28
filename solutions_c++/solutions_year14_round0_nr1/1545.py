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
		int r1,r2;
		cin >> r1;
		int r[4];
		int j = 0;
		while ( j != r1-1)
		{
			cin.getline(buf,1000);
			if (strlen(buf) == 0)
				continue;
			j ++;
		}
		cin >> r[0] >> r[1] >> r[2] >> r[3];
		j ++;
		while ( j < 4)
		{
			cin.getline(buf,1000);
			if (strlen(buf) == 0)
				continue;
			j ++;
		}
		cin >> r2;
		int a[4];
		j = 0;
		while ( j != r2-1)
		{
			cin.getline(buf,1000);
			if (strlen(buf) == 0)
				continue;
			j ++;
		}
		cin >> a[0] >> a[1] >> a[2] >> a[3];
		j ++;
		while ( j < 4)
		{
			cin.getline(buf,1000);
			if (strlen(buf) == 0)
				continue;
			j ++;
		}
		int num = 0;
		vector<int> s;
		for ( j = 0; j < 4; j ++)
			for (int k = 0; k < 4; k ++)
				if (a[j] == r[k])
				{
					num ++;
					s.push_back(a[j]);
				}
		if (num == 0)
			cout << "Case #" << i +1 << ": " << "Volunteer cheated!";
		else if (num > 1)
			cout << "Case #" << i +1 << ": " << "Bad magician!";
		else
			cout << "Case #" << i +1 << ": " << s[0];
		cout << endl;
	
	}

	return 1;
}
