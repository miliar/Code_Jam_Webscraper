/*
* @Author: ritesh
* @Date:   2016-04-08 21:25:18
* @Last Modified by:   ritesh
* @Last Modified time: 2016-04-09 00:55:46
*/

#include <iostream>
#include <vector>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <cstring>
#include <queue>
#include <algorithm>
#include <climits>
#include <string>
#include <cstdlib>
#include <sstream>
#include <cmath>
#include <cctype>
#include <iomanip>
#include <cstdio>
#include <list>

using namespace std;

typedef pair <int, int> pii;
typedef pair <int, double> pid;
typedef pair <double, double> pdd;
typedef vector <int> vi;
typedef vector <double> vd;
typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;

#define MP make_pair
#define PB push_back
#define PPB pop_back
#define PF push_front
#define PPF pop_front
#define EL endl
#define CO cout

int main() {
	int Tcases;

	cin >> Tcases;

	for (int tc = 1; tc <= Tcases; tc++)
	{
		cout << "Case #" << tc << ": ";

		string m, mm;
		cin >> m;
		mm = m;
		int count = 0;
		while(m.find("-") != string::npos)
		{
			int sad_start = m.find("-");
			int sad_end = m.find_last_of("-");

			string n = m.substr(0, sad_end + 1);

			if (n.length() == 1 || n.find("+") == string::npos)
			{
				count += 1;
				break;
			}

			int happy_start = n.find("+");
			int happy_end = n.find_last_of("+");

			if (happy_end < sad_start)
			{
				count += 2;
				break;
			}
			if (sad_end < happy_start)
			{
				count += 1;
				break;
			}

			if(happy_start == 0)
			{
				n.replace(happy_start, sad_start, sad_start - happy_start, '-');
				count += 1;
				m = n;
				continue;
			}

			std::reverse(n.begin(), n.end());
			std::replace(n.begin(), n.end(), '-', '*');
			std::replace(n.begin(), n.end(), '+', '-');
			std::replace(n.begin(), n.end(), '*', '+');

			if (n.compare(m) == 0)
			{
				//same thing;  change happy start
				n[happy_start] = '-';

			}
			m = n;
			count += 1;

		}
		cout << count << "\n";
	}

	return 0;
}
