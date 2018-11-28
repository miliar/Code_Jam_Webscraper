#include <iostream>
#include <cmath>
#include <iomanip>
#include <vector>
#include <algorithm>

using namespace std;

int n;
int x[1024];
int y[1024];
int z[1024];

int p[1024];

int find(int x) {
	if(p[p[x]] != p[x]) {
		p[x] = find(p[x]);
	}
	return p[x];
}

void merge(int a, int b) {
	a = find(a);
	b = find(b);
	p[a] = b;
}

int main() {
	int tc;
	cin >> tc;
	
	for(int ti = 1; ti <= tc; ++ti) {
		int s;
		cin >> n >> s;
		for(int i = 0; i < n; ++i) {
			double asd;
			cin >> x[i] >> y[i] >> z[i] >> asd >> asd >> asd;
			p[i] = i;
		}
		
		vector<pair<double, pair<int, int>>> Q;
		for(int i = 0; i < n; ++i) {
			for(int j = i + 1; j < n; ++j) {
				double dx = x[j] - x[i];
				double dy = y[j] - y[i];
				double dz = z[j] - z[i];
				double d = sqrt(dx * dx + dy * dy + dz * dz);
				
				Q.emplace_back(d, make_pair(i, j));
			}
		}
		sort(Q.begin(), Q.end());
		
		double res = 0.0;
		for(auto p : Q) {
			merge(p.second.first, p.second.second);
			if(find(0) == find(1)) {
				res = p.first;
				break;
			}
		}
		
		cout << "Case #" << ti << ": ";
		cout << fixed << setprecision(8) << res << '\n';
//		cout << '\n';
	}
	
	return 0;
}
