#include <iostream>
#include <queue>
using namespace std;

priority_queue <pair <int, pair <int, int> > > q;

int main() {
	int t, d, p, odp, licz_s;
	pair <int, pair <int, int> > ap;
	cin >> t;
	for(int i = 1; i <= t; i ++) {
		cin >> d;
		odp = 0;
		licz_s = 0;
		for(int j = 0; j < d; j ++) {
			cin >> p;
			odp = max(odp, p);
			q.emplace(p, make_pair(p, 1));
		}
		while(!q.empty() && odp > licz_s) {
			ap = q.top();
			q.pop();
			if(ap.first != 1) {
				licz_s ++;
				ap.second.second ++;
				ap.first = (ap.second.first + ap.second.second - 1) / ap.second.second;
				q.push(ap);
			}
			odp = min(odp, q.top().first + licz_s);
		} 
		while(!q.empty())
			q.pop();
		cout << "Case #" << i << ": " << odp << endl;
	}
	return 0;
}
