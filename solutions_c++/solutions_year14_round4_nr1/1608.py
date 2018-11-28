#include<iostream>
#include<assert.h>
#include<fstream>
#include<vector>
#include<map>
#include<set>
#include<deque>
#include<queue>
#include<functional>
#include<algorithm>
#include<unordered_map>
#include<unordered_set>
#include<cstdlib>
#include<cstring>
#include<cmath>
using namespace std;


int main() {
	int T, N, DS, fs;
	istream & in = cin;
	in >> T;
	int cnt[1000];

	for(int t = 1; t <= T; ++t) {
		in >> N >> DS;
		for(int i = 0; i <= 700; ++i)
			cnt[i] = 0;
		for(int i = 0; i < N; ++i) {
			in >> fs;
			cnt[fs]++;
		}
		int ret = 0;
		for(int i = 700; i >= 1; ) {
			int j;
			if(cnt[i] == 0) {
				i--;
				continue;
			}
			cnt[i]--;
			ret++;
			for(j = DS - i; j >= 1; --j) {
				if(cnt[j] > 0) {
					cnt[j]--;
					break;
				}
			}
		}
		cout << "Case #" << t << ": " << ret << endl;

	}
	return 0;
}

