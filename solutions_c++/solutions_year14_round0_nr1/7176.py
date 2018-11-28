#include <iostream>
#include <set>
using namespace std;

const char *Output[] = {
	"Bad magician!",
	"Volunteer cheated!"
};

int matrix[2][4][4];
int select[2];

int solve() {
	int cnt = 0;
	int tar = 0;
	set<int> rember;

	for (int i = 0; i < 4; ++i) {
		rember.insert(matrix[0][select[0]][i]);
	}
	for (int i = 0; i < 4; ++i) {
		if (rember.find(matrix[1][select[1]][i]) != rember.end()) {
			tar = matrix[1][select[1]][i];
			++cnt;
		}
	}
	if (cnt == 1) {
		return tar;
	} else if (cnt == 0) {
		return 18;
	} else {
		return 17;
	}
}

int dataset;

void read() {
	for (int i = 0; i < 2; ++i) {
		cin >> select[i];
		--select[i];
		for (int a = 0; a < 4; ++a){
			for (int b = 0; b < 4; ++b) {
				cin >> matrix[i][a][b];
			}
		}
	}
}

int main() {
	scanf("%d", &dataset);
	for (int cas = 1; cas <= dataset; ++cas) {
		read();
		printf("Case #%d: ", cas);
		int ret = solve();
		if (ret > 16) {
			cout << Output[ret - 17] << endl;
		} else {
			cout << ret << endl;
		}
	}

	return 0;
}
