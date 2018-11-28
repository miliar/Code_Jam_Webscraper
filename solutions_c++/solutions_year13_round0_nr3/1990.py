#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define DEBUG 0
#define MAX_VAL 10000000 // 10**7

using namespace std;

typedef vector<unsigned long long> VULL;

VULL candidates;
unsigned long long A, B;

bool is_palindrome(string s)
{
	int start = 0, end = s.size() - 1;
	while (start < end) {
		if (s[start++] != s[end--])
			return false;
	}
	return true;
}

void get_candidates()
{
	unsigned long long num, num_square;
	candidates.clear();
	for (num = 1; num <= MAX_VAL; ++num) {
		stringstream num_ss;
		num_ss << num;
		if (is_palindrome(num_ss.str())) {
			stringstream num_2_ss;
			num_square = num * num;
			num_2_ss << num_square;
			if (is_palindrome(num_2_ss.str()))
				candidates.push_back(num_square);
		}
	}
}

void readin()
{
	scanf("%llu%llu\n", &A, &B);
#if DEBUG
	cout << "A: " << A << " B: " << B << endl;
	for (int i = 0; i < candidates.size(); ++i)
		cout << candidates[i] << " ";
	cout << endl;
	cout << "total: " << candidates.size() << endl;
#endif
}

int solve()
{
	int ret = 0;
	VULL::iterator low_A, upp_B;
	low_A = lower_bound(candidates.begin(), candidates.end(), A);
	upp_B = upper_bound(candidates.begin(), candidates.end(), B);
#if DEBUG
	cout << "low_A's idx: " << low_A - candidates.begin() << endl;
	cout << "upp_B's idx: " << upp_B - candidates.begin() << endl;
	cout << "low_A: " << *low_A << " upp_B: " << *upp_B << endl;
#endif
	return upp_B - low_A;
}

int main(int argc, char *argv[])
{
	int case_num = 0;

	scanf("%d\n", &case_num);

	get_candidates();
	for (int case_id = 1; case_id <= case_num; ++case_id) {
		readin();
		cout << "Case #" << case_id << ": ";
		int ret = solve();
		cout << ret << endl;
		cout.flush();
	}

	return 0;
}

