#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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

using namespace std;

typedef vector<int> vi;
typedef long long ll;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<vi> vvi;
typedef vector<vii> vvii;

#define INF 100000000

int main()
{
	int T; cin >> T;
	int temp;
	for(int t = 1; t <= T; ++t)
	{
		int answer1; cin >> answer1;	
		vi cand1(4);
		for(int row = 1; row <= 4; ++row) {
			if (row != answer1) {
				for (int i = 0; i < 4; ++i) { cin >> temp; }
				continue;
			}
			for (int col = 0; col < 4; ++col) {
				cin >> cand1[col];
			}
		}
		int answer2; cin >> answer2;
		set<int> cand2;
		for(int row = 1; row <= 4; ++row) {
			if (row != answer2) {
				for (int i = 0; i < 4; ++i) { cin >> temp; }
				continue;
			}
			for (int col = 0; col < 4; ++col) {
				cin >> temp;
				cand2.insert(temp);
			}
		}
		int c = 0;
		int card = -1;
		for (int i = 0; i < 4; ++i) {
			if (cand2.count(cand1[i])) {
				c++;
				card = cand1[i];
			}
		}
		printf("Case #%d: ", t);
		if (c == 0) printf("Volunteer cheated!");
		else if (c == 1) printf("%d", card);
		else printf("Bad magician!");
		printf("\n");
	}
}
