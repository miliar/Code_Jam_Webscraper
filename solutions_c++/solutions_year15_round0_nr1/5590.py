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
#include <memory.h>
#include <valarray>
using namespace std;
#define SZ(X) (int)(X).size()
#define ALL(X) (X).begin(),(X).end()
#define ALLR(X) (X).rbegin(),(X).rend()
const double EPS = 1e-9;
const int INF = 1 << 28;
const long long INFL = 1LL << 62;
int main()
{

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	cin >> t;
	vector <int> answers;

	for (int tt = 1; tt <= t; tt++){


		int max,stand=0,need=0;
		string loop;
		cin >> max;
		cin >> loop;
		for (int m = 0 ; m <= max ; m++){

			int temp = loop[m]-'0';
			if (temp != 0) {
				int add = 0;
				if (m>=stand) add= m - stand;
				stand += (temp + (add));
				need += add;
			}
		}
		answers.push_back(need);
	}
	for (int tt = 1; tt <= t; tt++){
		
		cout << "Case #" << tt << ": " << answers[tt-1]<<endl;
	}


	return 0;
}
