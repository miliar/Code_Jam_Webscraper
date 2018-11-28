#include <bits/stdc++.h>

#define pb push_back
#define f first
#define s second
#define pii pair<int, int>
#define mp make_pair
 
using namespace std;
 
const string name = "A",
             in_file = name + ".in",
             out_file = name + ".out";
 
ifstream fin(in_file);
ofstream fout(out_file);

int tests, v[10];
long long n;

void get_digits(long long nr) {
	do {
		v[nr % 10] = 1;
		nr /= 10;
	} while (nr);
}

bool check() {
	for (int i = 0; i < 10; i++)
		if (!v[i])
			return true;
	return false;
}

int main() {
	fin >> tests;
	for (int i = 1; i <= tests; i++) {
		fin >> n;
		
		memset(v, 0, sizeof(v));
		if (n == 0) {
			fout << "Case #" << i << ": INSOMNIA\n";
			continue;
		}

		long long nr = n;

		for (; check(); nr += n)  
			get_digits(nr);
		
		fout << "Case #" << i << ": " << nr - n << '\n';
	}
	
	return 0;
}