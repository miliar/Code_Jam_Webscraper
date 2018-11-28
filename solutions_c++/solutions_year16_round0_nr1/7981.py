#include <iostream>
#include <cmath>
#include <cassert>
#include <vector>
#include <boost/math/distributions/chi_squared.hpp>
#include <iterator>
#include <algorithm>
#include <cstring>
#include <fstream>
#include <sstream>

using namespace std;


int main(){
	
	int pocetVstupu;
	int vstup;
	vector<int> aktualniCislo;
	vector<int> nevideneCifry;
	
	cin >> pocetVstupu;
	
	for(int k=0; k < pocetVstupu; k++){
		cin >> vstup;
		
		if(vstup == 0){
			cout << "Case #" << k+1 << ": INSOMNIA" << endl;
		} else{
			nevideneCifry.clear();
			for(int i=0; i<10; i++){
				nevideneCifry.push_back(i);
			}
			bool usnula = false;
			
			string cislo = to_string(vstup);
			aktualniCislo.clear();
			//nacte cislo do vektoru
			for(int i=0; i<cislo.length(); i++){
				aktualniCislo.push_back(cislo.at(i)-'0');
			}
			
			//uvodni beh
			//zjisti vyskyt cifer
			for(int i=0; i<aktualniCislo.size(); i++){
				if(aktualniCislo[i] == nevideneCifry[aktualniCislo[i]]){
					nevideneCifry[aktualniCislo[i]] = -1;
				}
			}
			//vyhodnoti zda usnula
			usnula = true;
			for(int i=0; i<10; i++){
				if(nevideneCifry[i] == i){
					usnula = false;
				}
			}
			
			int vynasobenyVstup;
			int nasobeni = 2;
			while (usnula == false) {
                vynasobenyVstup = nasobeni * vstup;
				
				string cislo = to_string(vynasobenyVstup);
			    aktualniCislo.clear();
			    //nacte cislo do vektoru
			    for(int i=0; i<cislo.length(); i++){
					aktualniCislo.push_back(cislo.at(i)-'0');
				}
					
				//zjisti vyskyt cifer
				for(int i=0; i<aktualniCislo.size(); i++){
					if(aktualniCislo[i] == nevideneCifry[aktualniCislo[i]]){
						nevideneCifry[aktualniCislo[i]] = -1;
					}
				}
				//vyhodnoti zda usnula
				usnula = true;
				for(int i=0; i<10; i++){
					if(nevideneCifry[i] == i){
						usnula = false;
					}
				}
				
				nasobeni ++;
			} 
			
			cout << "Case #" << k+1 << ": " << vynasobenyVstup << endl;
		}	
		
	}
	
    return 0;
}


    
