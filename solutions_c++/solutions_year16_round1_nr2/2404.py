#include <iostream>
#include <vector>

int lists[100][50];
bool used[100];
int order[50];
int row[50], col[50];
int T, N, r, c, nl;
int c_res[100][100];

bool compare (int li, int ri) {
    if (c_res[li][ri] != 0)
	return c_res[li][ri] < 0;
    int i = 0;
    while (i < N && lists[li][i] < lists[ri][i]) i++;
    if (i == N) {
	c_res[li][ri] = -1;
	c_res[ri][li] = 1;
    }
    else {
	c_res[li][ri] = 1;
	c_res[ri][li] = -1;
    }
    return c_res[li][ri] < 0;
}

bool check_array (int i, int* p, int nth) {
    if (i == -1) return true;
    for (int j = 0; j < nth; j++) {
	if (p[j] == -1) continue;
	if (lists[i][j] != lists[p[j]][nth]) return false;
    }
    return true;
}

bool check_consis (int nth) {
    return check_array (row[nth], col, nth) && check_array(col[nth], row, nth);
}

int main() {
    std::cin >> T;
    int n_case = 1;
    while (T--) {
	std::cin >> N;
	nl = 2*N-1;
	for (int i = 0; i < nl; i++) {
	    for (int j = 0; j < N; j++)
		std::cin >> lists[i][j];
	    std::fill_n (c_res[i], nl, 0);
	}
	std::fill_n (used, nl, false);
	std::fill_n (order, N, 0);
	for (int i = 0; i < N; i++) {
	    r = c = -1;
	    for (int j = 0; j < nl; j++) {
		if (used[j]) continue;
		if (r == -1 && c == -1) {
		    r = j;
		}
		else {
		    if (lists[r][i] < lists[j][i]) continue;
		    else if (lists[r][i] == lists[j][i]) c = j;
		    else {
			r = j;
			c = -1;
		    }
		}
	    }
	    used[r] = true;
	    row[i] = r;
	    col[i] = c;
	    if (c >= 0) {
		used[c] = true;
	    }
	}
	int i = 1, j;
	while (i < N) {
	    if ((row[i] == -1 || row[i-1] == -1 || compare(row[i-1], row[i]))
		&& (col[i] == -1 || col[i-1] == -1 || compare(col[i-1], col[i]))
		&& check_consis(i)) {
		    i++;
	    }
	    else {
		if (order[i] == 0) {
		    std::swap (row[i], col[i]);
		    order[i] = 1;
		}
		else {
		    while (order[i] == 1) {
			order[i] = 0;
			i--;
		    }
		    std::swap (row[i], col[i]);
		    order[i] = 1;
		}
	    }
	}
	int nth, *p;
	for (i = 0; i < N; i++)
	    if (row[i] == -1) {
		nth = i;
		p = col;
		break;
	    }
	for (i = 0; i < N; i++)
	    if (col[i] == -1) {
		nth = i;
		p = row;
		break;
	    }
	std::cout << "Case #" << n_case++ << ":";
	for (i = 0; i < N; i++)
	    std::cout << ' ' << lists[p[i]][nth];
	std::cout << std::endl;
    }

    return 0;
}
