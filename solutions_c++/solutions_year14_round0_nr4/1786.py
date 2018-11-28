#include <iostream>
#include <cstdio>
#include <math.h>
#include <iomanip>
#include <algorithm>
#include <cstring>

using namespace std;

const int MAX = 1009;
double naomi[MAX], ken[MAX];
bool flag_ken[MAX];

int main()
{
	int T;
	cin >> T;
	int case_id = 1;

	while (T--) {
		int N;
		cin >> N;
		for (int i = 0; i < N; i++)
			cin >> naomi[i];
		for (int i = 0; i < N; i++)
			cin >> ken[i];

		memset(flag_ken, true, sizeof(flag_ken));
		sort(naomi, naomi + N);
		sort(ken, ken + N);
		/*
		for (int i = 0; i < N; i++)
			cout << naomi[i] << " ";
		cout << endl;

		for (int i = 0; i < N; i++)
			cout << ken[i] << " " ;
		cout << endl;
		*/
		// war.
		int result_war = 0;
		for (int i = 0; i < N; i++) {
			// find the first element in ken that is bigger than naomi[i].
			int target = -1;
			for (int j = 0; j < N; j++) {
				if (ken[j] > naomi[i] && flag_ken[j] == true) {
					target = j;
					break;
				}
			}

			if (target == -1) {
				// all available element in ken is smaller. 
				for (int j = 0; j < N; j++) {
					if (flag_ken[j] == true) {
						flag_ken[j] = false;
					}
				}
				result_war++;
			}
			else {
				flag_ken[target] = false;
			}
		}


		// deceitful war.
		int result_deceit = 0;
		int tag = -1;
		memset(flag_ken, true, sizeof(flag_ken));
		for (int i = N - 1; i >= 0; i--) {
			if (naomi[i] > ken[i]) {
				result_deceit++;
			}
			else {
				tag = i;
				break;
			}
		}
		//cout << tag << endl;
		if (tag == -1) {
			;	// done!
		}
		else {
			for (int i = tag; i >= 0; i--) {
				bool no_more = true;
				for (int j = tag; j >= 0; j--) {
					//cout << naomi[i] << " " << ken[j] << flag_ken[j] << endl;
					if (ken[j] < naomi[i] && flag_ken[j] == true) {
						result_deceit++;
						flag_ken[j] = false;
						no_more = false;
						break;
					}
				}

				if (no_more == true) {
					break;
				}
			}

		}

		cout << "Case #" << case_id++ << ": " << result_deceit << " " << result_war << endl;
	}
}