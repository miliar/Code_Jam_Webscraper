#include <stdio.h>
#include <string.h>
#include <iostream>
#include <list>
#include <vector>
#include <stdlib.h>
#include <queue>
#include <algorithm>

using namespace std;

int findMin(int N, double arr[]) {
	double min_value = 1;
	int min_place = -1;
	for (int m = 0; m < N; m++) {
		if (arr[m] < min_value && (arr[m]!=-1)) {
			min_value = arr[m];
			min_place = m;
		}
	}
	return min_place;
}

int findMax(int N, double arr[]) {
	double max_value = -1;
	int max_place = -1;
	for (int m = 0; m < N; m++) {
		if (arr[m] > max_value && (arr[m]!=2)) {
			max_value = arr[m];
			max_place = m;
		}
	}
	return max_place;
}

int main() {
	int T;
	cin >> T;
	for (int i = 1 ; i <= T ; i++){
		int N, D = 0, W = 0;
		cin >> N;
		double naomi[N], ken[N], ken_temp[N];
		for (int j = 0 ; j < N ; j++){
			cin >> naomi[j];
		}
		for (int j = 0 ; j < N ; j++){
			cin >> ken[j];
			ken_temp[j] = ken[j];
		}

		for (int k = 0 ; k < N ; k++){
			double diff = 2;
			int place = -1;
			for (int j = 0 ; j < N ; j++){
				if ((ken_temp[j] != -1) && (ken_temp[j]>naomi[k]) && (diff > (ken_temp[j]-naomi[k])))
				{
						diff = (ken_temp[j]-naomi[k]);
						place = j;
				}
			}
			if (place != -1){
				ken_temp[place] = -1;
			}else{
				W++;
				ken_temp[findMin(N, ken_temp)] = -1;
			}
		}

		for (int k = 0 ; k < N ; k++){
			int naomi_min_place = findMin(N, naomi);
			int ken_min_place = findMin(N, ken);
			int naomi_max_place = findMax(N, naomi);
			int ken_max_place = findMax(N, ken);

			/* "kill" kens max with naomis min */
			if (naomi[naomi_min_place] < ken[ken_min_place]){
				naomi[naomi_min_place] = 2;
				ken[ken_max_place] = -1;
				continue;
			}

			/* win ken's max with naomis max */
			if (naomi[naomi_max_place] > ken[ken_max_place]){
				naomi[naomi_max_place] = -1;
				ken[ken_max_place] = -1;
				D++;
				continue;
			}

			/* naomi can't win ken's max, lets kill it with min */
			naomi[naomi_min_place] = 2;
			ken[ken_max_place] = -1;
		}

		cout << "Case #" << i << ": " << D << " "  << W << endl;
	}
}
