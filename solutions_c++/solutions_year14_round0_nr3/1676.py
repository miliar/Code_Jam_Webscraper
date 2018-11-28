#include <queue>
#include <vector>
#include <iostream>
using namespace std;

bool f = false;
void solve() {
	int r, c, m;
	cin >> r >> c >> m;
	for(int mask = 0; mask < (1 <<(r*c)); ++mask) {
		int inmask = 0;
		for(int i = 0; i < (r*c); ++i){
			if(mask & ( 1 << i)) {
				++inmask;
			}
		}
		if(m != inmask)
			continue;
		for(int start = 0; start < r * c; ++start) {
			if(mask & (1 << start)) {
				continue;
			}
			queue<int> q;
			int x = start / c;
			int y = start % c;
			vector<int> used(r * c);
			q.push(start);
			int cnt = 1;

			used[start] = true;
			while(!q.empty()) {
				x = q.front() / c;
				y = q.front() % c;
				q.pop();
			bool go = true;
				for(int dx = -1; dx <= 1; ++dx)
					for(int dy = -1; dy <= 1; ++dy) {
						int nx = x + dx;
						int ny = y + dy;
						if(nx >= 0 && ny >= 0 && nx < r && ny < c) {
							int k = nx * c + ny;
							if(mask & (1 << k)) {
			//					if(f && mask == 3 && start == 3 && x == 1 && y == 3) {
			//						cout << nx << ' ' << ny << endl;
			//					}
								go = false;
							}
						}
					}
				if(go) {
				for(int dx = -1; dx <= 1; ++dx)
					for(int dy = -1; dy <= 1; ++dy) {
						int nx = x + dx;
						int ny = y + dy;
						if(nx >= 0 && ny >= 0 && nx < r && ny < c) {
							int k = nx * c + ny;
							if(!used[k]) {
								q.push(k);
								used[k] = true;
								++cnt;
							}
						}
					}
				}
			}
			if(cnt + m == r * c) {
				for(int i = 0; i < r; ++i) {
					for(int j = 0; j < c; ++j) {
						int k = i * c + j;
						if(start == k)
							cout << 'c';
						else if(mask & (1 << k))
							cout << '*';
						else
							cout << '.';
					}
					cout << "\n";
				}
				return;
			}
		}

	}
	cout << "Impossible\n";
}

int main() {
	int t;
	cin >> t;
	for(int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ": \n";
		cerr << i << endl;
		solve();
	}
	return 0;
}
