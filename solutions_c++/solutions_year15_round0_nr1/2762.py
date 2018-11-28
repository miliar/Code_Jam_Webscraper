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

int doit(string p)
{
	int res = 0;
	int cur = 0;
	for (int i = 0; i < p.size(); i++)
	{
		if (p[i] == '0')
			continue;

		if (cur < i)
		{
			res += i - cur;
			cur += res;
		}
		
		cur += p[i] - '0';
		
	}

	return res;

}

int main(void)
{
	freopen("d:\\output.txt", "w", stdout);
	freopen("d:\\input.txt", "r", stdin);

	int T;
	cin >> T;
	int S;
	string p;
	
	for (int i = 0; i < T; i++)
	{
		cin >> S >> p;
		cout << "Case #"<<i+1<<": " << doit(p) << endl;
	}
}