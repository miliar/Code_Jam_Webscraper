#include <fstream>
#include <iostream>
#include <cstring>

int T;
int size;

int findZero(int num) {
	for (int i = size - 1; i >= 0; i--) {
		if (((1 << i) | num) != num) return i;
	}
}

int findOne(int num) {
	for (int i = size - 1; i >= 0; i--) {
		if (((1 << i) | num) == num) return i;
	}
}

void change(int &num, int n, int ch) {
	for (int i = n; i <= size - 1; i++) {
		num ^= (1 << i);
	}
}

int Calculate(int num) {
	int res = 0;

	while (num != 0) {
		if ((num + 1) == (1 << size)) return res + 1;

		if (num >= (1 << (size - 1))) {
			int index = findZero(num);
			change(num, index + 1, 0);
		}
		else {
			int index = findOne(num);
			change(num, index + 1, 1);
		}
		res++;
	}
	return res;
}

int main() {
	std::ifstream fin("B-small-attempt0.in");
	std::ofstream fout("output.out");

	if (!fin.is_open() || !fout.is_open()) return 1;
	fin >> T;
	//scanf("%d", &T);

	for (int t = 1; t <= T; t++) {
		char str[12];
		int curr = 0;
		fin >> str;
//		scanf("%s", str);

		size = strlen(str);
		for (int i = 0; i < size; i++) {
			if (str[i] == '-') 
				curr |= (1 << (size - 1 - i));
		}
		
		fout << "Case #" << t << ": " << Calculate(curr) << "\n";
//		printf("Case #%d: %d\n", t, Calculate(curr));
	}
}
