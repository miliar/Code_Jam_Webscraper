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

//int gcd(int a, int b) {
//     return b == 0 ? a : gcd(b, a % b);
// }

// int gcd(vector <int> vec)
// {
// 	int result = gcd(vec[0], vec[1]);
// 	for (int i = 2; i < vec.size(); ++i)
// 		result = gcd(result, vec[i]);
// 	return result;
// }

// int lcs(vector<int> v)
// {
// 	int result = 1;
// 	for (int i = 0; i < v.size(); ++i)
// 		result *= v[i];
// 	result /= gcd(v);
// 	return result;
// }

// int cutted(vector <int> vec)
// {
// 	int lcs = lcs(vec);
// 	int result = 0;
// 	for (int i = 0; i < vec.size(); ++i)
// 		result += lcs / vec[i];
// 	return result;
// }

int main()
{
	int T;
	cin >> T;
	for (int test = 0; test < T; ++test)
	{
		vector < point > vec;
		int b, n;
		cin >> b >> n;
		for (int i = 0; i < b; ++i)
		{
		 	int inp;
		 	cin >> inp;
		 	vec.push_back(make_pair(inp, i));
		}
		// sort(vec.begin(), vec.end());

		vector <int> list;
		// n %= cutted(vec);
		for (int time = 0; ; ++time)
		{
			int good = 0;
			for (int i = 0; i < vec.size(); ++i)
			{
				if(time % vec[i].X == 0) {
					list.push_back(vec[i].Y);
					good ++;
				}
			}
			if(time && good == vec.size()) break;
		}
		list.resize(list.size() - vec.size());

		// for (int i = 0; i < list.size(); ++i)
		// {
		// 	cerr << list[i] << " - ";
		// }
		// cerr << endl;
		n--;
		n %= list.size();
		cout << "Case #" << test+1 <<": " << list[n] + 1 << endl;
	}
	return 0;
}