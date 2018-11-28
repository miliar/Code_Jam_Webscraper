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
#include "assert.h"
using namespace std;
typedef long long i64;

string A(vector<int>& L, string str, char c, char digit)
{
	string res;
	if (L[c - 'A'] > 0) {
		int cnt = L[c - 'A'];
		res.append(cnt, digit);
		for (auto cc:str) {
			L[cc - 'A'] -= cnt;
		}
	}
	return res;
}

int main() {
	int T; scanf("%d", &T);
	for (int Ti = 1; Ti <= T; ++Ti) {
		fprintf(stderr, "Case #%d of %d...\n", Ti, T);

		string S;
		cin >> S;

		vector<int> L(26);
		for (auto c:S) {
			L[c - 'A']++;
		}
		
		string res;
		res.append(A(L, "ZERO", 'Z', '0'));
		res.append(A(L, "TWO", 'W', '2'));
		res.append(A(L, "SIX", 'X', '6'));
		res.append(A(L, "EIGHT", 'G', '8'));
		res.append(A(L, "THREE", 'T', '3'));
		res.append(A(L, "FOUR", 'U', '4'));
		res.append(A(L, "ONE", 'O', '1'));
		res.append(A(L, "FIVE", 'F', '5'));
		res.append(A(L, "SEVEN", 'S', '7'));
		res.append(A(L, "NINE", 'I', '9'));

		assert(accumulate(L.begin(), L.end(), 0) ==0);
		
		sort(res.begin(),res.end());
		printf("Case #%d: %s\n", Ti, res.c_str());
	}
	return 0;
}
