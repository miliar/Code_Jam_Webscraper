#include <algorithm>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <deque>
#include <iostream>
#include <limits>
#include <numeric>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
#include <complex>
#include <time.h>

#define M_PI           3.14159265358979323846

using namespace std;

#define MP make_pair
#define all(v) (v).begin(), (v).end()
#define PROBLEM_ID "1"

#pragma comment(linker, "/STACK:56777216")

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<bool> vb;
typedef pair<int, int> pii;

vi GetBits(const string& pan) {
	vi res(pan.length());
	for (int i = 0; i < pan.length(); ++i) {
		if (pan[i] == '+') {
			res[i] = 1;
		}
	}
	return res;
}

int GetNum(const vi& bits) {
	int res = 0;
	for (int i = 0; i < bits.size(); ++i) {
		if (bits[bits.size() - 1 - i] == 1) {
			res += 1 << i;
		}
	}
	return res;
}

vi GetVec(int num, int len) {
	vi res(len);
	int i = 0;
	while (num != 0) {
		int bit = num % 2;
		num = num / 2;
		res[len - i - 1] = bit;
		i++;
	}
	return res;
}

vi Inverse(const vi& bits, int top) {
	vi res = bits;
	for (int i = 0; i < top; ++i) {
		res[top - i - 1] = 1 - bits[i];
	}
	return res;
}

vvi MakeStep(vvi& bits, vi& res, int newSteps) {
	vvi newBits;

	for (auto& b : bits) {
		for (int i = 1; i <= b.size(); ++i) {
			vi inverse = Inverse(b, i);
			int num = GetNum(inverse);
			if (res[num] == -1) {
				res[num] = newSteps;
				newBits.push_back(inverse);
			}
		}
	}
	return newBits;
}

vi GetCounts(int len) {
	vi res((1 << len), -1);
	
	vvi bits(1, vi(len, 1));
	int steps = 0;

	res[GetNum(bits[0])] = steps;

	vvi nextBits = MakeStep(bits, res, steps + 1);
	while (!nextBits.empty()) {
		steps++;
		nextBits = MakeStep(nextBits, res, steps + 1);
	}
	return res;
}

int main() {
	freopen(PROBLEM_ID".in", "r", stdin);
	freopen(PROBLEM_ID".out", "w", stdout);
	
	//vi x = Inverse({ 1, 0, 1, 1, 0, 0 }, 3);
	//int num = GetNum({ 0, 1, 1 });
	//vi v = GetVec(3, 6);

	int t;
	cin >> t;
	string pan;
	getline(cin, pan);
	for (int i = 0; i < t; ++i) {
		getline(cin, pan);

		int len = pan.length();
		vi counts = GetCounts(len);

		cout << "Case #" << i + 1 << ": " << counts[GetNum(GetBits(pan))] << endl;
	}

	return 0;
}