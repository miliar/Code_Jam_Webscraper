#include <cstring>
#include <functional>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <fstream>
#include <iostream>
#include <sstream>
#include <cmath>
#include <cctype>
#include <iomanip>
#include <queue>
#include <ctime>
#include <assert.h>
using namespace std;

#define D(x) cerr << x << endl;
//#undef D
//#define D(x)

#ifdef _WIN32
#define LL _int64
#else
#define LL long long
#endif



int main()
{
	clock_t start, finish;
	start = clock();

	ifstream inp("2015_Qual_A.in");
	ofstream outp("2015_Qual_A.out");

	/////////////////////////////////////

	int t;
	inp >> t;

	for (int i = 0; i < t; i++) {
		int Smax;
		string s;
		inp >> Smax >> s;
		
		int prev = 0;
		int res = 0;
		for (int j = 0; j <= Smax; j++) {
			int cur = s[j] - '0';
			if (j > 0 && prev < j && cur > 0) {
				int add = j - prev;
				res += add;
				prev += add;
			}
			prev += cur;
		}

		outp << "Case #" << i + 1 << ": " << res << endl;
	}


	/////////////////////////////////////

	inp.close();
	outp.close();

	finish = clock();
	double duration = (double)(finish - start) / CLOCKS_PER_SEC;
	D("Duration: " << duration << endl);

	return 0;
}
