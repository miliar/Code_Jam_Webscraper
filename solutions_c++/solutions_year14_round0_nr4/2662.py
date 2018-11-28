#include <iostream>
#include <stdio.h>
#include <list>

using namespace std;

void GetData(int N, list<double>& user) {
	for(int i = 0; i < N; i++) {
		double weight = 0;
		cin >> weight;
		user.push_back(weight);
	}
	user.sort();
	user.reverse();
}

void HandleCases(int caseCount) {
	for (int i = 1; i <= caseCount; i++) {
		int N = 0;
		cin >> N;
		list<double> Naomi, Ken;
		GetData(N, Naomi);
		GetData(N, Ken);
		int trickyScore = 0;
		for (list<double>::iterator naomi = Naomi.begin(), ken = Ken.begin(); (naomi != Naomi.end()) && (ken != Ken.end()); ) {
			if (*naomi > *ken) {
				trickyScore++;
				naomi++;
			   	ken++;
			} else {
				ken++;
			}
		}
		int score = 0;
		Naomi.reverse();
		for (list<double>::iterator naomi = Naomi.begin(); naomi != Naomi.end(); naomi++) {
			list<double>::iterator ken = Ken.begin();
			if (ken != Ken.end()) {
				if (*naomi > *ken) {
					score = Ken.size();
					break;
				}
			
				list<double>::iterator tempKen = ken;
				tempKen++;
				while(tempKen != Ken.end() && *tempKen > *naomi) {
					ken = tempKen;
					tempKen++;
				}
				Ken.erase(ken);
			}
		}
		cout << "Case #" << i << ": " << trickyScore << " " << score <<endl;
	}
}

int main() {
	int caseCount = 0;
	cin >> caseCount;
	HandleCases(caseCount);
	return 0;
}
