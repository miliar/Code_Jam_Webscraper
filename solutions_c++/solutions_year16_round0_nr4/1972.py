#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

typedef unsigned long long int ll;
ll K, C, S, T;
ifstream fin("frac.in");
ofstream fout("frac.out");

int main() {
	fin >> T;
	for (int t = 1; t <= T; t++) {
		fin >> K >> C >> S;

		vector<ll> v(K + ((C - (K % C)) % C), 0);
		for (int i = 0; i < K; i++)
			v[i] = i;

		vector<ll> out;
		for (int i = 0; i < v.size(); i += C) {
			ll acc = 0;
			for (int j = 0; j < C; j++) {
				acc *= K;
				acc += v[i + j];
			}
			out.push_back(acc);
		}

		fout << "Case #" << t << ":";
		if (out.size() > S)
			fout << " IMPOSSIBLE";
		else
			for (ll x : out)
				fout << " " << x+1;
		fout << endl;
	}
}
