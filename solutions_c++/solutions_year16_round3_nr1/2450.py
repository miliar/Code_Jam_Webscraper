#include <cstdlib>
#include <string>
#include <iostream>
#include <math.h>
#include <vector>

using namespace std;

int checkhighest(int * abc, int k, int highestij) {
	int highesti = highestij;
	int highest;
	highest = abc[highestij];
	int i;
	for (i = 0; i < k; i++) {
		if (abc[i] > highest) {
			highesti = i;
			highest = abc[i];
		}
	}

	return highesti;
}


int main() {
	int test;
	cin >> test;
	int n;
	for (n = 0; n < test; n++) {
		cout<<"Case #"<<(n + 1)<<": ";
		int k;
		cin >> k;

		int i;
		int * abc = (int *) malloc(k * sizeof(int));
		int highest;
		int highesti;
		int total = 0;
		for (i = 0; i < k; i++) {
			int j;
			cin >> j;
			abc[i] = j;
			if (i == 0) {
				highest = j;
				highesti = 0;
			}

			if (j > highest) {
				highest = j;
				highesti = i;
			}
			total = total + j;
		}
		while (total > 0) {
			if (total != 3) {
				if (abc[highesti] > total/2) {
					cout << "WRONG" << endl;
				}
				cout <<char('A' + highesti);
				abc[highesti]--;
				total--;
				highesti = checkhighest(abc, k, highesti);
				cout <<char('A' +highesti);
				abc[highesti]--;
				total--;
				cout <<" ";
				highesti = checkhighest(abc, k, highesti);
			} else {
				if (abc[highesti] > total/2) {
					cout << "WRONG" << endl;
				}
				cout <<char('A' + highesti);
				abc[highesti]--;
				total--;
				cout << " ";
				highesti = checkhighest(abc, k, highesti);
			}

		}
		cout << endl;	

	}
}