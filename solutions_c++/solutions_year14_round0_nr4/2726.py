#include <iostream>
#include <algorithm>
#include <iomanip>
#include <vector>
#include <fstream>

#define EPS 0.0000001

using namespace std;

int playWar(vector<double> &nao, vector<double> &ken) 
{
	int N = nao.size();
	int kenWins = 0;
	int naoWins = 0;
	
	int kmin = 0;
	int k;

	// Naomi put increasing blocks, believing that Ken make mistake
	for (int i = 0; i < N; i++) {
		// Ken choose minimum block which beat Naomi's
		k = kmin;
		while(k < N && ken[k] < nao[i]) k++;
		if (k == N) {
			// oops, he can't bit her - so throw minimum block
			kmin++;
			naoWins++;
		} else {
			// found it - beat Naomi
			kenWins++;
			ken[k] = -1;
		}
	}
	
	return naoWins;
}

int playDeceitfulWar(vector<double> &nao, vector<double> &ken) 
{
	int N = nao.size();
	int kenWins = 0;
	int naoWins = 0;
	
	int kmin = 0;
	
	for (int i = 0; i < N; i++) {
		
		if (nao[i] > ken[kmin]) {
			// Naomi can win this block - cheat about ken[kMax] + eps (Ken choose min and lose)
			naoWins++;
			kmin++;
		} else {
			// this block is too small, do her best - cheat about ken[kMax] - eps to steal Ken's maximum
			kenWins++;
		}
	}	
	return naoWins;
}



int main (void)
{
	int T; 		// number of games
	int N;		// number of blocks
	vector<double> nao;
	vector<double> ken;
	double in;

	cin >> T;
	
	for (int t = 0; t < T; t++) {

		// read input
		cin >> N;
		
		for (int i = 0; i < N; i++) {
			cin >> in;
			nao.push_back(in);			
		}
		
		for (int i = 0; i < N; i++) {
			cin >> in;
			ken.push_back(in);
		}				

		// sort arrays
		sort(nao.begin(), nao.end());
		sort(ken.begin(), ken.end());
					
 		// Output
 		cout << "Case #" << t+1 << ": ";
 		cout << playDeceitfulWar(nao, ken);
		cout << " ";
		cout << playWar(nao, ken);
 		cout << endl;

		nao.clear();
		ken.clear();
	}
	
	
	return 0;	
}
			
			
			
			
			
			
			
			
			