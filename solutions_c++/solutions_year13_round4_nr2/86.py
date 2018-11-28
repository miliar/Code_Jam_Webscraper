#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <cstring>
#include <vector>
using namespace std;
typedef long long int64;
int N;
int64 P;

bool check1(int64 a) {
	//can we make a lose?
	int64 at = 0;
	int64 rem = a; //rem better than a
	for (int i = 0; i < N; ++i) {
		if (rem == 0) {
			//a have to win!
			break;
		}
		//make a into loser team!
		at += 1LL << (N - 1 - i);
		--rem;
		rem /= 2;
	}
	return at <= P;
}

bool check2(int64 a) {
	//can we make a win?
	int64 at = 0;
	int64 rem = (1LL << N) - 1 - a; //rem worse than a
	for (int i = 0; i < N; ++i) {
		if (rem == 0) {
			//a have to lose!
			at += 1LL << (N - 1 - i);
			continue;
		}
		//make a into a winner team!
		--rem;
		rem /= 2;
	}
	return at <= P;
}

void work() {
	cin >> N >> P;
	--P;
	//[0..P] have price
	int64 l = 0, r = (1LL << N);
	while (l + 1 < r) {
		int64 m = (l + r) >> 1;
		if (check1(m))
			l = m;
		else
			r = m;
	}
	cout << l << " ";
	l = 0, r = (1LL << N);
	while (l + 1 < r) {
		int64 m = (l + r) >> 1;
		if (check2(m))
			l = m;
		else
			r = m;
	}
	cout << l << endl;
}

int main() {
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i) {
		printf("Case #%d: ", i);
		work();
	}
	return 0;
}
