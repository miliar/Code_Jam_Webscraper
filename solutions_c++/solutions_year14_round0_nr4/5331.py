#include <iostream>
#include <algorithm>
#include <vector>
/*
Ken's war strategy: choose his lightest block heavier than Naomi_told
Naomi's Dwar strategy: maximise Naomi_told and minimise Naomi_chosen
Naomi's war strategy: maximise Naomi_chosen

Dwar Sim:
1. find ken's highest.
2. look at naomi's lowest:
   a. naomi's is less than ken's. 
	-> choose this block
   b. naomi's is greater than ken's
	-> naomi wins the rest
	

*/	

using namespace std;

void print(vector<float> v) {
	for(auto it = v.begin(); it != v.end(); it++) cout << *it << " ";
	cout << endl;
}

int main() {
	int T = 0;
	cin >> T;
	for(int i = 0; i < T; i++) {
		int N = 0;
		cin >> N;
		vector<float> naomi, ken;
		float buf;
		for(int j = 0; j < N; j++) {
			cin >> buf;
			naomi.push_back(buf);
		}
		for(int j = 0; j < N; j++) {
			cin >> buf;
			ken.push_back(buf);
		}
		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());
		//print(naomi);
		//print(ken);
		
		// Simulate War
		int W_Kscore = 0, W_Nscore = 0;
		vector<float> temp_ken(ken);
		bool kscored = false;
		for(int j = 0; j < N; j++) {
			kscored = false;
			for(auto it = temp_ken.begin(); it != temp_ken.end(); it++) {
				if(*it > naomi[N-j-1]) {
					kscored = true;
					W_Kscore++;
					temp_ken.erase(it);
					break;
				}
			}
			if(!kscored) {
				W_Nscore++;
			}
		}
		
		// Simulate Deceitful War
		int D_Kscore = 0, D_Nscore = 0;
		for(int k = 0; k < N; k++) {
			//cout << naomi[0] << " " << ken[0] << " " << endl;
			if(naomi[0] > ken[0]) {
				D_Nscore++;
				ken.erase(ken.begin());
			}
			else {
				ken.pop_back();
			}
			naomi.erase(naomi.begin());
		}
		cout << "Case #" << i+1 << ": " << D_Nscore << " " << W_Nscore << endl;
	}
}
