#include <iostream>
#include <stdio.h>
#include <string>
#include <math.h>
#include <cmath>

using namespace std;

int cuts(int cutsize, int nempty, int * plates){
	int answer = 0;
	int i;
		
	for (i = 0; i < nempty; i++) {
		answer = answer + (plates[i] - 1)/cutsize;
	}
	return answer;	
}

int maxpile(int nempty, int * plates){
	int i, ans = 0;
	for (i = 0; i < nempty; i++) {
		if (plates[i] > ans) {
			ans = plates[i];
		}
	}
	return ans;
}

int countd(int nempty, int * plates){
	int total = 0;
	int i;
	for (i = 0; i < nempty; i++) {
		total = total + plates[i];
	}
	return total;
}


int main (int argc, char * const argv[]) {
	
	int cases;
	
	cin >> cases;
	
	int diners[1005], plate;
	int lbound, ubound, run, sizee, minutes, nempty;
	
	for (run = 0; run < cases; run++) {
		cin >> nempty;
		plate = 0;
		for (plate = 0; plate < nempty; plate++) {
			cin >> diners[plate];
		}
		
		if (1 < ceil(sqrt(countd(nempty, diners))) - 3*nempty - 1) {
			lbound = ceil(sqrt(countd(nempty, diners))) - 3*nempty - 1;
		}
		else {
			lbound = 1;
		}
		ubound = min(lbound + 6*nempty + 1, maxpile(nempty, diners) + 1);
		
		minutes = maxpile(nempty, diners);
		
		for (sizee = lbound; sizee < ubound; sizee++) {
			if (minutes > cuts(sizee, nempty, diners) + sizee) {
				/*cout << "minutos e" << minutes << " " << sizee << endl;*/
				minutes = cuts(sizee, nempty, diners) + sizee;
			}
		}
		
		cout << "Case #" << run + 1 << ": " << minutes << endl;		
	}
	return 0;
}
