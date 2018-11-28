#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int getDigit(const long number, int pos)
{
	return (pos == 0) ? number % 10 : getDigit(number / 10, --pos);
}

int _tmain(int argc, _TCHAR* argv[])
{
	const string INSOMNIA = "INSOMNIA";

	ifstream fin("A-small-attempt0.in");
	ofstream fout("A-small-attempt0.out");

	int T;
	string tStr;
	getline(fin, tStr);
	T = atoi(tStr.c_str());

	int A;
	for (int i = 1; i <= T; i++)
	{
		fin >> A;
		int multiple = 1;
		bool bDigit[10] = { 0 };
		bool bComplete = false;

		while (!bComplete) {
			int count = A * multiple++;
			int length = to_string(count).length();

			if (count == 0){
				fout << "Case #" << i << ": " << INSOMNIA << endl;
				break;
			}

			while (length > 0) {
				int r = getDigit(count, --length);
				bDigit[r] = true;
			}

			int order = 0;
			while (bDigit[order++] == true) {
				if (order == 10){
					bComplete = true;
					fout << "Case #" << i << ": " << count << endl;
				}
			}
		}
	}

	fout.close();
	return 0;
}

