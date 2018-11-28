#if 1
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
#include <stdio.h>
#include <string.h>
using namespace std;

#define MAX(a, b) (((a)>(b))?(a):(b))
#define REP(i, n) for(i=0;i<(n);i++)    
#define FOR(i, l, h) for(i=(l);i<=(h);i++) 
#define FORD(i, h,l) for(i=(h);i>=(l);i--) 

typedef vector<int> VI;    // interger vector
typedef vector<string> VS; // string vector
typedef vector<double> VD; // double vector
typedef long long LL;    // long long type
typedef pair<int, int> PII; // integer pair

void main_algorithm()
{
	int n;
	int result, cur;
	string in;
	int i;

	// solve problem
	cin >> n;
	cin >> in;

	cur = 0;
	result = 0;
	FOR(i, 0, n)
	{
		char c = in[i];
		c = c - '0';

		if (cur < i)
		{
			cur++;
			result++;
		}
		cur += c;
	}

	cout << result << endl;
}

int main(int argc, char *argv[])
{
	int n;
	int case_no;

	cin >> n;

	for (case_no = 1; case_no <= n; case_no++)
	{
		cout << "Case #" << case_no << ": ";
		main_algorithm();
	}

	return 0;
}
#endif