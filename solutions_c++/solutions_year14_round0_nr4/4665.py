#include <iostream>
#include <fstream>
#include <set>
#include <iomanip>
#include <deque>
#include <algorithm>

using namespace std;
int T, N;

int main(){
	ifstream infile("input.txt");
	infile >> T;
	deque<double> naomi, ken;

	for(int i = 1; i <= T; i++){
		infile >> N;

		naomi.clear(); ken.clear();
		for(int ii = 0; ii < N; ii++){
			double temp;
			infile >> temp;
			naomi.push_back(temp);
		}
		for(int ii = 0; ii < N; ii++){
			double temp;
			infile >> temp;
			ken.push_back(temp);
		}

		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());

		deque<double> naomi2(naomi);
		deque<double> ken2(ken);

		int dW = 0;
		int W = 0;
		int kenP = 0;
		int nP = 0;

		while(!naomi.empty()){
			if(naomi[naomi.size() - 1] < ken[ken.size() - 1]){
				naomi.pop_front();
				ken.pop_back();
			}
			else{
				dW++;
				naomi.pop_back();
				ken.pop_back();
			}
		}

		kenP = 0;

		while(true){
			if(kenP >= ken2.size() || naomi2.empty() || ken2.empty()){
				break;
			}
			if(naomi2[0] > ken2[kenP]){
				kenP++;
				W++;
			}
			else{
				naomi2.erase(naomi2.begin());
				ken2.erase(ken2.begin() + kenP);
			}
		}

		cout << "Case #" << i << ": " << dW << " " << W << endl;
	}
}