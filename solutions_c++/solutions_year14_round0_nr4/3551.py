#include <iostream>
#include <set>
#include <algorithm>
#include <iomanip>
#include <vector>

using namespace std;

int main(){
	freopen("C:/Users/Johan Sannemo/Downloads/D-large.in", "r", stdin);
	freopen("C:/Users/Johan Sannemo/Downloads/D-large.out", "w", stdout);
	int T;
	cin >> T;
	for (int tc = 1; tc <= T; ++tc){
		int n;
		cin >> n;
		vector<pair<double, int>> w(2 * n);
		for (int k = 0; k < 2; ++k){
			for (int i = 0; i < n; ++i){
				cin >> w[n * k + i].first;
				w[n * k + i].second = k;
			}
		}
		sort(w.begin(), w.end());
		int win = 0;
		int x = 0, y = 0;
		for (int i = 0; i < 2 * n; ++i){
			if (w[i].second == 1) y++;
			if (w[i].second == 0 && y > 0){
				win++;
				y--;
			}
		}
		cout << "Case #" << tc << ": " << win;
		win = 0;
		x = 0, y = 0;
		for (int i = 2 * n - 1; i >= 0; --i){
			if (w[i].second == 1) y++;
			if (w[i].second == 0 && y == 0){
				win++;
			}		
			if (w[i].second == 0) y = max(0, y - 1);

		}
		cout << " " << win << endl;
	}

}