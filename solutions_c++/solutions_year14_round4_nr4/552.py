#include <iostream>
#include <iomanip>
#include <stdio.h>
#include <cstdlib>
#include <string>
#include <vector>
#include <algorithm>

#ifdef _WIN32
#define LL "%I64d"
#else
#define LL "%lld"
#endif

#define inp(x) scanf("%d",&x)
#define inpf(x) scanf("%f",&x)

using namespace std;

typedef long long int ll;
typedef long long unsigned int ull;

const int p4[] = {1, 4, 16, 64, 256, 1024, 4096, 16384, 65536};

int T;
int M,N;
string s[8];
int largest;
int lCount;

bool isValid(int i) {
	int cnt[4];

	for (int j = 0; j < N; j++) {
		cnt[j] = 0;
	}

	for (int j = 0; j < M; j++) {
		if (((i >> (2*j)) % 4) >= N)
			return false;
		cnt[(i >> (2*j)) % 4]++;
	}

	for (int j = 0; j < N; j++) {
		if (cnt[j] == 0) {
			return false;
		}
	}
	return true;
}

int nodeCount(int i) {
	int nodeCnt = 0;
	vector<ll> codeArr;

	for (int j = 0; j < N; j++) {
		codeArr.clear();
		for (int k = 0; k < M; k++) {
			if (((i >> (2*k)) % 4) == j) {
				ll code = 0;
				for (int l = 0; l < s[k].length(); l++) {
					code *= 28;
					code += (s[k][l] - 'A' + 1);
					codeArr.push_back(code);
				}
			}
		}

		sort(codeArr.begin(), codeArr.end());
		nodeCnt++;
		for (int j = 1; j < codeArr.size(); j++) {
			if (codeArr[j] != codeArr[j - 1]) {
				nodeCnt++;
			}
		}
	}

	return nodeCnt + N;
}

int main() {

	cin >> T;

	for (int t = 1; t <= T; t++) {
		cin >> M >> N;

		for (int i = 0; i < M; i++) {
			cin >> s[i];
		}

		largest = 0;

		for (int i = 0; i < p4[M]; i++) {
			if (isValid(i)) {
				largest = max(largest, nodeCount(i));
			}
		}

		lCount = 0;
		for (int i = 0; i < p4[M]; i++) {
			if (isValid(i) && nodeCount(i) == largest) {
				lCount++;
			}
		}
		
		cout << "Case #" << t << ": " << largest << " " << lCount << endl;
	}

	return 0;
}
