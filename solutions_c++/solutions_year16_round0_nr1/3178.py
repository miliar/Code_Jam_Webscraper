#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>
#include <bitset>


using namespace std;

bitset<100000000> visited;
bitset<10> dig;

void extract(int n) {

	while (n > 0) {
		int d = n % 10;
		dig[d] = true;
		n /= 10;
	}

}

bool check() {
	for (int i = 0; i < 10; i++) {
		if (!dig[i]) return false;
	}

	return true;
}

int solve(int n) {
	visited.reset();
	dig.reset();
	extract(n);
	visited[n] = true;
	int p = 2;
	int cur = 0;

	while (!check()) {
		cur = p * n;
		p++;
		if (visited[cur]) {
			return -1;
		}

		visited[cur] = true;
		extract(cur);
	}

	return cur;
}

int main() {

	ifstream in ("in.txt");
	ofstream out ("out.txt");

	int T; in >> T;

	for (int i = 1; i <= T; i++) {

		int n; in >> n;
		int res = solve(n);
		if (res > 0)
			out << "Case #" << i << ": " << res << endl;
		else
			out << "Case #" << i << ": " << "INSOMNIA" << endl;
	}


	in.close();
	out.close();
	return 0;
}
