#include<cstdio>
#include<bits/stdc++.h>

char str[10];

int orig_tab[4][4];

int tmp_tab[4][4];

bool get_next(int n) {
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < n; ++j) {
			if (orig_tab[i][j]) continue;
			if (tmp_tab[i][j])
				tmp_tab[i][j] = 0;
			else {
				tmp_tab[i][j] = 1;
				return true;
			}
		}
	}
	return false;
}

union occs {
	bool b[4];
	int p;
};

bool is_good(occs m, occs w, int l, int n) {
	if(l >= n) return true;
	bool good = true;
	for (int i = 0; i < n; ++i) {
		if (w.b[i]) continue;
		bool found = false;
		for (int j = 0; j < n; ++j) {
			if (tmp_tab[i][j] && !m.b[j]) {
				m.b[j] = 1;
				w.b[i] = 1;
				good &= is_good(m, w, l+1, n);
				found = 1;
				m.b[j] = 0;
				w.b[i] = 0;
			}
		}
		if (!found) return false;
	}
	return good;
}

int main() {
	int T; scanf("%d", &T);
	for (int _ = 0; _ < T; ++_) {
		int N; scanf("%d", &N);
		for (int i = 0; i < N; ++i) {
			scanf("%s", str);
			for (int j = 0; str[j]; ++j)
				tmp_tab[i][j] = orig_tab[i][j] = str[j] - '0';
		}
		int best_res = N*N*N;
		do {
			occs m, w;
			m.p = 0;
			w.p = 0;
			if (is_good(m, w, 0, N)) {
				int res = 0;
				for (int i = 0; i < N; ++i)
					for (int j = 0; j < N; ++j)
						res += tmp_tab[i][j] - orig_tab[i][j];
				if (res < best_res) best_res = res;
			}
		} while(get_next(N));
		printf("Case #%d: %d\n", _+1, best_res);
	}
	return 0;
}
