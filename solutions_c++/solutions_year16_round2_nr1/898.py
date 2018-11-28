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

vector<string> numbers; // (10) = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
map<int, map<char, int> > num_counts;
map<int, string> num_vals;

void initialize() {
	// ZERO => Z
	// TWO => W
	// SIX => X
	// EIGHT => G
	// FOUR => U

	// ONE (O) ==> THREE (T) ==> FIVE (F) ==> SEVEN (S) ==> NINE 

	// string nums[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
	string nums[10] = {"ZERO", "TWO", "SIX", "EIGHT", "FOUR", "ONE", "THREE", "FIVE", "SEVEN", "NINE"};
	string nums_idx[10] = {"0", "2", "6", "8", "4", "1", "3", "5", "7", "9"};
	numbers.clear();
	num_counts.clear();
	num_vals.clear();
	FOR(i, 10) {
		string s = nums[i];
		numbers.pb(s);
		map<char, int> tmp;
		FOR(j, sz(s)) {
			tmp[s[j]]++;
		}
		num_counts[i] = tmp;
		num_vals[i] = nums_idx[i];
	}
}

bool isempty(map<char, int> count) {
	FOREACH(it, count) {
		if (it->second != 0) {
			return false;
		}
	}
	return true;
}

bool isinvalid(map<char, int> count) {
	FOREACH(it, count) {
		if (it->second < 0) {
			return true;
		}
	}
	return false;
}

void debug(map<char, int> count, int pos) {
	return;
	cout << "Going with pos = " << pos << endl;
	FOREACH(it, count) {
		cout << it->first << " = " << it->second << "; ";
	}
	cout << endl;
}

string solve_rec(map<char, int> count, int pos) {
	debug(count, pos);

	if (isempty(count)) {
		return "";
	}
	if (pos == 10 || isinvalid(count)) {
		return "-1";
	}

	FOREACH(it, num_counts[pos]) {
		count[it->first] -= num_counts[pos][it->first];
	}
	string aux = solve_rec(count, pos);
	if (aux != "-1") {
		stringstream ss;
		string curr;
		ss << pos;
		ss >> curr;
		return curr + aux; 
	}

	FOREACH(it, num_counts[pos]) {
		count[it->first] += num_counts[pos][it->first];
	}
	return solve_rec(count, pos+1);
}

string solve_greedy(map<char, int> count) {
	string ans = "";
	FOR(pos, 10) {
		while (true) {
			int ok = 1;
			FOREACH(it, num_counts[pos]) {
				if (count[it->first] < num_counts[pos][it->first]) {
					ok = 0;
				}
			}
			if (!ok) {
				break;
			}

			FOREACH(it, num_counts[pos]) {
				count[it->first] -= num_counts[pos][it->first];
			}
			ans += num_vals[pos];
		}
	}
	sort(all(ans));
	return ans;

}
void solve() {
	string input;
	cin >> input;
	map<char, int> count;
	FOR(i, sz(input)) {
		count[input[i]]++;
	}
	debug(count, -1);
	string nums = solve_greedy(count);
	cout << nums << endl;
}

int main() {
	initialize();
  int num_testes;
  scanf("%d", &num_testes);
  for(int t = 1; t <= num_testes; t++) {
    printf("Case #%d: ", t);
    solve();
  }
  return 0;
}
