#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
#include <fstream>   
using namespace std;

int doit(vector<int> v)
{
	int res = 1000;
	
	for (int i = 1; i <= 1000; i++)
	{
		int r = 0;
		for (int j = 0; j < v.size(); j++)
		{
			r += (v[j] + i - 1) / i - 1;
		}
		res = min(res, r + i);
	}

	return res;

}

int main(void)
{
	freopen("d:\\output.txt", "w", stdout);
	freopen("d:\\input.txt", "r", stdin);

	int T;
	cin >> T;
	int D;
	int P;
	
	for (int i = 0; i < T; i++)
	{
		cin >> D;

		vector<int> v;
		for (int j = 0; j < D; j++)
		{
			cin >> P;
			v.push_back(P);
		}

		cout << "Case #"<<i+1<<": " << doit(v) << endl;
	}
}