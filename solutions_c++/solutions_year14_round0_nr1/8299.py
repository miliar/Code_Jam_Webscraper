#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <string>
#include <cstring>

using namespace std;

int main()
{
	int t;
	cin >> t;
	for(int ti = 1;ti <= t;ti++)
	{
		int a[4][4];
		int b[4][4];
		int ac,bc;
		cin >> ac;
		ac--;
		for(int i = 0;i < 4;i++)
		{
			for(int j = 0;j < 4;j++)
			{
				cin >> a[i][j];
			}
		}
		cin >> bc;
		bc--;
		for(int i = 0;i < 4;i++)
		{
			for(int j = 0;j < 4;j++)
			{
				cin >> b[i][j];
			}
		}
		// get the values
		vector<int> res;
		for(int i = 0;i < 4;i++)
		{
			for(int j = 0;j < 4;j++)
			{
				if(a[ac][i] == b[bc][j])
				{
					res.push_back(a[ac][i]);
				}
			}
		}
		/*
		Case #1: 7
		Case #2: Bad magician!
		Case #3: Volunteer cheated!
		*/
		if(res.size() == 1)
		{
			printf("Case #%d: %d\n",ti,res[0]);
		}
		else if(res.size() == 0)
		{
			printf("Case #%d: Volunteer cheated!\n",ti);
		}
		else
		{
			printf("Case #%d: Bad magician!\n",ti);
		}
	}
	return 0;
}