#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <utility>
#include <string>
#include <bitset>
#include <valarray>
#include <cmath>
#include <climits>
#include <cctype>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <boost/intrusive/rbtree.hpp>
#include <unordered_map>
#include <unordered_set>
#include <regex>
#include <tuple>
#include <cstdint>

using namespace std;

//#define DO_DEBUG 1

#define INFIN 0x3f3f3f3f
#define cin fin
#define cout fout

#define delta 0.000001

int N;
ofstream fout ("d.out");
ifstream fin ("D-large.in");

int main() {
	cin >> N;
	for (int n = 1; n <= N; n++) {
		int B;
		cin >> B;
		float kb[1000], nb[1000];
		for (int i = 0; i < B; i++) cin >> nb[i];
		for (int i = 0; i < B; i++) cin >> kb[i];
		sort(kb, kb + B);
		sort(nb, nb + B);
		int kStart = 0, nStart = 0, kEnd = B-1, nEnd = B-1;
		int deceitfulScore = 0;
		for (int i = 0; i < B; i++) {
			if (nb[nStart] < kb[kStart]) {
				nStart++;
				kEnd--;
			}
			else {
				nStart++;
				kStart++;
				deceitfulScore++;
			}
		}
		kStart = 0, nStart = 0, kEnd = B-1, nEnd = B-1;
		int normalScore = 0;
		for (int i = 0; i < B; i++) {
			if (nb[nStart] > kb[kEnd]) {
				nStart++;
				kStart++;
				normalScore++;
			}
			else {
				float *kBlock = upper_bound(kb + kStart, kb + kEnd, nb[nStart]);
				memcpy(kBlock, kBlock+1, (kb+kEnd-kBlock)*sizeof(float));
				kEnd--;
				nStart++;
			}
		}
		cout << "Case #" << n << ": " << deceitfulScore << ' ' << normalScore << '\n';
	}
	return 0;
}