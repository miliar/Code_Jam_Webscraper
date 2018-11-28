#include<algorithm>
#include<cmath>
#include<cstdio>
#include<fstream>
#include<iostream>
#include<map>
#include<set>
#include<string>
#include<utility>
#include<vector>

using namespace std;

int main()
{
	ifstream fin("A-small-attempt.in");
	ofstream fout("A-small-attempt.out");

	int cases, num = 0, den = 0, pos = 0, gen;
	char c;
	std::string frac;

	fin >> cases;

	for(int caseN = 1; caseN <= cases; ++caseN) {
		fout << "Case #" << caseN << ": ";

		fin >> frac;
		while((c = frac[pos++]) != '/') {
			num *=  10;
			num += c - '0';
		}
		while(pos != frac.size()) {
			c = frac[pos];
			den *=  10;
			den += c - '0';
			++pos;
		}

		if((float)den / num == (int)(den / num)) {
			den /= num;
			num = 1;
		}

		while((float)num / 2 == (int)(num / 2) && (float)den / 2 == (int)(den / 2)) {
			num /= 2;
			den /= 2;
		}

	//	cout << num << ' ' << den << '\n';

		if((float)log2(den) != (int)log2(den))
			fout << "impossible";
		else {

			gen = (int)log2(den) - (int)log2(num);

			fout << gen;
		}
		fout << '\n';

		pos = num = den = 0;
	}

	return 0;
}
