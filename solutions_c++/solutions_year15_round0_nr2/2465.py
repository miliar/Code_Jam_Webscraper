#include <iostream>
#include <vector>
#include <stack>
#include <cmath>

// Gilles Waeber, 12.04.2015
// O(D*Pmax)

using namespace std;

const int P_LIMIT = 1001;
const int INF = 1e9;

int answer(){
	int D, Pi, Pmax = 1, specialMinutes = 0, Tmin;
	vector<stack<int>> diners = vector < stack<int> >(P_LIMIT);
	cin >> D;
	for (int d = 0; d < D; d++){
		cin >> Pi;
		diners[Pi].push(Pi);
		if (Pi > Pmax) Pmax = Pi;
	}
	Tmin = Pmax;

	for (int level = Pmax; level > 1;){

		while (!diners[level].empty()){
			int Pi = diners[level].top(), splits = (Pi + level - 1) / level;
			diners[level].pop();
			while ((Pi + splits - 1) / splits >= level){
				splits++;
				specialMinutes++;
			}
			diners[(Pi + splits - 1) / splits].push(Pi);
		}

		do{
			level--;
		} while (diners[level].empty() && level > 1);

		if (level + specialMinutes < Tmin) Tmin = level + specialMinutes;
	}

	return Tmin;
}

// B. INFINITE HOUSE OF PANCAKES

int main(){
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++){
		cout << "Case #" << i << ": " << answer() << "\n";
	}
	cout << flush;
}