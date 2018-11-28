#include <fstream>
#include <iostream>
#include <cstring>

int T;
int result[11];

bool finished() {
	for (int i = 0; i < 10; i++)
		if (result[i] == 0) return false;
	return true;
}

void fill(long long int res) {
	while (res > 0) {
		result[res % 10] = 1;
		res /= 10;
	}
}
long long int Calculate(int num) {
	long long int res;
	for (res = num; !finished(); res += num) {
		fill(res);
	}
	return res-num;
}

int main() {
	std::ifstream fin("A-large.in");
	std::ofstream fout("output.out");

	if(!fin.is_open() || !fout.is_open()) return 1;
	fin >> T;
	//scanf("%d", &T);

	for (int t = 1; t <= T; t++) {
		memset(result, 0, sizeof(result));
		int num = 0;
		fin >> num;
		//scanf("%d", &num);

		if (num == 0) fout << "Case #" << t << ": INSOMNIA\n"; //printf("Case #%d: INSOMNIA\n", t);
		else fout << "Case #" << t << ": " << Calculate(num) << "\n";
		//printf("Case #%d: %lld\n", t, Calculate(num));
	}
}