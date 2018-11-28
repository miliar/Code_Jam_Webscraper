#include <iostream>
#include <string>

#define INF 1000000000

using namespace std;

int tests, n, m, answer;
int dx, dy;
string p[101];

int main() {
    cin >> tests;
    for (int test = 0 ; test < tests ; test ++) {
        cin >> n;
	cin >> m;
        for(int i = 0 ; i < n ; i ++) {
            cin >> p[i];
        }
        answer = 0;
        for (int i = 0 ; i < n ; i ++) {
	    for (int j = 0 ; j < m ; j ++) {
		dx = 0;
		dy = 0;
		if (p[i][j] == '^') {
		    dx = -1;
		} else if (p[i][j] == '>') {
		    dy = 1;
		} else if (p[i][j] == 'v') {
		    dx = 1;
		} else if (p[i][j] == '<') {
		    dy = -1;
		} else {
		    continue;
		}
		int tmp = 1;
		int ii = i + dx, jj = j + dy;
		while (ii >= 0 && jj >= 0 && ii < n && jj < m) {
		    if (p[ii][jj] != '.') {
			tmp = 0;
			break;
		    }
		    ii += dx;
		    jj += dy;
		}
		if (tmp == 0) {
		    continue;
		}
		answer += tmp;
		tmp = 0;
		if (tmp == 0) {
		    for (int q = 0 ; q < m ; q ++) {
			if (q != j && p[i][q] != '.') {
			    tmp = 1;
			    break;
			}
		    }
		    if (tmp == 0) {
			for (int q = 0 ; q < n ; q ++) {
			    if (q != i && p[q][j] != '.') {
				tmp = 1;
				break;
			    }
			}
			if (tmp == 0) {
			    answer = INF;
			}
		    }
		}
	    }
        }
        cout << "Case #" << test + 1 << ": ";
	if (answer >= INF) {
	    cout << "IMPOSSIBLE" << endl;
	} else {
	    cout << answer << endl;
	}
    }
    return 0;
}
