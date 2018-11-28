#include <iostream>
#include <fstream>
#include <algorithm>
#include <iomanip>
#include <cmath>

using namespace std;

int t;
long double cur_c, cur_r, c, f, x, t_t;

int main() {
	ifstream fin ("B-large.in");
	ofstream fout ("cc.out");
	fin >> t;
	for (int i = 1; i <= t; i++) {
		t_t = 0.0;
		cur_c = 0.0;
		cur_r = 2.0;
		fin >> c >> f >> x;
		while (cur_c < x) {
			long double b_farm = c - cur_c;
			long double b_farm_t = b_farm / cur_r;
			cur_c += c;
			t_t += b_farm_t;
			long double t_left = (x - cur_c) / cur_r;
			long double t_farm = (x - cur_c + c) / (cur_r + f);
			if (t_farm < t_left) {
				cur_c -= c;
				cur_r += f;
			}
			else
				break;
		}
		t_t += (x-cur_c) / cur_r;
		int log_t = (int) log(t_t);
		fout << "Case #" << i << ": " << setprecision(log_t + 7) << t_t << endl;
	}
}
