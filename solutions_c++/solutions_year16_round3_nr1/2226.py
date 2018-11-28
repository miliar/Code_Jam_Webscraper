#include <iostream>
#include <iomanip>
#include <string.h>
#include <stdint.h>
#include <vector>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <stdio.h>
#include <bitset>
#include <assert.h>
#include "combination.hpp"
using namespace std;

int N;
vector<pair<string, string>> L;


int main(int argc, char* argv[])
{
	if (argc >= 2) {
		FILE* fp = freopen(argv[1], "r", stdin);
	}

	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int Pn = 0;
		vector<int> Ps;
		cin >> N;
		for (int i = 0; i < N; i++) {
			int P;
			cin >> P;
			Pn += P;
			Ps.push_back(P);
		}
		cout << "Case #" << i + 1 << ":";
		while (Pn > 0) {
			int max1 = -1, max2 = -1, max3 = -1;
			for (int i = 0; i < N; i++) {
				if (Ps[i] == 0) continue;

				if (max1 == -1) {
					max1 = i;
				} else {
					if (Ps[i] > Ps[max1]) {
						max3 = max2;
						max2 = max1;
						max1 = i;
					} else {
						if (max2 == -1) {
							max2 = i;
						} else {
							if (Ps[i] > Ps[max2]) {
								max3 = max2;
								max2 = i;
							} else {
								if (max3 == -1) {
									max3 = i;
								} else {
									if (Ps[i] > Ps[max3]) {
										max3 = i;
									}
								}
							}
						}
					}
				}
			}
			if (Ps[max1] == Ps[max2]) {
				if (max3 != -1) {
					if (Ps[max3] / (Pn - 2.0) <= 0.5) {
						cout << " " << (char) ('A' + max1) << (char) ('A' + max2);
						Ps[max1] -= 1;
						Ps[max2] -= 1;
						Pn -= 2;
					} else {
						cout << " " << (char) ('A' + max1);
						Ps[max1] -= 1;
						Pn -= 1;
					}
				} else {
					cout << " " << (char) ('A' + max1) << (char) ('A' + max2);
					Ps[max1] -= 1;
					Ps[max2] -= 1;
					Pn -= 2;
				}
			} else {
				cout << " " << (char) ('A' + max1);
				Ps[max1] -= 1;
				Pn -= 1;
			}
		}
		cout << endl;
	}

	return 0;
}
