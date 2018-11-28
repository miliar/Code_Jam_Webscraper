#define INF 1e9
#define EPS 1e-9
#include <iostream>
#include <vector>
#include <queue>
#include <utility>
#include <algorithm>
#include <cmath>
#include <set>
#include <sstream>
#include <string>
using namespace std;
typedef set<int> si;
typedef vector<si> vsi;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef pair<int, int> ii;
typedef pair<int, ii> iii;
typedef pair<double, ii> dii;
typedef vector<ii> vii;

bool eq(double a, double b) { return fabs(a-b) < EPS; }

int main() {

	int T;
	cin >> T;
	
	for (int t = 1; t <= T; t++) {
		int N; cin >> N;
		cout << "Case #" << t << ": ";
		vii senators(N);
		for (int i = 0; i < N; i++) {
			cin >> senators[i].first;
			senators[i].second = i;
		}
		sort(senators.begin(), senators.end());//, [](ii a, ii b) {return a.first < b.first;});
		int max = senators[N-1].first;
		while (senators[0].first >= 1) {
			int ind = lower_bound(senators.begin(), senators.end(), ii(max,0)) - senators.begin();
		//	cout << ind << "max " << max << "ub " << (upper_bound(senators.begin(), senators.end(), ii(max,0)) - senators.begin()) << endl;
			if (ind==0 && max==1 && (upper_bound(senators.begin(), senators.end(), ii(max,INF)) - senators.begin()) % 2 != 0) {
				senators[ind].first--;
		//		cout << "trigger" << endl;
				cout << (char)('A' + senators[ind++].second) << " ";
			}
			while (ind+1<N) {
				senators[ind].first--; senators[ind+1].first--;
				cout << (char)('A'+senators[ind].second) << (char)('A'+senators[ind+1].second) << " ";
				ind += 2;
			}
			if (ind < N) {
				senators[ind].first--;
				cout << (char)('A' + senators[ind++].second) << " ";
			}
			max--;
		}
		cout << endl;
	}

}
