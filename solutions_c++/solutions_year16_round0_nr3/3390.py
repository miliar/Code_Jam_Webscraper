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

/*
#define NN 10000000
bool is_prime[NN];

void pre_process() {
	for(long long i = 0; i < NN; i++) {
		is_prime[NN] = true;
	}
	for(long long i = 2; i < NN; i++) {
		if (is_prime[i] == false) continue;
		for (long long j = i*i; j < NN; j += i) {
			is_prime[j] = false;
		}
	}
}
*/

string generate_random(int size) {
	string s = "1";
	size -= 2;
	FOR(i, size) {
		double aux = (double)rand() / RAND_MAX;
		if (aux <= 0.5) s += "0";
		else s += "1";
	}
	s += "1";
	return s;
}

long long convert(string s, int base) {
	long long num = 0;
	long long mult = 1;
	for(int i = sz(s) - 1; i >= 0; i--) {
		long long val = s[i] - '0';
		val *= mult;
		num += val;
		mult *= base;
	}
	return num;
}

long long divisor_of(long long x) {
	for(long long i = 2; i*i <= x; i++) {
		if (x % i == 0) {
			return i;
		}
	}
	return 0;
}

vector<long long> find(string s) {
	vector<long long> ans;

	for(int base = 2; base <= 10; base++) {
		long long num = convert(s, base);
		long long div = divisor_of(num);
		if (div == 0) {
			return ans;
		}
		ans.pb(div);
	}

	return ans;
}

void solve() {
	int N, J;
	cin >> N >> J;

	map<string, vector<long long> > answers;
	while(answers.size() < J) {
		string s = generate_random(N);
		// cout << "TRYING FOR " << s << endl;
		if (answers.count(s)) continue;
		vector<long long> v = find(s);
		if (sz(v) == 9) {
			answers.insert(mp(s, v));
		}
	}

	cout << endl;
	FOREACH(it, answers) {
		vector<long long> v = (it)->second;
		cout << (it)->first;
		// int base = 2;
		FOREACH(it2, v) {
			cout << " " << (*it2);
			// cout << "(" << convert( (it)->first, base ) << ")  " ;
			// base++;
		}
		cout << endl;
	}
}

int main() {
	// pre_process();
  int num_testes;
	srand (time(NULL));
  scanf("%d", &num_testes);
  for(int t = 1; t <= num_testes; t++) {
    printf("Case #%d: ", t);
    solve();
  }
  return 0;
}
