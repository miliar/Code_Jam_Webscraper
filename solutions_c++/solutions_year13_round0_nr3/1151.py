#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
using namespace std;

void InitFiles() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
}

vector<long long> pals;
vector<long long> ans;
char buf[100];

long long a[] = {
	1,
	4,
	9,
	121,
	484,
	10201,
	12321,
	14641,
	40804,
	44944,
	1002001,
	1234321,
	4008004,
	100020001,
	102030201,
	104060401,
	121242121,
	123454321,
	125686521,
	400080004,
	404090404,
	10000200001,
	10221412201,
	12102420121,
	12345654321,
	40000800004,
	1000002000001,
	1002003002001,
	1004006004001,
	1020304030201,
	1022325232201,
	1024348434201,
	1210024200121,
	1212225222121,
	1214428244121,
	1232346432321,
	1234567654321,
	4000008000004,
	4004009004004
};

string MyITOA(long long x) {
	string res;
	while (x) {
		res.push_back(x % 10 + '0');
		x /= 10;
	}
	reverse(res.begin(), res.end());
	return res;
}

bool IsPal(long long i) {
	string buf = MyITOA(i);
	int len = buf.size();
	for (int i = 0; i < len / 2; ++i) {
		if (buf[i] != buf[len - 1 - i]) {
			return false;
		}
	}
	return true;
}

void Prebuild() {
	int lim = 10 * 1000 * 1000;
	for (int i = 1; i <= lim; ++i) {
		if (IsPal(i)) {
			pals.push_back(i);
		}
	}

	cout << "long long a[] = {\n";
	for (size_t i = 0; i < pals.size(); ++i) {
		long long x = pals[i] * pals[i];
		if (IsPal(x)) {
			cout << "\t" << x << ",\n";
		}
	}
	cout << "};\n";
}

int Solve() {
	size_t size = sizeof(a) / sizeof(a[0]);

	long long A, B;
	cin >> A >> B;
	int res = 0;
	for (size_t i = 0; i < size; ++i) {
		if (A <= a[i] && a[i] <= B) {
			res++;
		}
	}
	return res;
}

int main()
{
	InitFiles();
	//Prebuild();

	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; ++i) {
		printf("Case #%d: %d\n", i + 1, Solve());
	}
	return 0;
}