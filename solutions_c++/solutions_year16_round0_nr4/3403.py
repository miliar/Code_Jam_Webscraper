#include <cstdio>
#include <queue>
#include <string>
#include <utility>
#include <iostream>
#include <cmath>
#include <fstream>

using namespace std;
typedef long long ll;

int main() {
	ifstream in;
	ofstream out;
	in.open("input.txt");
	out.open("output.txt");
	int T;
	in >> T;
	for (int t = 0; t < T; t++) {
		out << "Case #" << t + 1 << ": ";
		int k, c, s;
		in >> k >> c >> s;
		if (k == s) {
			ll len = pow(k, c);
			ll prev = -1;
			for (ll i = 0; i < s; i++) {
				ll num = len / k * i + 1;
				if (num != prev) out << num << " ";
				prev = num;
			}
		}
		out << endl;
		
	}
}
