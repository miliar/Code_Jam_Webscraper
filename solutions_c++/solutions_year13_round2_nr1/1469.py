//============================================================================
// Name        : CodeJam.cpp
// Author      : 
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include "math.h"
#include <algorithm>
#include <vector>
using namespace std;




int main() {
	int cunt,kunt;
	long my_weigh, moth_count, i, operations, rest;
	vector<int> moths_weigh;
	cin >> cunt;

	for (kunt=1; kunt<=cunt; ++kunt){
		operations=0;
		cin >> my_weigh;
		cin >> moth_count;
		moths_weigh.resize(moth_count);
		for (i=0; i<moth_count; ++i){
			cin >>moths_weigh[i];
		}
		sort(moths_weigh.begin(), moths_weigh.end());


		for(i=0; i<moth_count; ++i){
			rest = i;
			while (my_weigh <= moths_weigh[i] && rest < moth_count){
				my_weigh += my_weigh-1;
				++rest;
				++operations;
			}
			my_weigh += moths_weigh[i];
			if (operations >= moth_count || rest >= moth_count) break;
		}

		cout << "Case #" << kunt << ": " << operations <<  endl;

	}
	return 0;
}
