#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <fstream>
#include <cstdint>
using namespace std;

int main()
{
	fstream f_in("A-large.in", fstream::in);
	fstream f_out("A-large.out", fstream::out);
	FILE* file_out;
	fopen_s(&file_out, "a.out", "w");
	int n;
	f_in >> n;
	for (int i = 0; i < n; ++i) {
		int d;
		f_in >> d;
		if (d == 0) {
			f_out << "Case #" << i + 1 << ": INSOMNIA\n";
			//fprintf(file_out, "Case #%d: INSOMNIA\n", i + 1);
			continue;
		}
		vector<bool> digits(10, false);
		for (int64_t j = 1;; ++j) {
			int64_t r = d * j;
			cout << r << " ";
			while (r != 0) {
				digits[r % 10] = true;
				r /= 10;
			}
			bool flag = true;
			for (int k = 0; k < 10; ++k) {
				if (!digits[k]) {
					flag = false;
					break;
				}
			}
			if (flag) {
				f_out << "Case #" << i + 1 << ": " << d * j << "\n";
				//fprintf(file_out, "Case #%d: %lld\n", i + 1, j);
				break;
			}
		}
		cout << "\n";
	}
	system("pause");
	return 0;
}