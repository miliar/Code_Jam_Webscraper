#include <iostream>
#include <fstream>
#include <stdio.h>
using namespace std;


int P[1001];

int main()
{
	ifstream cin("A-small-attempt0.in");
	ofstream cout("output.txt");
	int T;
	cin >> T;
	int N;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";
		cin >> N;
		int sum = 0;
		for (int n = 0; n < N; n++) {
			cin >> P[n];
			sum += P[n];
		}
		//cout << sum << " ";
		while (sum > 0) {
			int a = -1;
			int b = -1;
			
			if (sum > 1) {
				for (int i = 0; i < N; i++) {
					for (int j = i; j < N; j++) {
						bool ok = true;
						for (int k = 0; k < N; k++) {
							int now = P[k];
							if (k == i) {
								now--;
							}
							if (k == j) {
								now--;
							}
							if ((sum - 2) < now * 2) {
								ok = false;
								break;
							}
						}
						if (ok) {
							a = i;
							b = j;

			//				cout <<  a << b << " ";
							break;
						}
					}
				}
			}

			if (a == -1) {
				for (int i = 0; i < N; i++) {
					bool ok = true;
					for (int k = 0; k < N; k++) {
						int now = P[k];
						if (k == i) {
							now--;
						}
						if ((sum - 1) < now * 2) {
							ok = false;
							break;
						}
					}
					if (ok) {
						a = i;
						break;
					}
				}
			}

			P[a]--;
			cout << (char)('A'+ a );
			if (b != -1) {
				P[b]--;
				sum--;
				cout << (char)('A'+b);
			}
			sum--;

			cout << " ";
		}


		cout << '\n';
	}



	return 0;
}