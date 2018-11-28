#include <iostream>
#include <set>
#include <algorithm>
#include <iomanip>

using namespace std;

int main(){
	freopen("C:/Users/Johan Sannemo/Downloads/B-large.in", "r", stdin);
	freopen("C:/Users/Johan Sannemo/Downloads/B-large.out", "w", stdout);
	int T;
	cin >> T;
	cout << fixed << setprecision(7);
	for (int tc = 1; tc <= T; ++tc){
		double c, f, x;
		double prod = 2;
		cin >> c >> f >> x;
		double curtime = 0;
		double best = 50000;
		while (curtime <= best){
			best = min(best, curtime + x / prod);
			curtime += c / prod;
			prod += f;
		}
		cout << "Case #" << tc << ": " << best << endl;
	}

}