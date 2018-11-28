#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <fstream>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

using namespace std;

int counter = 0;

vector<int> warSmall(vector<double> &Nw, vector<double> &Kw, int N) {	
	
	// cout << Nw.size() << endl;	
	vector<int> result(2,0);
		
	sort(Nw.begin(), Nw.end());	//small to large
	sort(Kw.begin(), Kw.end());
	
	int nwar = 0;
	int ndwar = 0;
	
	// for war game, Naomi losses if Ken use the lighter one which is heavier than her's 
	int i=0, j=0;
	while (i < N && j < N) {
		
		if (Nw[i] < Kw[j]) {
			i += 1;
			j += 1;
		} else {
			j += 1;
			nwar += 1;
		}
	}
	result[1] = nwar;	

	i=0;
	j=0;
	int upper = N;
	while (i < N && j < upper) {
		
		if (Nw[i] < Kw[j]) {
			i += 1;
			upper -= 1;
		} else { // no equal
			j += 1;
			i += 1;
			ndwar += 1;
		}
	}
	result[0] = ndwar;
	
	return result;
}

void process() {
	int N;
	cin >> N;
	
	vector<double> Nw(N), Kw(N);
	
	for (int i=0; i<N; i++) cin >> Nw[i];
	for (int i=0; i<N; i++) cin >> Kw[i];

	vector<int> num = warSmall(Nw, Kw, N);
	//N wins in dwar and war
	cout << "Case #" << ++counter << ": " << num[0] << " " << num[1] << endl;

	return;
}


int main() {
	int t;
	scanf("%d", &t); // read the number of cases
	
	while (t--) {
		process();
	}

	return 0;
}