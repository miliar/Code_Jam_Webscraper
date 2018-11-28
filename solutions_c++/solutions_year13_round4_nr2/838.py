#include <iostream>

using namespace std;

typedef long long i64;

bool byte_set(i64 x, int i) {
	return ((x>>i)&1) != 0LL;
}

bool can_win(i64 x, int N, i64 P) {
	for (int i = N-1; i >= 0; i--) {
		if (!byte_set(P-1,i)) {
			if (x == (1LL<<(i+1)) - 1)
				return false;
			x = (x+1)/2;
		} else {
			if (x != (1LL<<(i+1)) - 1)
				return true;
			x = (x-1)/2;
		}
	}
	return true;
}
bool can_lose(i64 x, int N, i64 P) {
	return can_win((1LL<<N)-1-x, N, (1LL<<N)-P);
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int N;
		i64 P;
		cin >> N >> P;
		i64 max_pos_winner = -1;
		i64 max_cert_winner = -1;
		if (P == (1<<N)) {
			max_pos_winner = P-1;
			max_cert_winner = P-1;
		} else {
			for (i64 i = 0; i < (1LL<<N); i++) {
				if ((max_cert_winner == -1) && can_lose(i,N,P)) {
					max_cert_winner = i-1;
				}
				if (!can_win(i,N,P)) {
					max_pos_winner = i-1;
					break;
				}
			}
		}
		cout << "Case #" << t << ": " << max_cert_winner << " " << max_pos_winner << endl;
	}
	return 0;
} 