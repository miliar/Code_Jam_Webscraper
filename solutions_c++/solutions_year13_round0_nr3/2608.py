#include <fstream>
#include <sstream>

using namespace std;

ifstream in("in");
ofstream out("out");

bool pali(int num) {
	string res;
	ostringstream convert;
	
	convert << num;
	
	res = convert.str();

	for (int i = 0; i < res.size()/2; ++i)
		if (res[i] != res[res.size()-1-i])
			return false;

	return true;
}

int main() {
	int t;
	in >> t;
	for (int i = 1; i <= t; ++i) {
		long long a, b, res = 0;

		in >> a >> b;
		for (long long num = 0; num*num <= b; ++num) {
			long long bigNum = num*num;
			if (pali(num) && pali(bigNum) && bigNum >= a)
				++res;
		}

		out << "Case #" << i << ": " << res << "\n";
	}
	return 0;
}
