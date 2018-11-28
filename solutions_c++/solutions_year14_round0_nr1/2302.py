#include <string>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <list>
#include <set>

using namespace std;

#define fr first
#define sd second
#define pb push_back
#define mp make_pair

typedef long long ll;
typedef vector < vector < double > > vvd;
typedef vector < double > vd;
typedef vector < pair < double, double> > vdd;
typedef vector < vector < long long > > vvl;
typedef vector < long long > vl;


int main()
{
	int T;
	cin >> T;

	for(int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";

		int ans;
		cin >> ans;

		set<int> row;

		for(int i = 1; i <= 4; i++) {
			for(int j = 0; j < 4; j++) {
				int b;
				cin >> b;
				if(i == ans) {
					row.insert(b);
				}
			}
		}

		cin >> ans;
		int cnt = 0;
		int lst = 0;
		for(int i = 1; i <= 4; i++) {
			for(int j = 0; j < 4; j++) {
				int b;
				cin >> b;
				if(i == ans) {
					if(row.find(b) != row.end()) {
						cnt++;
						lst = b;
					}
				}
			}
		}
//		cout << cnt << " " << lst;

		if(cnt == 0) {
			cout << "Volunteer cheated!";
		} else if (cnt == 1) {
			cout << lst;
		} else {
			cout << "Bad magician!";
		}

		cout << endl;
	}
	

	return 0;
}
