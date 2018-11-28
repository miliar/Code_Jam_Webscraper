#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <fstream>

using namespace std;

const int modulo =1000002013;

int n, m;
pair<int, int> val[1 << 15];
pair<int, int> re[1 << 15];

ifstream fin("A-large.in");
ofstream fout("A.large.txt");

int solve(){
	fin >> n >> m;
	long long ret = 0;
	for (int i = 0; i < m; ++i){
		int x, y, p;
		fin >> x >> y >> p;
		ret += (long long)((long long)n + n - (y - x) + 1) * (y - x) / 2  % modulo * p % modulo;
		val[i].first = x;
		val[i].second = -p;
		val[i + m].first = y;
		val[i + m].second = p;
	}
	sort(val, val + m * 2);
	int len = 0, last = 0;
	for (int i = 0; i < m * 2; ++i){
		long long det = val[i].first - last;
		if (det != 0)
			for (int k = 0; k < len; ++k){
				long long tmp = re[k].first;
				tmp = (tmp + tmp - det + 1) * det / 2 % modulo;
				//				cout << "??" << i << " " << tmp << " " << re[k].first << " " << re[k].second << " " << det << endl;
				ret -= tmp * re[k].second % modulo;
				re[k].first -= det;
				ret = (ret + modulo) % modulo;
			}
		else ;
		last = val[i].first;

		if (val[i].second < 0)
			re[len++] = make_pair(n, -val[i].second);
		else {
			int u = -val[i].second;
			while (u < 0){
				if (re[len - 1].second + u < 0){
					u += re[len - 1].second;
					re[len - 1].second = 0;
					--len;
				}
				else {
					re[len - 1].second += u;
					u = 0;
				}
			}
			if (re[len - 1].second == 0)
				--len;
		}
	}
	return (ret + modulo) % modulo;
}

int main(){
	int test = 0;
	fin >> test;
	for (int i = 1; i <= test; ++i)
		fout << "Case #" << i << ": " << solve() << endl;
	return 0;
}