#include <string>
#include <algorithm>
#include <numeric>
#include <fstream>

using namespace std;

int main() {
	ofstream fout ("A-large.out");
	ifstream fin ("A-large.in");
	int n = 0, cases = 0;
	fin >> cases;
	for(int c = 1; c <= cases; c++) {
        fin >> n;
        if(n == 0)
			fout << "Case #" << c <<": INSOMNIA" << endl;
        else {
			int digits[10] = {false};
			int multiples = 0;
			int counter = 1;
			string listnums;
			bool allGood = false;
			while(!allGood) {
				int cnt = 0;
				multiples = counter * n;
				listnums = to_string(multiples);
				for(char &num : listnums) {
					digits[num - '0'] = true;
				}
				for(int i = 0; i < 10; i++) {
					if(digits[i] == true)
						cnt++;
				}
				if(cnt == 10)
					allGood = true;
				counter++;
			}
			fout << "Case #" << c << ": " << multiples << endl;
        }
    }
    return 0;
}