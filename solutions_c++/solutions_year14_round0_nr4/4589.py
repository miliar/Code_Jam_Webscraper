#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;

#define MAX 1000


int size;

void display(const vector<double>& v, int size) {
	cout << endl;
	for (int i = 0 ; i < size ; i++) {
		cout << v[i] << " ";
	}
	cout << endl;
}

int war(const vector<double>& naomi, const vector<double>& ken) {
	int* mask = new int[size];
	memset(mask, 0 , size*sizeof(int));
	int k_cnt = 0;
	for (int i = 0 ; i < size ; i++) {
		const double n = naomi[i];
		for (int j = 0 ; j < size ; j++) {
			if ((ken[j] > n) && !mask[j]) {
				mask[j] = 1;
				k_cnt++;
				break;
			}
		}
	}
	delete mask;
	return size - k_cnt;
}

int d_war(const vector<double>& naomi, const vector<double>& ken) {
	int* mask = new int[size];
	memset(mask, 0 , size*sizeof(int));
	int n_cnt = 0;
	for (int i = 0 ; i < size ; i++) {
		const double n = naomi[i];
		for (int j = 0 ; j < size ; j++) {
			if(!mask[j] && (ken[j] < n)) {
				mask[j] = 1;
				n_cnt++;
				break;
			}
		}
	}
	delete mask;
	return n_cnt;
}

void doSolve(int* n_dw, int* n_w) {
	cin >> size;
	std::vector<double> ken(size);
	std::vector<double> naomi(size);	
	for (int i = 0 ; i < size ; i++) {
		cin >> naomi[i];
	}
	for (int i = 0 ; i < size ; i++) {
		cin >> ken[i];
	}
	//display(naomi, size);
	//display(ken, size);
	sort(ken.begin(), ken.begin()+size);
	sort(naomi.begin(), naomi.begin()+size);
	//display(naomi, size);
	//display(ken, size);
	*n_w = war(naomi, ken);
	*n_dw = d_war(naomi, ken);
}

int main() {
	int T;
	cin >> T;
	for (int i = 1 ;  i <= T ; i++)  {
		int naomi_w, naomi_dw;
		doSolve(&naomi_dw, &naomi_w);
		cout << "Case #" << i << ": " << naomi_dw << " " << naomi_w << endl;
	}
}
