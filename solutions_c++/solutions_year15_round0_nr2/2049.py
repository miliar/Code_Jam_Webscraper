#include <iostream>
#include <cstring>
#include <queue>
#include <cmath>
#include <cassert>
#include <map>
#include <algorithm>
using namespace std;

#define REP(i,n) for(int i = 0; i < n; i++)

const int inf = 1<<28;
int T, d, x;

int bestz, v[1005], w[1005];
struct data {
	int here_v[1005], here_d;
	data() {
		here_d = 0;
		REP(i,d) if (v[i]) here_v[here_d++] = v[i];
		sort(here_v, here_v + here_d);
	}
	bool operator <(const data& a) const {
		if (here_d != a.here_d) return here_d < a.here_d;
		REP(i,here_d) if (here_v[i] != a.here_v[i]) return here_v[i] < a.here_v[i];
		return false;
	}
};
map<data,int> seen;

void brute(int time) {
	if (seen.count(data())) return;
	seen[data()] = 1;

/*
	if (true || time <= 3) {
		cout << "*" << time << " ";
		REP(i,d) cout << v[i] << " ";
		cout << endl;
	} else {
//		return;
	}
*/

	{
		int top = 0;
		REP(i,d) top = max(top, v[i]);
		bestz = min(bestz, time + top);
	}

/*
	bool done = true;
	REP(i,d) if (v[i]) done = false;
	if (done) {
//		return;
	}

	//all eat?
/*
	bool ok[1005];
	REP(i,d) if (v[i] > 0) {
		ok[i] = true;
		v[i]--;
	} else ok[i] = false;
	brute(time+1);
	REP(i,d) if (ok[i]) v[i]++;
*/

	//split each pile in half...
	REP(i,d) if (v[i] > 1) {
		for (int ww = 1; ww < v[i]-1; ww++) {
			int old = v[i];
			v[i] = ww;
			v[d] = old - ww;
			d++;
			brute(time+1);
			d--;
			v[i] = old;
		}
	}
}

int main() {
	cin >> T;
	REP(qqq,T) {
		cin >> d;

		priority_queue<int> q;
//		q.clear();
		REP(i,d) {
			cin >> x;
			v[i] = x;
			w[i] = x;
			q.push(x);
		}

		int best = inf, curr_time = 0;
		for (int critical = 1; critical < 1005; critical++) {
			int need = critical;
			REP(i,d) {
				need += (v[i] + critical-1) / critical - 1;
			}
			best = min(best, need);
		}

/*
		while (curr_time < best) {
			x = q.top(); q.pop();

			//stop now, don't split any more
			best = min(best, curr_time + x);

			//split the top stack, keep going
			int new_a = x/2;
			int new_b = x - new_a;
			q.push(new_a);
			q.push(new_b);
			curr_time++;
		}
*/

		cout << "Case #" << (qqq+1) << ": " << best << endl;

/*
		bestz = inf;
		seen.clear();
		brute(0);
//		cout << bestz << endl;
		if (best != bestz) {
			cout << best << "          " << bestz << endl;
			REP(i,d) cout << w[i] << " ";
			cout << endl;
			assert(false);
		}
*/
	}
}
