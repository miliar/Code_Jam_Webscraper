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
const int MAXN = 1e9;

int main()
{
	freopen("B-smal.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for(int test = 0; test < t; test ++)
	{
		int x, y;
		cin >> x >> y;
		cout << "Case #" << test + 1 << ": " ;
		for(int i=0; i<x; i++)
			cout << "WE";
		for(int i=x; i<0; i++)
			cout << "EW";
		for(int i=0; i<y; i++)
			cout << "SN";
		for(int i=y; i<0; i++)
			cout << "NS";
		cout << endl;

	}

	return 0;
}
