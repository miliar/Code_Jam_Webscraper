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
	int pocetZmen;
	
	cin >> pocetVstupu;
	
	for(int k=0; k < pocetVstupu; k++){
		pocetZmen = 0;
		cin >> vstup;
		for(int i=0; i<vstup.length()-1; i++){
				if(vstup[i] != vstup[i+1]){
					pocetZmen++;
				}
			}
		if(vstup[vstup.length()-1] == '+'){
			cout << "Case #" << k+1 << ": " << pocetZmen << endl;
		} else{
		    cout << "Case #" << k+1 << ": " << pocetZmen+1 << endl;
		}
	}
	
    return 0;
}


    
