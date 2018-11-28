#include <bits/stdc++.h>
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define endl '\n'

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;

int cnt[3];
int rps[3];
const string let = "RPS";

int memo[3][3][15];
int isless(int t1, int t2, int lv) {
	if(lv == 0)	{
		return let[t1] < let[t2];
	}else if(memo[t1][t2][lv] != -1){
		return memo[t1][t2][lv];
	}else{
		int c1[2];
		int c2[2];
		if(t1 == 0) {
			c1[0] = 0;
			c1[1] = 2;
		}else if(t1 == 1) {
			c1[0] = 0;
			c1[1] = 1;
		} else {
			c1[0] = 1;
			c1[1] = 2;
		}

		if(t2 == 0) {
			c2[0] = 0;
			c2[1] = 2;
		}else if(t2 == 1) {
			c2[0] = 0;
			c2[1] = 1;
		} else {
			c2[0] = 1;
			c2[1] = 2;
		}
		
		if(isless(c1[1], c1[0], lv-1)) {
			swap(c1[0], c1[1]);
		}

		if(isless(c2[1], c2[0], lv-1)) {
			swap(c2[0], c2[1]);
		}

		if(isless(c1[0], c2[0], lv-1)) {
			return memo[t1][t2][lv] = 1;
		}else if(isless(c2[0], c1[0], lv-1)){
			return memo[t1][t2][lv] = 0;
		}else{
			return memo[t1][t2][lv] = isless(c1[1], c2[1], lv-1);
		}
	}
}


string cur;

vi possible;
vector<string> best;

void buildbest(int curl, int lv) {
	if(lv == 0){
		cur.pb(let[curl]);
	}else{
		int c[2];
		if(curl == 0) {
			c[0] = 0;
			c[1] = 2;
		}else if(curl == 1) {
			c[0] = 0;
			c[1] = 1;
		} else {
			c[0] = 1;
			c[1] = 2;
		}

		if(isless(c[1], c[0], lv-1)) {
			swap(c[0], c[1]);
		}

		buildbest(c[0], lv-1);
		buildbest(c[1], lv-1);
	}
}


int main() {
	ios_base::sync_with_stdio(0);
	memset(memo, -1, sizeof memo);

	int T;
	cin >> T;
	for(int t = 1; t <= T; t++) {
		best.clear();
		possible.clear();
		cout << "Case #" << t <<": ";

		int n;
		cin >> n;
		int tot = 1 << n;

		for(int i = 0; i < 3; i++){
			cin >> rps[i];
		}

		for(int i = 0; i < 3; i++){
			int aux[3];
			memset(cnt, 0, sizeof cnt);
			memset(aux, 0, sizeof aux);
			cnt[i] = 1;
			for(int j = 0; j < n; j++){
				memset(aux, 0, sizeof aux);
				aux[0] += cnt[0] + cnt[1];
				aux[1] += cnt[1] + cnt[2];
				aux[2] += cnt[2] + cnt[0];
				memcpy(cnt, aux, sizeof cnt);
			}

			if(cnt[0] == rps[0] and cnt[1] == rps[1] and cnt[2] == rps[2]){
				possible.pb(i);
			}
		}



		if(possible.size() == 0){
			cout << "IMPOSSIBLE" << endl;
			continue;
		}

		for(int i = 0; i < possible.size(); i++){
			cur.clear();	
			buildbest(possible[i], n);
			best.pb(cur);
		}

		sort(best.begin(), best.end());
		cout << best[0] << endl;
	}

	return 0;
}
