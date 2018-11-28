#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <queue>

using namespace std;

int findmax(const string& s, int start, int end)
{
	int m = start;
	for (int i = start; i < end; i++) {
		if (s[i] > s[m]) {
			m = i;
		}
	}
	return m;
}

void process_substr(string& s, int start, int end)
{
	if (start >= end) return;
	int m = findmax(s, start, end);
	string smax;
	string sless;
	int countmax = 0;
	for (int i = start; i < end; i++) {
		if (s[i] == s[m]) {
			smax.append(1, s[i]);
			countmax++;
		} else {
			sless.append(1, s[i]);
		}
	}
	for (int i = start; i < start + countmax; i++) {
		s[i] = smax[i - start];
	}
	for (int i = start + countmax; i < end; i++) {
		s[i] = sless[i - start - countmax];
	}
	process_substr(s, start + countmax, m + countmax);
}

void test()
{
	string S;
	cin >> S;
	process_substr(S, 0, S.length());
	cout << S;
}

int main()
{
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		cout << "Case #" << i + 1 << ": ";
		test();
		cout << endl;
	}
	return 0;
}
