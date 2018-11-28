#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"
#include "iostream"
using namespace std;
typedef long long i64;


int main() {
	int T; scanf("%d", &T);
	for (int Ti = 1; Ti <= T; ++Ti) {
		fprintf(stderr, "Case #%d of %d...\n", Ti, T);

		string S;
		cin >> S;

		string A;
		for (auto c: S) {
			if (A.empty() || A.front() <= c) {
				A.insert(A.begin(), c);
			} else {
				A.push_back(c);
			}
		}
		
		printf("Case #%d: %s\n", Ti, A.c_str());
	}
	return 0;
}
