/*
* @Author: ritesh
* @Date:   2016-04-08 20:54:06
* @Last Modified by:   ritesh
* @Last Modified time: 2016-04-08 21:19:36
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

		int m = 0;
		cin >> m;


		set<int> sheep;
		sheep.clear();
		bool insom = false;
		int sleeping_sheep = 0;
		int count = 0;
		while(sheep.size() != 10 and !insom)
		{
			count += 1;
			int n = count * m;
			if (count > 1 and m==n) { insom = true; break; }
			while (n > 0 )
			{
				int r = n%10;
				n = n/10;
				sheep.insert(r);
			}
		}

		if (insom)
			cout << "INSOMNIA\n";
		else
			cout << m * count << "\n";
	}

	return 0;
}
