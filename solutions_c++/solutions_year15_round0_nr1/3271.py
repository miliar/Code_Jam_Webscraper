/*************************************************************************
	> Author: Wayne Ho
	> Purpose: TODO
	> Created Time: Sat Apr 11 22:43:13 2015
	> Mail: hewr2010@gmail.com 
 ************************************************************************/
#include <iostream>
#include <fstream>
#include <cstdio>
using namespace std;

int main(int argc, char **argv) {
	freopen("a-large.in", "r", stdin);
	int Cases;
	cin >> Cases;
	for (int Case = 1; Case <= Cases; ++Case) {
		int Smax;
		string buf;
		cin >> Smax >> buf;
		int ans(0), now(buf[0] - '0');
		for (int i = 1; i <= Smax; ++i) {
			int tmp = buf[i] - '0';
			if (now < i) {
				ans += i - now;
				now = i + tmp;
			} else {
				now += tmp;
			}
		}
		cout << "Case #" << Case << ": " << ans << endl;
	}

    return 0;
}

