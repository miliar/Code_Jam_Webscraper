// 2013A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <algorithm>
#include <vector>

using namespace std;

int test(int a, int n, vector<int> motes);

int _tmain(int argc, _TCHAR* argv[])
{
	ios_base::sync_with_stdio(false);

	ifstream in("A.in");
	ofstream out("A.out");

	int t;
	in >> t;

	for (int c = 1; c <= t; c++) {
		int a, n;
		in >> a >> n;

		vector<int> motes(n);
		for (int i = 0; i < n; i++) {
			in >> motes[i];
		}

		sort(motes.begin(), motes.end());

		int res = test(a, n, motes);
		out << "Case #" << c << ": " << res << endl;
	}

	return 0;
}

int test(int a, int n, vector<int> motes)
{
	int sum = a;
	int pos = 0;
	int count = 0;

	while (pos < n) {
		if (sum > motes[pos]) {
			sum += motes[pos];
			pos++;
		
		} else {
			int t = 0;
			int q = sum;
			while (true) {
				if (t >= n-pos) {
					return count+n-pos;
				} else if (q > motes[pos]) {
					break;
				} else {
					q += q-1;
					t++;
				}
			}
			count += t;
			sum = q;
		}
	}

	return count;
}