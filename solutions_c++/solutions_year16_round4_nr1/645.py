#include <iostream>

using namespace std;

int n, r, p, s;
int order[20][3];

int ord(pair<int, int> p) {
	if (p == make_pair(0, 1) || p == make_pair(1, 0)) return 0;
	if (p == make_pair(0, 2) || p == make_pair(2, 0)) return 1;
	if (p == make_pair(1, 2) || p == make_pair(2, 1)) return 2;
	return -1;
}

void printhelp(int round, int cur) {
	if (round == 0) {
		switch (cur) {
			case 0: cout << "R"; break;
			case 1: cout << "P"; break;
			case 2: cout << "S"; break;
		}
		return;
	} else {
		switch (cur) {
		case 0: // rock versus scissors
			if (order[round - 1][0] < order[round - 1][2]) {
				printhelp(round - 1, 0);
				printhelp(round - 1, 2);
			}
			else {
				printhelp(round - 1, 2);
				printhelp(round - 1, 0);
			}
			break;
		case 1: // paper versus rock
			if (order[round - 1][0] < order[round - 1][1]) {
				printhelp(round - 1, 0);
				printhelp(round - 1, 1);
			}
			else {
				printhelp(round - 1, 1);
				printhelp(round - 1, 0);
			}
			break;
		case 2: // scissors versus paper
			if (order[round - 1][2] < order[round - 1][1]) {
				printhelp(round - 1, 2);
				printhelp(round - 1, 1);
			}
			else {
				printhelp(round - 1, 1);
				printhelp(round - 1, 2);
			}
			break;
		}
	}
}

void printrps() {
	if (r > 0) {
		printhelp(n, 0);
	}
	else if (p > 0) {
		printhelp(n, 1);
	}
	else if (s > 0) {
		printhelp(n, 2);
	}
}

int main() {
	order[0][0] = 1; // rock
	order[0][1] = 0; // paper
	order[0][2] = 2; // scissors
	for (int round = 1; round < 20; ++round) {
		order[round][0] = ord(make_pair(order[round - 1][0], order[round - 1][2])); // rock beats scissors
		order[round][1] = ord(make_pair(order[round - 1][1], order[round - 1][0])); // paper beats rock
		order[round][2] = ord(make_pair(order[round - 1][2], order[round - 1][1])); // scissors beats paper
	}
	int t; cin >> t;
	for (int test = 1; test <= t; ++test) {
		cin >> n >> r >> p >> s;

		cout << "Case #" << test << ": ";

		int round = 0;
		bool failure = false;
		while (round < n) {
			int total = r + p + s;
			if (total % 2 != 0) {
				failure = true; break;
			}
			total /= 2;
			int rr = total - p; // rock + scissor matches is total/2 - paper
			int pp = total - s;
			int ss = total - r;
			if (rr < 0 || pp < 0 || ss < 0) {
				failure = true; break;
			}
			r = rr; p = pp; s = ss;
			round++;
		}
		if (failure) {
			cout << "IMPOSSIBLE" << endl;
		}
		else {
			printrps();
			cout << endl;
		}
	}
	return 0;
}