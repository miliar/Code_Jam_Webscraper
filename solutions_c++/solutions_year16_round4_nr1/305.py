#include <bits/stdc++.h>

using namespace std;

template<class T> inline bool _min(T& data, const T& comp) {
	if (comp < data) {
		data = comp;
		return true;
	}
	return false;
}

template<class T> inline bool _max(T& data, const T& comp) {
	if (data < comp) {
		data = comp;
		return true;
	}
	return false;
}

long N, R, P, S;

long d[16][65536];
long cnt[4];

#define C_P 0
#define C_R 1
#define C_S 2

void buildWin(long depth, long pos) {
	if (depth == N + 1) return;
	d[depth + 1][pos << 1] = d[depth][pos];
	d[depth + 1][(pos << 1) + 1] = (d[depth][pos] + 2) % 3;
	buildWin(depth + 1, pos << 1);
	buildWin(depth + 1, (pos << 1) + 1);
}

long diff(long *arr1, long *arr2, long length) {
	while (length --) {
		if (*arr1 != *arr2) return *arr1 - *arr2;
		++ arr1;
		++ arr2;
	}
	return 0;
}

void swap(long *arr1, long *arr2, long length) {
	while (length --) {
		swap(*arr1, *arr2);
		++ arr1;
		++ arr2;
	}
}

void minify(long depth) {
	for(long i = 0; i < depth; ++ i) {
		for (long j = 0; j < (1 << depth); j += (1 << (i + 1))) {
			if (diff(d[depth] + j, d[depth] + j + (1 << i), 1 << i) > 0) {
				swap(d[depth] + j, d[depth] + j + (1 << i), 1 << i);
			}
		}
	}
	for(long i = 0; i < (1 << depth); ++ i) {
		cout << ("PRS"[d[depth][i]]);
	}
	cout << endl;
}

int main(void) {
	ios::sync_with_stdio(false);

	long T;
	cin >> T;
	for (long t = 1; t <= T; ++ t) {
		cin >> N >> R >> P >> S;
		cout << "Case #" << t << ": ";
		d[0][0] = 1;
		buildWin(0, 0);
		memset(cnt, 0, sizeof cnt);
		for (long i = 0; i < (1 << N); ++ i) {
			++ cnt[d[N][i]];
		}
		if (cnt[0] == P && cnt[1] == R && cnt[2] == S) {
			minify(N);
			continue;
		}
		for (long i = 0; i < (1 << N); ++ i) {
			d[N][i] = (d[N][i] + 1) % 3;
		}
		memset(cnt, 0, sizeof cnt);
		for (long i = 0; i < (1 << N); ++ i) {
			++ cnt[d[N][i]];
		}
		if (cnt[0] == P && cnt[1] == R && cnt[2] == S) {
			minify(N);
			continue;
		}
		for (long i = 0; i < (1 << N); ++ i) {
			d[N][i] = (d[N][i] + 1) % 3;
		}
		memset(cnt, 0, sizeof cnt);
		for (long i = 0; i < (1 << N); ++ i) {
			++ cnt[d[N][i]];
		}
		if (cnt[0] == P && cnt[1] == R && cnt[2] == S) {
			minify(N);
			continue;
		}
		cout << "IMPOSSIBLE" << endl;
	}

	return 0;
}
