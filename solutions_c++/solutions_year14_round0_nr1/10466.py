#include <stdio.h>
#include <string>
#include <iostream>
#include <sstream>

using namespace std;
string fungsi();
int main(void) {
    /* number of test cases */
    unsigned short int t;
	string hasil[110];
    cin >> t;
    for(int i=0; i < t; i++) { //loops for each case
		hasil[i] = fungsi();
		//cout << coba[1][1]  <<endl;
    }
	for(int c = 0 ; c < t ; c++){
		cout << "Case #"  << c+1 << ": " << hasil[c] << endl;
	}
    return 0;
}
string fungsi(){
	unsigned short int r_volunter , r_penyihir , row_volunter[4][4] , row_penyihir[4][4] , cocok = 0 ;
	string angka;
	stringstream convert; 
	//Digunakan Untuk Input Baris ke 1
	cin  >> r_volunter ;
	for (int zeile=0; zeile<4; zeile++) {
		for (int spalte=0; spalte<4; spalte++) {
                cin >> row_volunter[zeile][spalte];
		}
    }
	//Digunakna untuk input baris ke 2
	cin  >> r_penyihir ;
	for (int zeile=0; zeile<4; zeile++) {
		for (int spalte=0; spalte<4; spalte++) {
                cin >> row_penyihir[zeile][spalte];
		}
    }
	//Digunakan Untuk mencookkan Angka nya
	for(int x = 0 ; x < 4 ; x++){ // Untuk Array Ke 1
		for(int y = 0 ; y < 4 ; y++){ // Untuk array ke 2
			if(row_volunter[r_volunter-1][x] == row_penyihir[r_penyihir-1][y]){
				convert << row_volunter[r_volunter-1][x];
				angka = convert.str();
				cocok++;
			}
		}
	}
	if(cocok == 1 ){
		return angka;
	}else if(cocok > 1){
		return "Bad magician!";
	}else{
		return "Volunteer cheated!";
	}	
}