#include <stdio.h>
#include <functional>
#include <bitset>
#include <math.h>
#include <time.h>
#include <stdlib.h>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <sstream>
#include <queue>
#include <bitset>
#include <string.h>
#include <iomanip>
using namespace std;

int N;
int J;

inline void assert(bool v)
{
	if(!v) 
		throw "ERROR";
}

void readCase()
{
	cin >> N >> J;
}

long long gcd(long long a, long long b) {
	while (b != 0) {
		long long r = a % b;
		a = b;
		b = r;
	}
	return a;
}

long long modmul(long long x, long long y, long long m)
{
	if (y == 0) return 0;
	if (y == 1) return x % m;
	long long temp = modmul(x, y/2, m);
	temp = (2*temp) % m;
	if (y % 2 == 1) {
		temp = (temp + x) % m;
	}
	return temp;
}

long long pollard_rho(long long number) {

	long long x_fixed = 2, cycle_size = 2, x = 2, factor = 1;

	while( factor == 1 ) {

		for( int count = 1; count <= cycle_size && factor <= 1; count++ ) {
			x = modmul(x, x, number);
			x = (x + 1) % number;
			long long d = x - x_fixed;
			if(d < 0) d = -d;
			factor = gcd( d, number);
			assert(factor >= 0);

			if(count > 10000) return 1;
		}

		cycle_size *= 2;
		x_fixed = x;

		assert(x_fixed >= 0);
		assert(cycle_size >= 0);
	}

	return factor;
}

void stupidsolve()
{
	//map<int, string> divides;
	int cnt = 0;
	char buf[256];
	for(int i = (1 << (N - 1)) + 1; i < (1 << N); i += 2) {
		_i64toa(i, buf, 2);
		stringstream str;
		bool valid = true;
		for(int base = 2; base <= 10; base++) {
			long long num = _strtoi64(buf, 0, base);
			long long factor = pollard_rho(num);
			if(factor == 1 || factor == num) {
				valid = false;
				break;
			}
			assert(num % factor == 0);
			str << " " << factor;
		}
		if(valid) {
			//divides[i] = str.str();
			cout << endl << buf << str.str();
			cnt++;
			if(cnt == J) return;
		}
	}

}

int complexsolve()
{
	return 0;
}

void solve()
{
	stupidsolve();
}

int main()
{
	//string fname = "./test/C-example.in";
	string fname = "./test/C-small-attempt0.in";
	//string fname = "./test/C-small-attempt1.in";
	//string fname = "./test/C-small-attempt2.in";
	//string fname = "./test/C-large.in";
	//string fname = "./test/C-large-2.in";

	freopen(fname.c_str(),"r",stdin);freopen((fname+".out").c_str(),"w",stdout);

	int analizeCase = -1;
	
	int T;
	scanf("%d", &T);
	for(int tCase = 1; tCase <= T; tCase++) {
		//printf("Case #%d: ", tCase);
		printf("Case #%d:", tCase);
		readCase();
		if(analizeCase < 0 || analizeCase == tCase) solve();
		printf("\n");
		fflush(stdout);
		fprintf(stderr, "Done %d %%     \r", 100 * tCase / T );
	}
	return 0;
}

