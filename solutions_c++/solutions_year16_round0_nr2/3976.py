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

vector<int> input;

int solve_rec(int idx, int required) {
	if (idx < 0) { return 0; }

	if (input[idx] == required) {
		return solve_rec(idx - 1, required);
	} else {
		return 1 + solve_rec(idx - 1, 1 - required);
	}
}

void solve() {
	string input_sign;
	cin >> input_sign;
	int ans = 0;
	input.clear();
	FOR(i, sz(input_sign)) {
		if (input_sign[i] == '+') input.push_back(1);
		else input.push_back(0);
	}
	
	ans = solve_rec( sz(input) - 1, 1);
	cout << ans << endl;
}

int main() {
  int num_testes;
  scanf("%d", &num_testes);
  for(int t = 1; t <= num_testes; t++) {
    printf("Case #%d: ", t);
    solve();
  }
  return 0;
}
