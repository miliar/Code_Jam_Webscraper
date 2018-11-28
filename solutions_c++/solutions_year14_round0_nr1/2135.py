#include <cstring>
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <cstdio>

using namespace std;

int was[20];

void Load()
{
	memset(was, 0, sizeof(was));
	int n;
	int i, j, a;
	cin >> n;
	for (i = 0; i < 4; i++) {
		for (j = 0; j < 4; j++) {
			cin >> a;
			if (i == n-1) {
				was[a] = 1;
			}
		}
	}
	cin >> n;
	for (i = 0; i < 4; i++) {
		for (j = 0; j < 4; j++) {
			cin >> a;
			if (i == n-1) {
				was[a] += 1;
			}
        }
	}
}

void Solve()
{
	int i;
	int cnt, ans;
	cnt = 0;
	for (i = 1; i <= 16; i++) {
		if (was[i] == 2) {
			cnt++;
			ans = i;
		}
    }
    if (cnt == 0) cout << "Volunteer cheated!\n";
    else if (cnt == 1) cout << ans << "\n";
    else cout << "Bad magician!\n";
}

int main()
{
	cout.setf(ios::fixed|ios::showpoint);
	cout.precision(10);
	int nt, tt;
	cin >> nt;
	for (tt = 1; tt <= nt; tt++) {
		cout << "Case #" << tt << ": ";
		Load();
		Solve(); 
	}
	return 0;
}
