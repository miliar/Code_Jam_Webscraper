#include <vector>
#include <iterator>
#include <list>
#include <map>
#include <math.h>
#include <cmath>
#include <set>
#include <queue>
#include <deque>
#include <string>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <string.h>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#define pi 3.14159
#define inf 9e10
using namespace std;
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int testcases;
	cin >> testcases;
	for (int tc = 1; tc <= testcases; tc++)
	{
		double c, f, x, i = 0;
		cin >> c >> f >> x;
		double currentime = x / ((f*i) + 2), newfactime = c / 2 + (x / (f + 2)) , time = 0;
		while ( currentime > newfactime)
		{
			time += c / (f*i + 2);
			i++;
			currentime = x / (f*i + 2);
			newfactime = (c / (f*i + 2)) + (x / (f*(i + 1) + 2));
		}
		time += currentime;
		cout << "Case #"<<tc<<": "<<fixed<<setprecision(7)<< time << endl;
	}
	return 0;
}