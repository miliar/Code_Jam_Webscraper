#include <cstdio>
#include <iostream>
#include <map>
#include <queue>
#include <string>
#include <vector>

#define mp make_pair
#define pb push_back

#define REP(i,n) for(int i=0; i < (n); ++i)

typedef long long ll;

using namespace std;

int keys[500] = {0,};
int visited[1234567] = {0, };
int solution[500];
int open[300];

bool success = false;

void go(int c, int s, int nn, vector<vector<int> > & chest)
{
	if(visited[s]) return;
	visited[s] = true;

	if(c >= nn) {
		REP(i, nn) cout << solution[i]+1 << " ";
		cout << endl;
		success = true;
		return;
	}

	for(int i = 0; i < nn; ++i) {
		if (s & (1 << i)) continue;
		if (keys[open[i]] > 0) {
			keys[open[i]]--;
			solution[c] = i;

			REP(j, chest[i].size()) {
				keys[chest[i][j]]++;
			}

			go(c+1, s | (1 << i), nn, chest);

			REP(j, chest[i].size()) {
				keys[chest[i][j]]--;
			}

			visited[i] = false;

			if(success) return;

			keys[open[i]]++;
		}
	}
}
void solve()
{
	int k,n;

	vector<vector<int> > chest;

	REP(i, 500) {
		keys[i] = 0;
	}
	REP(i, 1234567) visited[i] = 0;

	cin >> k >> n;

	REP(i, k) {
		int x;
		cin >> x;
		keys[x]++;
	}
	REP(i, n) {
		cin >> open[i];
		int count;
		cin >> count;
		chest.pb(vector<int>());
		REP(j,count) {
			int xx;
			cin >> xx;
			chest[i].pb(xx);
		}
	}
	success = false;
	go(0, 0, n, chest);
	if(!success) cout << "IMPOSSIBLE" << endl;
}

int main(int argc, char *argv[])
{
	int t;
	cin >> t;
	for(int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}

