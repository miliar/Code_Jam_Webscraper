#include <iostream>
#include <string>
#include <cstdlib>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;
typedef long long LL;

int main() {
    std::ifstream fin("A-large.in");

	std::ofstream fout("A-large.out");
//	std::ifstream fin("A-small.in");
//	FILE *fout = freopen("A-small.out", "w", stdout);
	int T;
	string add;
	fin >> T;
	for (int t = 1; t <= T; t++) {
		int start, mul;
		int nums[10];
		for (int i = 0; i < 10; i++)
			nums[i] = 0;
		int count = 10;
		bool outerWhile = true;
		mul = 0;
		fin >> start;
		while (outerWhile) {
			mul++;
			int res = start * mul;
			if (res == 0) {
				add = "INSOMNIA";
				break;
			}
			div_t divresult = div(res, 10);
			while (divresult.rem != 0 || divresult.quot != 0) {
				if (count == 0) {
					ostringstream convert;
					convert << res;
					add = convert.str();
					outerWhile = false;
					break;
				}
				if (!nums[divresult.rem]) {
					count--;
					nums[divresult.rem] = 1;
				}
				divresult = div(divresult.quot, 10);
			}
			if (count == 0) {
				ostringstream convert;
				convert << res;
				add = convert.str();
				outerWhile = false;
				break;
			}
		}
		fout << "Case #" << t << ": ";
		fout << add << endl;
	}
	//exit(0);

	return 0;
}

