#include <fstream>
#include <iostream>
#include <array>

using namespace std;

FILE *fin, *fout;

bool isFull(std::array<bool,10> ar)
{
	for (int i = 0; i < 10; i++) {
		if (!ar[i]) {
			return false;
		}
	}

	return true;
}



int main()
{
	fopen_s(&fin, "input.txt", "r");
	fopen_s(&fout, "output.txt", "w");

	int t;
	fscanf_s(fin, "%d", &t);

	for (int i = 1; i <= t; i++) {
		char str[101];
		string s;
		fscanf_s(fin, "%s", str, _countof(str));
		s = str;

		char ch = s[0];
		int k = 0;
		for (int i = 0; i < s.length(); i++) {
			if (s[i] != ch) {
				k++;
				ch = s[i];
			}
		}
		if (s[s.length() - 1] == '-') {
			k++;
		}
		
		fprintf_s(fout, "Case #%d: %d\n", i, k);
	}

}