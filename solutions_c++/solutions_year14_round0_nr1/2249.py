#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>

using namespace std;

#define FOR(i,a,b) for(int i = a ; i < b ; i++)

void solvePr1() {
	int T;
	cin >> T;
	for(int tc = 1 ; tc <= T ; tc++) {
		int r1, r2;
		int arr1[4][4], arr2[4][4];
		cin >> r1;
		FOR(i,0,4) {
			FOR(j,0,4) {
				cin >> arr1[i][j];
			}
		}
		cin >> r2;
		FOR(i,0,4) {
			FOR(j,0,4) {
				cin >> arr2[i][j];
			}
		}
		vector <int> v;
		FOR(i,0,4) {
			FOR(j,0,4) {
				if(arr1[r1-1][i] == arr2[r2-1][j]) {
					v.push_back(arr1[r1-1][i]);
				}
			}
		}
		cout << "Case #" << tc << ": ";
		if(v.size() == 1) {
			cout << v[0] << endl;
		} else if(v.size() > 1) {
			cout << "Bad magician!" << endl;
		} else if(v.size() == 0) {
			cout << "Volunteer cheated!" << endl;
		}
	}
}

int main() {
	freopen("C:/Users/deepd/Downloads/in.txt", "r", stdin);
	freopen("C:/Users/deepd/Downloads/out.txt", "w", stdout);
	solvePr1();
	return 0;
}
