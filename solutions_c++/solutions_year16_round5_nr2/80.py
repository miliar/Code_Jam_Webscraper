#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define trav(a, v) for(auto& a : v)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

int val(int at, vector<vi>& gives) {
	int sum = 1;
	trav(it, gives[at]) {
		sum += val(it, gives);
	}
	return sum;
}

void solve() {
	static int tc = 1;
	cout << "Case #" << tc << ": ";
	tc++;
	int C;
	cin >> C;
	vector<vi> gives(C+1);
	rep(i,0,C) {
		int x;
		cin >> x;
		gives[x].push_back(i + 1);
	}
	vi value(C + 1);
	rep(i,0,C+1) value[i] = val(i, gives);
	string id;
	cin >> id;
	int cool;
	cin >> cool;
	rep(i,0,cool) {
		string word;
		cin >> word;
		int has = 0;
		rep(j,0,10000) {
			vi cur = gives[0];
			string str;
			while (sz(cur)) {
				int sum = 0;
				trav(it, cur) sum += value[it];
				int choice = rand()%sum;
				int idx = 0;
				trav(it, cur) {
					choice -= value[it];
					if (choice < 0) break;
					idx++;
				}
				int w = cur[idx];
				str += id[w - 1];
				swap(cur[idx], cur.back());
				cur.pop_back();
				cur.insert(cur.end(), all(gives[w]));
			} 
			if (str.find(word) != string::npos) has++;
		}
		cout << fixed << setprecision(4) << endl;
		cout << has / 10000.0 << ' ';
	}
	cout << endl;
}

int main() {
	int N;
	cin.sync_with_stdio(false);
	cin >> N;
	while(N-->0) solve();
}
