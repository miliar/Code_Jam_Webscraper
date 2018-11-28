#include <iostream>
#include <fstream>
using namespace std;

long long MaxY(long long a,long long b) {
	long long max = a>b? a: b;
	long long min = a<b? a: b;
	return (max%min==0)? min: MaxY(min, max%min);
} 

int dfs(long long n, long long m, int depth) {
	if (depth > 40) return 0;
	long long y = MaxY(n, m);
	n /= y;
	m /= y;
	n <<= 1;
	while (n < m) {
		++depth;
		n <<= 1;
	}
	if (n == m) return depth; 
	if (dfs(n-m, m, depth+1)) return depth;
	return 0;
}

int main() {
	ifstream fin("A-large.in");
	ofstream fout("output.txt");
	int T;
	fin >> T;
	for (int i=0; i<T; ++i) {
		long long n = 0, m = 0;
		char s;
		fin >> n >> s >> m;
		int res = dfs(n, m, 1);
		if (res) fout << "Case #" << i+1 << ": " << res << endl;
		else fout << "Case #" << i+1 << ": impossible" << endl;
	}
	return 0;
}
