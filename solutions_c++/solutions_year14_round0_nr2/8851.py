#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <stack>
#include <algorithm>
#include <cmath>
#include <queue>
#include <map>
#include <cstdlib>
#include <queue>
#include <set>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <bitset>
#include <sstream>

using namespace std;

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	ios_base::sync_with_stdio(false);
	int test;
	cin >> test;
	for (int t = 0; t < test; ++t) {
		long double c, f, x;
		cin >> c >> f >> x;
		long double min_time = x / 2;
		long double cur_time = 0, cur_recv = 2;
		while (true) {
			cur_time += c / cur_recv;
			cur_recv += f;
			if (min_time >= cur_time + x / cur_recv)
				min_time = cur_time + x / cur_recv;
			else
				break;
		}
		cout << "Case #" << t + 1 << ": " << fixed << setprecision(7) << min_time << endl;
	}
	return 0;
}