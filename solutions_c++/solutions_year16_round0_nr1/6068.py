#include <iostream>
#include <vector>
#include <cmath>
#include <cstdlib>
using namespace std;

void printv (vector <int> v){
	for(int i : v) cout << i;
	cout << endl;
}

vector <int> charToV (char c [6]){
	vector <int> v;
	for(int i = 0; c[i] != 0; i++){
		v.push_back(c[i] - 48);
	}
	return v;
}

int main(){
	int T, i, j, k;
	long N;
	char lel[6];
	cin >> T;
	for(i = 0; i < T; i++){
		cin >> lel;
		vector <int> digitN(charToV(lel));
		vector <int> digitset = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
		N = atol(lel);
		long temp = N;
		if(N == 0){
			cout << "CASE #" << i + 1<< ": INSOMNIA\n";
			continue;
		}
		while(((int) digitset.size()) > 0){
			sprintf(lel, "%ld", N);
			digitN = charToV(lel);
			for(k = 0; k < digitN.size(); k++){
				for(j = 0; j < digitset.size(); j++){
					if(digitset[j] == digitN[k]) {
						digitset.erase(digitset.begin() + j);
						j--;
					}
				}
			}
			N += temp;
		}
		N -= temp;
		cout << "CASE #" << i + 1<< ": " << N << endl;
	}
}