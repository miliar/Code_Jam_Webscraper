#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#pragma comment(linker, "/STACK:16777216")

#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <stack>
#include <set>
#include <queue>
#include <numeric>
#include <algorithm>
#include <utility>
#include <bitset>
#include <cmath>
#include <sstream>
#include <functional>
#include <iomanip> 

#define all(a) (a).begin(),(a).end()
#define sz(a) (int)(a).size()

using namespace std;

typedef long long int64;
typedef vector<int> vi;
typedef vector< vi > vvi;
typedef vector<double> vd;
typedef vector< vd > vvd;
typedef vector< string > vs;
typedef pair< int, int > pii;
typedef vector< pii > vpii;



int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif
	int T = 0;
	cin >> T;
	for (int t = 0; t < T; t++)
	{

		double c, f, x;
		cin >> c >> f >> x;
		double tmin = x / 2.0;
		double current_add_time = 0;
		double current_v = 2;
		for (int i = 0; i < 100000; i++)
		{
			current_add_time += c / current_v;
			current_v += f;
			double current_t = x / current_v + current_add_time;
			if (current_t < tmin)
				tmin = current_t;
			else
				break;
		}

		cout << "Case #" << t + 1 << ": ";
		// TODO: Answer here
		cout << setprecision(16) << tmin << endl;
	}

	return 0;
}