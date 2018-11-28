#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
string ansa, ansb;
long long ansd;

long long diff(string sa, string sb, int l) {
	long long ans = 0;
	for (int i = 0; i < sa.size(); i ++) {
		if (i < l) {
			ans += (sa[i] - sb[i]);
		}
		ans *= 10;
	}
	if (ans < 0) ans = -ans;
	return ans;
}

void update(string & sa, string & sb) {
	long long dif = diff(sa, sb, sa.size());
	if (ansd < 0 || dif < ansd || (dif == ansd && sa < ansa) || (dif == ansd && sa == ansa && sb < ansb)) {
		ansd = dif;
		ansa = sa;
		ansb = sb;
	}
}

void search(int i, string sa, string sb) {
	if (i == sa.size()) {
		update(sa, sb);
		return ;
	}
	if (sa[i] == '?') {
		if (sb[i] == '?') {
			sa[i] = '0';
			sb[i] = '0';
			search(i + 1, sa, sb);
			sb[i] = '1';
			search(i + 1, sa, sb);
			sb[i] = '9';
			search(i + 1, sa, sb);
			sb[i] = '0';
			sa[i] = '1';
			search(i + 1, sa, sb);
			sa[i] = '9';
			search(i + 1, sa, sb);
		} else {
			sa[i] = sb[i];
			search(i + 1, sa, sb);
			sa[i] = ((sb[i] - '0') + 9) % 10 + '0';
			search(i + 1, sa, sb);
			sa[i] = ((sb[i] - '0') + 1) % 10 + '0';
			search(i + 1, sa, sb);
			sa[i] = '0';
			search(i + 1, sa, sb);
			sa[i] = '9';
			search(i + 1, sa, sb);
		}
	} else {
		if (sb[i] == '?') {
			sb[i] = sa[i];
			search(i + 1, sa, sb);
			sb[i] = ((sa[i] - '0') + 9) % 10 + '0';
			search(i + 1, sa, sb);
			sb[i] = ((sa[i] - '0') + 1) % 10 + '0';
			search(i + 1, sa, sb);
			sb[i] = '0';
			search(i + 1, sa, sb);
			sb[i] = '9';
			search(i + 1, sa, sb);
		} else {
			search(i + 1, sa, sb);
		}
	}
}

int main() {
	int testcases;
	cin >> testcases;
	for (int testcase = 0; testcase < testcases; testcase ++) {
		string sa, sb;
		cin >> sa >> sb;
		ansa = ansb = "";
		ansd = -1;
		search(0, sa, sb);
		cout << "Case #" << testcase + 1 << ": " << ansa << " " << ansb << endl;
	}
	return 0;	
}