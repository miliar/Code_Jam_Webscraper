#include <iostream>
#include <fstream>
#include <sstream>
#include <set>
#include <map>
#include <vector>
#include <deque>
#include <queue>
#include <list>
#include <algorithm>


using namespace std;


int missR = -1;
int missC = -1;

bool fit (const std::vector<int>& b,
			 const std::vector<int>& a,
			 int r)
{
	bool f = true;
	for (int i = 0; i < r; ++i) {
		if (b[i] != 0 && a[i] != b[i]) {
			f = false;
			break;
		}
	}
	return f;
}

bool fitC (const std::vector<vector<int> >& b,
			  const std::vector<int>& a,
			  int r)
{
	for (int i = 0; i < r; ++i) {
		if (b[i][r] != 0 && b[i][r] != a[i]) {
			return false;
		}
	}
	return true;
}

bool
solve(const std::vector<vector<int> >& a,
		std::vector<vector<int> >& b,
		std::set<int>& used,
		int r, int N)
{
//	std::cout << "-------------" << endl;
//	for (int i = 0; i < N; ++i) {
//		for (int j = 0; j < N; ++j) {
//			std::cout << b[i][j] << ' ';
//		}
//		std::cout << endl;
//	}


	if (r == N) {
		return true;
	}

	int m = 3000;
	int c = 1;
	int w[2];
	for (int i = 0; i < 2 * N - 1; ++i) {
		if (used.find(i) != used.end()) {
			continue;
		}

		if (a[i][r] < m) {
			m = a[i][r];
			c = 1;
			w[0] = i;
		}
		else if (a[i][r] == m) {
			++c;
			w[1] = i;
		}
	}

	if (c == 2) {
		bool fit1 = fit(b[r], a[w[0]], r) && fitC(b, a[w[1]], r);
		bool fit2 = fit(b[r], a[w[1]], r) && fitC(b, a[w[0]], r);

		if (!fit1 && !fit2) {
			return false;
		}

		used.insert(w[0]);
		used.insert(w[1]);

		std::vector<int> c0(N);
		std::vector<int> c1(N);
		for (int i = 0; i < N; ++i) {
			c0[i] = b[r][i];
			c1[i] = b[i][r];
		}

		bool res = false;
		if (fit1) {
			for (int i = 0; i < N; ++i) {
				b[r][i] = a[w[0]][i];
				b[i][r] = a[w[1]][i];
			}
			res = solve(a, b, used, r + 1, N);
		}

		if (!res && fit2) {
			for (int i = 0; i < N; ++i) {
				b[r][i] = c0[i];
				b[i][r] = c1[i];
			}

			for (int i = 0; i < N; ++i) {
				b[r][i] = a[w[1]][i];
				b[i][r] = a[w[0]][i];
			}
			res = solve(a, b, used, r+1, N);
		}

		if (!res) {
			for (int i = 0; i < N; ++i) {
				b[r][i] = c0[i];
				b[i][r] = c1[i];
			}
			used.erase(w[0]);
			used.erase(w[1]);
			return false;
		}
	}

	if (c == 1) {
		bool fit1 = fit(b[r], a[w[0]], r);
		bool fit2 = fitC(b, a[w[0]], r);

		if (!fit1 && !fit2)
			return false; //NO

		std::vector<int> c0(N);
		std::vector<int> c1(N);
		for (int i = 0; i < N; ++i) {
			c0[i] = b[r][i];
			c1[i] = b[i][r];
		}

		used.insert(w[0]);
		bool res = false;
		if (fit1) {
			for (int i = 0; i < N; ++i) {
				b[r][i] = a[w[0]][i];
			}
			missR = -1;
			missC = r;

//std::cout << "R " << missR << " C " << missC << endl;

			res = solve(a, b, used, r + 1, N);

			if (!res) {
				for (int i = 0; i < N; ++i) {
					b[r][i] = c0[i];
				}
			}
		}

		if (!res && fit2) {
			for (int i = 0; i < N; ++i) {
				b[i][r] = a[w[0]][i];
			}
			missC = -1;
			missR = r;

//std::cout << "R " << missR << " C " << missC << endl;
			res = solve(a, b, used, r+1, N);

			if (!res) {
			 	for (int i = 0; i < N; ++i) {
				 	b[i][r] = c1[i];
				}
			}
		}

		if (!res) {
			used.erase(w[0]);
			return false;
		}
	}

	return true;
}





int main(int argc, char* argv[])
{
	std::ifstream infile("infile.txt");
	std::ofstream outfile("outfile.txt");

	int T = 0;
	infile >> T;

	for (int t = 1; t <= T; ++t) {
		int N = 0;
		infile >> N;

		vector<vector<int> > a;
		vector<vector<int> > b;
		for (int i = 0; i < N; ++i) {
			a.push_back(vector<int>(N, 0));
			b.push_back(vector<int>(N, 0));
			for (int j = 0; j < N; ++j) {
				infile >> a[i][j];
			}
		}
		for (int i = 0; i < N - 1; ++i) {
			a.push_back(vector<int>(N, 0));
			for (int j = 0; j < N; ++j) {
				infile >> a[N + i][j];
			}
		}

		std::set<int> used;
		bool s = solve(a, b, used, 0, N);

		std::vector<int> ans(N, 0);
		if (s) {
			if (missR >= 0) {
				for (int i = 0; i < N; ++i) {
					ans[i] = b[missR][i];
				}
			}
			else if (missC >= 0) {
				for (int i = 0; i < N; ++i) {
					ans[i] = b[i][missC];
				}
			}
		}



		outfile << "Case #" << t << ":";
		for (int i = 0; i < N; ++i) {
			outfile << ' ' << ans[i];
		}
		outfile << std::endl;

//		int mmm;
//		std::cin >> mmm;
	}

	return 0;
}
