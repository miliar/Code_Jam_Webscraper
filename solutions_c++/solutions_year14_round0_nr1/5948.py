#include <iostream>
#include <cstring>
#include <vector>
#include <set>
#include <cstdio>
#include <cmath>
#include <map>
#include <queue>
#include <stack>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <cstdlib>

using namespace std;

#define LL long long
#define ULL unsigned long long

#define REP(var, init, limit, inc) for(int var = init; var < limit; var += inc)
#define FF first
#define SS second

typedef pair <int, int> PII;
const LL oo = 1e9 + 5;
const int LM = 1e5 + 5;

class a {
public:
	void init() {
		int T;
		cin >> T;
		REP(test_case, 1, T+1, 1) {
			int row1[17], row2[17];
			int choice1, choice2;

			cin >> choice1;
			REP(i, 0, 4, 1) {
				REP(j, 0, 4, 1) {
					int X;
					cin >> X;
					row1[X] = i+1;
				}
			}

			cin >> choice2;
			REP(i, 0, 4, 1) {
				REP(j, 0, 4, 1) {
					int X;
					cin >> X;
					row2[X] = i+1;
				}
			}

			set <int> sols;
			REP(i, 1, 17, 1)
				if (row1[i] == choice1 && row2[i] == choice2)
					sols.insert(i);

			cout << "Case #" << test_case << ": ";
			if (sols.size() == 1)
				cout << *sols.begin();
			else if (sols.size())
				cout << "Bad magician!";
			else
				cout << "Volunteer cheated!";

			cout << endl;
		}
	}
};
