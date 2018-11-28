#include <iostream>
#include <cmath>
#include <cassert>
#include <vector>
#include <iterator>
#include <algorithm>
#include <cstring>
#include <fstream>
#include <sstream>

using namespace std;


int main(){
	
	int pocetVstupu;
	string vstup;
	vector<char> vystup;
	
	cin >> pocetVstupu;
	
	
	
	for(int k=0; k < pocetVstupu; k++){
		vstup.clear();
		vystup.clear();
		
		cin >> vstup;
		vystup.push_back(vstup[0]);
		
		
		for(int i=0; i<vstup.length()-1; i++){
				if(vstup[i+1] >= vystup[0]){
					vystup.insert(vystup.begin(),vstup[i+1]);
				} else {
					vystup.push_back(vstup[i+1]);
				}
			}
		cout << "Case #" << k+1 << ": ";
		for(int i=0; i<vystup.size(); i++){
				cout << vystup[i];
			}	
		cout << endl;	
	}
	
    return 0;
}