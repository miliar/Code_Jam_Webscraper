#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {		
		int N;
		cin >> N;
		vector<double> nao(N), ken(N);
		for (int j = 0; j < N; j++)
			cin >> nao[j];
		for (int j = 0; j < N; j++)
			cin >> ken[j];
				
		sort(nao.begin(), nao.end());
		sort(ken.begin(), ken.end());
		
		int k = N-1, w = 0, dw = 0;
		for (int j = N-1; j >= 0; j--) {
			if (nao[j] > ken[k]) {
				w++;
			} else {
				k--;
			}
		}	
		
		k = N-1;
		int n = N-1;
		while (k >= 0) {
			while (k >= 0 && nao[n] < ken[k]) {
				k--;
			}
			if (k >= 0) {
				dw++;
			}
			k--; n--;
		}	
		
		cout << "Case #" << i+1 << ": " 
			 << dw << " " << w << endl;			
	}	
	return 0;	
}
