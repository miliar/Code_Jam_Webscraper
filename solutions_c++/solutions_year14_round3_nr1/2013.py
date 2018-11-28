#include <string>
#include <vector>
#include <iostream>
#include <fstream>
#include <set>
#include <algorithm>
#include <map>

using namespace std;

//#define GEN_LOCAL_TEST
#define USE_LOCAL_TEST

#ifdef GEN_LOCAL_TEST
void genTest() {
	ofstream ofs("test.txt", ifstream::out);
	int n = 100000;
	ofs << n << endl;
	for (int i = 0; i < n; ++i)
		ofs << 0 << " ";
	ofs << endl;
	ofs.close();
}
#endif

void funcTrunc(long long int & p, long long int & q) {
	for (long long int j = 1; j*j <= p; ++j) {
		if (p % j != 0) continue;
		long long int dv = p / j;
		if (q % j == 0) {
			p /= j;
			q /= j;
		}
		if (p % dv == 0 && q % dv == 0) {
			p /= dv;
			q /= dv;
		}
	}
}

int main(int argc, char* argv[])
{
#ifdef GEN_LOCAL_TEST
	genTest();
#endif

	int n;
#ifdef USE_LOCAL_TEST
	ifstream ifs("test.txt", ifstream::in);
	ifs >> n;
#else
	cin >> n;
#endif
	ofstream ofs("ans.txt", ifstream::out);
	long long int p, q;
	char c;
	vector<int> x, y;
	for (int i = 0; i < n; ++i) {
#ifdef USE_LOCAL_TEST
		ifs >> p >> c >> q;
#else
		cin >> p >> c >> q;
#endif
		funcTrunc(p, q);
		long long int mult = 2;
		int qt = 1;
		int res = -1;
		while (qt <= 40 && p > 0)  {
			while (q > p*mult && qt <= 40) {
				mult *= 2;
				++qt;
			}
			if (qt > 40) break;
			if (res == -1) res = qt;
			long long int tmp = mult;
			p = p*tmp - q;
			funcTrunc(p, q);
			funcTrunc(p, tmp);
			q = q*tmp;
			funcTrunc(p, q);
		}
		if (p > 0) res = -1;
		ofs << "Case #" << i + 1 << ": ";
		if (res == -1)
			ofs << "impossible" << endl;
		else
			ofs << res << endl;
	}

	return 0;
}

