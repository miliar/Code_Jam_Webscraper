#include "B.h"

#include <cassert>
#include <iostream>
#include <string>
#include <numeric> 
#include <vector> 
#include <sstream>

using namespace std;


void solveB(){
	FILE *fin = freopen("B-large.in", "r", stdin);
	assert(fin != NULL);
	FILE *fout = freopen("B-large.out", "w", stdout);
	int T;

	cin >> T;
	for (int t = 1; t <= T; t++){
		string order;
	
		cin >> order;
		char cprev = order.at(0);
		int flips = 1;

		for (int i = 1; i < order.size(); i++){
			if (order.at(i) != cprev){
				flips++;
			}
			cprev = order.at(i);
		}
		if (order.at(order.size()-1)=='+'){
			flips--;
		}
		cout << "Case #" << t << ": ";
		cout << flips << endl;
		
	}
}