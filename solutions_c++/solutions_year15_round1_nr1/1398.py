// K1
// :)

#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <queue>
#include <bitset>
#include <string>
#include <cmath>
#include <iomanip>
#include <set>
#include <map>

#define EPS 1e-8
#define PI 3.141592653589793
#define X first
#define Y second
#define FX(x) fixed << setprecision((x))

using namespace std;

typedef pair<int, int> point;
typedef set<int>::iterator ITR;
const int MAXN = 2e5 + 123;


int main()
{
	int T;
	cin >> T;
	for (int test = 0; test < T; ++test)
	{
		vector <int> vec;
		int n;
		cin >> n;
		for (int i = 0; i < n; ++i)
		{
			int inp;
			cin >> inp;
			vec.push_back(inp);
		}
		long long res1 = 0;
		long long res2 = 0;

		for (int i = 0; i < n-1; ++i)
			if(vec[i] > vec[i+1])
				res1 += vec[i] - vec[i+1];
		int mx_dis = -1;
		for (int i = 0; i < n-1; ++i)
			if(vec[i] - vec[i+1] > mx_dis)
				mx_dis = vec[i] - vec[i+1];
		for (int i = 0; i < n-1; ++i)
		{
			if(vec[i] - vec[i+1] == mx_dis) res2 += mx_dis;
			else if(vec[i+1] > vec[i]) res2 += min(vec[i], mx_dis);
			else res2 += min(vec[i], mx_dis);
		}

		cout << "Case #" << test+1 <<": " << res1 << " " << res2 << endl;

	}
	return 0;
}