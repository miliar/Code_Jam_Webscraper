#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <fstream>
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
using namespace std;

#define cin in
#define cout out

const int OO = (int) 2e9;

int shynessArr[1001];

int main()
{
	ifstream in("in.txt");
	ofstream out("out.txt");

	int t, n;
	string input;

	cin >> t;

	for (int i = 0; i < t; i++)
	{
		cin >> n;

		int sum = 0;
		int needed = 0;

		cin >> input;

		for (int j = 0; j <input.length(); j++)
		{
			int currentShynessCount;
			currentShynessCount = input[j] - '0';

			if (sum + needed < j)
				needed += j - (sum + needed);
			sum += currentShynessCount;
		}

		cout << "Case #" << i + 1 << ": " << needed << endl;
	}
}