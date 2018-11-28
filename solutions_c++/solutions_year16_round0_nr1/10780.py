#include <string>
#include <fstream>
#include <iostream>

using namespace std;

bool digit[10];

bool numb(long long a)
{
	string str = to_string(a);
	//cout << str;
	//getchar();
	for (int i = 0; i < str.size(); ++i) {
		if (digit[str[i] - 48] == false) digit[str[i] - 48] = true;
	}

	for (int i = 0; i < 10; ++i) {
		if (digit[i] == false) return false;
	}
	return true;
}

int main() {

	ifstream fin("A-large.in");
	ofstream fout("output.out");

	int t, k = 2;
	fin >> t;
	for (int j = 0; j < t; ++j) {
		long long num;
		fin >> num;

		for (int i = 0; i < 10; ++i) digit[i] = false;
		k = 1;
		if (num == 0) fout << "Case #" << j + 1 << ": INSOMNIA" << endl;
		else {
			while (!numb(num * k)) {
				k++;
			}
			fout << "Case #" << j + 1 << ": " << num * k << endl;
		}

	}
	fin.close();
	fout.close();
	return 0;
}