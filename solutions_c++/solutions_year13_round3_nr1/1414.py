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
#include <string>
using namespace std;




int main() {
	int cunt,kunt;
	int result, n, first, last, cur_const;
	string word;

	cin >> cunt;

	for (kunt=1; kunt<=cunt; ++kunt){
		cur_const = 0;
		result = 0;
		first = 0;
		last = 0;
		cin >> word;
		cin >> n;
		while (last!=word.size()){
			if (word[last] != 'a' && word[last] != 'e' && word[last] != 'i' && word[last] != 'o' && word[last] != 'u'){
				++cur_const;
				if (cur_const == n){
					result += (last-n-first+2)*(word.size()-last);
					--cur_const;
					first = last-n+2;
				}
			}else {
				cur_const = 0;
			}
			++last;
		}



		cout << "Case #" << kunt << ": " << result <<  endl;

	}
	return 0;
}
