#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <sstream>
using namespace std;
typedef vector<string> vs;
typedef vector<int> vi;
typedef long long ll;
typedef pair<int,int> pii;
#define sz(A) (int)(A).size()
#define FOR(A,B) for(int A=0; A < (int) (B);A++)
#define FOREACH(I,C) for(__typeof(C.begin()) I = (C).begin(); I != (C).end(); I++)
#define pb push_back
#define all(x) x.begin() , x.end()
#define mp make_pair

int N;
vi dummy;
vector< vector<int> > lists;
vector < vector<int> > rows, cols;

bool check_add_row(vi list, int skip) {
	int idx = sz(rows);
	if (idx == skip) {
		return true;
	}

	FOR(i, sz(cols)) {
		if (cols[i][idx] != -1 && cols[i][idx] != list[i]) return false;
	}
	return true;
}

bool check_add_col(vi list, int skip) {
	int idx = sz(cols);
	if (idx == skip) {
		return true;
	}

	FOR(i, sz(rows)) {
		if (rows[i][idx] != -1 && rows[i][idx] != list[i]) return false;
	}
	return true;
}

vi compute(int skip_row, int skip_col) {
	vi ans;
	if (skip_col != -1) {
		FOR(i, sz(rows)) {
			ans.pb(rows[i][skip_col]);
		}
	} else {
		FOR(i, sz(cols)) {
			ans.pb(cols[i][skip_row]);
		}
	}
	return ans;
}

void print_state(int pos) {
	return;

	cout <<  "N = " << N << " pos = " << pos << endl;
	FOR(i, N) {
		FOR(j, N) {
			if (sz(rows) > i) {
				cout << rows[i][j];
			} else if (sz(cols) > j) {
				cout << cols[j][i];
			} else {
				cout << "N";
			}
			cout << " ";
		}
		cout << endl;
	}
	cout << endl;
}

void print_list(vi list) {
	return;

	FOR(i, sz(list)) {
		cout << list[i] << " ";
	}
	cout << endl;
}

void print_row_status(int pos, bool ok) {
	return;

	if (ok) {
		cout << "Can add row at " << sz(rows) << " : ";
		print_list(lists[pos]);
	} else {	
		cout << "!Cannot add row at " << sz(rows) << " : ";
		print_list(lists[pos]);
	}

	cout << " Done " << endl << endl;
}

void print_col_status(int pos, bool ok) {
	return;

	if (ok) {
		cout << "Can add col at " << sz(cols) << " : ";
		print_list(lists[pos]);
	} else {	
		cout << "!Cannot add col at " << sz(cols) << " : ";
		print_list(lists[pos]);
	}

	cout << " Done " << endl << endl;
}


vi solve_rec(int pos, int skip_row, int skip_col, bool done) {

	if (pos == 2*N - 1 && done) {
		return compute(skip_row, skip_col);
	}
	
	if (sz(rows) < N) {
		if(check_add_row(lists[pos], !done ? skip_row : -1)) {
			print_state(pos);
			print_row_status(pos, true);
			bool new_done = done;
			if (!done && skip_row == sz(rows)) {
				new_done = true;
				rows.pb( dummy );
			} else {
				rows.pb(lists[pos]);
			}
			vi ans = solve_rec(new_done != done ? pos : pos + 1, skip_row, skip_col, new_done);
			if (sz(ans) > 0) {
				return ans;
			}
			rows.pop_back();
		} else {
			print_state(pos);
			print_row_status(pos, false);
		}
	}
	if (sz(cols) < N) {
		if (check_add_col(lists[pos], !done ? skip_col : -1)) {
			print_state(pos);
			print_col_status(pos, true);
			bool new_done = done;
			if (!done && skip_col == sz(cols)) {
				new_done = true;
				cols.pb( dummy );
			} else {
				cols.pb(lists[pos]);
			}
			vi ans = solve_rec(new_done != done ? pos : pos + 1, skip_row, skip_col, new_done);
			if (sz(ans) > 0) {
				return ans;
			}
			cols.pop_back();
		} else {
			print_state(pos);
			print_col_status(pos, false);
		}
	}
	vi ans;
	return ans;
}

void solve() {
	cin >> N;
	lists.clear();
	rows.clear();
	cols.clear();
	dummy.clear();
	FOR(i, N) dummy.pb(-1);

	FOR(i, 2*N - 1) {
		vi aux;
		FOR(j, N) {
			int tmp;
			cin >> tmp;
			aux.pb(tmp);
		}
		lists.pb(aux);
	}
	sort(all(lists));

	FOR(i, N) {
		vi ans;
		ans = solve_rec(0, i, -1, false);
		if (sz(ans)) {
			FOR(i, sz(ans)) {
				cout << " " << ans[i];
			}
			cout << endl;
			return;
		}
		ans = solve_rec(0, -1, i, false);
		if (sz(ans)) {
			FOR(i, sz(ans)) {
				cout << " " << ans[i];
			}
			cout << endl;
			return;
		}
	}
}

int main() {
  int num_testes;
  scanf("%d", &num_testes);
  for(int t = 1; t <= num_testes; t++) {
    printf("Case #%d:", t);
    solve();
  }
  return 0;
}
