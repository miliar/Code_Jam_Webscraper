#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <map>
using namespace std;

int lookFor(string *inputLetters, string pattern){
	int strSize = inputLetters->size();
	size_t pos = inputLetters->find(pattern[0]);
	if(pos == string::npos)
		return 0;
		
	inputLetters->replace(pos, 1, "0");
	for(int k = 1; k < pattern.size(); ++k)
		inputLetters->replace(inputLetters->find(pattern.at(k)), 1, "0");
	
	return lookFor(inputLetters, pattern)+1;
}


int main(){
	int t;
	string inputLetters;
	vector<int> digitAmount(10,0);
	
	cin >> t;
	
	for(int i = 1; i <= t; ++i){
		cin >> inputLetters;
		
		digitAmount[0] = lookFor(&inputLetters, "ZERO");
		digitAmount[2] = lookFor(&inputLetters, "WTO");
		digitAmount[4] = lookFor(&inputLetters, "UFOR");
		digitAmount[6] = lookFor(&inputLetters, "XSI");
		digitAmount[5] = lookFor(&inputLetters, "FIVE");
		digitAmount[7] = lookFor(&inputLetters, "SEVEN");
		digitAmount[1] = lookFor(&inputLetters, "ONE");
		digitAmount[3] = lookFor(&inputLetters, "RTHEE");
		digitAmount[8] = lookFor(&inputLetters, "HEIGT");
		digitAmount[9] = lookFor(&inputLetters, "NINE");
		
		
		cout << "Case #" << i << ": ";
		for(int d = 0; d < 10; ++d){
			for(int k = 0; k < digitAmount[d]; ++k){
				cout << d ;
			}
		}
		cout << endl;
		
		    
	}

}
