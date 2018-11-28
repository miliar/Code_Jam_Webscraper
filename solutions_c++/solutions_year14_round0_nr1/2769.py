#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>

using namespace std;

#define REP(i, a) for (int i = 0; i < (int)(a); i++)
#define FOR(i, a, b) for (int i = (int)(a); i <= (int)(b); i++)
#define CLEAR(x, val) memset(x, val, sizeof x)

int tc;
int r1, r2, temp;
bool possible[20];

int main () {
	cin >> tc;
	
	FOR(id, 1, tc) {
		CLEAR(possible, 0);
		
		int intersect = 0;
		int ans = 0;
		
		cin >> r1;
		FOR(i, 1, 4) {
			FOR(j, 1, 4) {
				cin >> temp;
				
				if (i == r1) {
					possible[temp] = 1;
				}
			}
		}
		
		cin >> r2;
		FOR(i, 1, 4) {
			FOR(j, 1, 4) {
				cin >> temp;
				
				if (i == r2) {
					if (possible[temp]) {
						intersect++;
						ans = temp;
					}
				}
			}
		}
		
		cout << "Case #" << id << ": ";
		
		if (intersect == 0) {
			cout << "Volunteer cheated!";
		}
		else if (intersect == 1) {
			cout << ans;
		}
		else {
			cout << "Bad magician!";
		} 
		
		cout << endl;
	}
}
