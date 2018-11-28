//============================================================================
// Name        : super_number.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <map>
using namespace std;


map <char, int> znaki;

int main() {
	int t;
	cin >> t;
	for(int tests = 0; tests < t; ++tests){
		string s;
		znaki.clear();
		cin >> s;
		for(auto it = s.begin(); it!= s.end(); ++it){
			++znaki[*it];
		}
		int ile[10];
		for(int i=0; i<10; ++i)ile[i]=0;
		int ile_tej;


		//zera
		ile_tej = znaki['Z'];
		znaki['Z']-=ile_tej;
		znaki['E']-=ile_tej;
		znaki['R']-=ile_tej;
		znaki['O']-=ile_tej;
		ile[0] = ile_tej;
		//szostki
		ile_tej = znaki['X'];
		znaki['S']-=ile_tej;
		znaki['I']-=ile_tej;
		znaki['X']-=ile_tej;
		ile[6] = ile_tej;
		//siodemki
		ile_tej = znaki['S'];
		znaki['S']-=ile_tej;
		znaki['E']-=ile_tej;
		znaki['V']-=ile_tej;
		znaki['E']-=ile_tej;
		znaki['N']-=ile_tej;

		ile[7] = ile_tej;
		//osemki
		ile_tej = znaki['G'];
		znaki['E']-=ile_tej;
		znaki['I']-=ile_tej;
		znaki['G']-=ile_tej;
		znaki['H']-=ile_tej;
		znaki['T']-=ile_tej;
		ile[8] = ile_tej;
		//piatki
		ile_tej = znaki['V'];
		znaki['F']-=ile_tej;
		znaki['I']-=ile_tej;
		znaki['V']-=ile_tej;
		znaki['E']-=ile_tej;
		ile[5] = ile_tej;
		//czworki
		ile_tej = znaki['F'];
		znaki['F']-=ile_tej;
		znaki['O']-=ile_tej;
		znaki['U']-=ile_tej;
		znaki['R']-=ile_tej;
		ile[4] = ile_tej;
		//trojki
		ile_tej = znaki['R'];
		znaki['T']-=ile_tej;
		znaki['H']-=ile_tej;
		znaki['R']-=ile_tej;
		znaki['E']-=ile_tej;
		znaki['E']-=ile_tej;
		ile[3] = ile_tej;
		//dwojki
		ile_tej = znaki['W'];
		znaki['T']-=ile_tej;
		znaki['W']-=ile_tej;
		znaki['O']-=ile_tej;
		ile[2] = ile_tej;
		//jedynki
		ile_tej = znaki['O'];
		znaki['O']-=ile_tej;
		znaki['N']-=ile_tej;
		znaki['E']-=ile_tej;
		ile[1] = ile_tej;
		//dziewiatki
		ile_tej = znaki['I'];
		znaki['N']-=ile_tej;
		znaki['I']-=ile_tej;
		znaki['N']-=ile_tej;
		znaki['E']-=ile_tej;
		ile[9] = ile_tej;
		cout << "Case: #" << tests+1 << ": ";
		for(int i=0; i<10; ++i)
			for(int j=0; j<ile[i]; ++j)
				cout << i;
		cout << "\n";

	}
	return 0;
}
