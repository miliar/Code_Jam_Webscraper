#include <algorithm>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>
#include <map>
#include <bitset>

using namespace std;

ofstream out("out.txt");
map<int, int> inv;
map<int, pair<int, map<int, int> > > chests;
vector<int> visited[1048576];
//1 means closed, 0 opened
bool done = false;

int N;
//all lookups are to use inverted direction


int keys(int state, int which) {
	int copy = state;
	int sum = 0;
	for (int i = 0; i < N; i++) {
		int a = state % 2;
		state /= 2;
		if (!a) {
			sum += chests[i].second[which];
			if (chests[i].first == which)
				sum -= 1;
		}

	}
//	if (sum)
//		return sum;
	sum += inv[which];

//	cout << "in state "<<bitset<4>(copy)<<", I have "<<sum<<" of key "<<which<<endl;
	return sum;
}

void loot(int cur) {
	if (!cur) {
		//we're done
		for(int i = 1; i <5; i++)
			keys(cur, i);
		done = true;
	}
	int copy = cur;
	int it = 0;
	while (copy) {
		int a = copy % 2;
		copy /= 2;
		if (a) {
			if(keys(cur, chests[it].first)) {
			int next = cur & ~(1 << it);
			if (visited[next].empty()) {
				visited[next] = visited[cur];
				visited[next].push_back(it);
				loot(next);
				if (done)
					return;
			}
		}
	}
		it++;
	}
}

int main() {

	ifstream f("D-small-attempt0.in");
	int T;
	f >> T;

	for (int x = 0; x < T; x++) {
		int K;

		f >> K >> N;
		inv.clear();
		chests.clear();
		for (int i = 0; i < K; i++) {
			int n;
			f >> n;
			inv[n]++;
		}

		for (int i = 0; i < N; i++) {
			int n;
			f >> n;
			chests[i].first = n;
			f >> n;
			for (int j = 0; j < n; j++) {
				int r;
				f >> r;
				chests[i].second[r]++;
			}
		}
		for (int i = 0; i < 1048576; i++) {
			visited[i].clear();
		}
		done = false;


		loot(pow(2, N) - 1);

		if (visited[0].empty())
			out << "Case #" << x + 1 << ": IMPOSSIBLE" << endl;
		else {
			out << "Case #" << x + 1 << ":";
			for (int i = 0; i < visited[0].size(); i++) {
				out << " " << visited[0].at(i)+1;
			}
			out << endl;
		}

	}

	return 0;
}
