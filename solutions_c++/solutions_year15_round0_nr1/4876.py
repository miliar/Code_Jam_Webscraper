/*
 * ovation.cpp
 *
 *  Created on: 10/04/2015
 *      Author: JoséIgnacio
 */

#include <iostream>

using namespace std;

int main(){
	int testCases;
	cin >> testCases;

	int shyMax, genteParada, colados;
	string audience;

	for(int numberTest = 0; numberTest < testCases; numberTest++){
		cin >> shyMax >> audience;
		genteParada = colados = 0;

		int i = 0;
		while(i <= shyMax){

			if(genteParada < i){
				genteParada++;
				colados++;
			}
			genteParada += (audience[i++] - '0');
		}

		cout << "Case #" << numberTest+1 << ": " << colados << endl;

	}

	return 0;
}


