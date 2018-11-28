#include<fstream>
#include<iostream>

using namespace std;

int main(int argc, char **argv) {
	ifstream f(argv[1]);
	int case_num;
	f >> case_num;
	case_num++;
	int b[100][100];
	for (int i = 1; i < case_num; ++i) {
		int n, m;
		f >> n;
		f >> m;
		n--;
		m--;
		for (int p = 0; p <= n; ++p) {
			for (int q = 0; q <= m; ++q) {
				f >> b[p][q];
			}
		}
		bool is_legal = true;
		for (int p = 0; p <= n; ++p) {
			for (int q = 0; q <= m; ++q) {
				if (b[p][q] == 1) {
					bool is_leg1 = true;
					bool is_leg2 = true;
					for (int k = 0; k <= n; ++k) {
						if (b[k][q] > 1) {
							is_leg1 = false;
							break;
						}
					}
					for (int k = 0; k <= m; ++k) {
						if (b[p][k] > 1) {
							is_leg2 = false;
							break;
						}
					}
					if (!(is_leg1 || is_leg2)) {
						is_legal = false;
						break;
					}
				}
			}
			if (!is_legal) {
				break;
			}
		}
		if (!is_legal) {
			cout << "Case #" << i << ": NO" << endl;
		} else {
			cout << "Case #" << i << ": YES" << endl;
		}
	}
	return 0;
}
