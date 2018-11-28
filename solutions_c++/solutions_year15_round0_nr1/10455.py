
#include <fstream>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string>

using namespace std;

int main(int argc, char *argv[]){

	int numCases, maxS, acc, fri;
	string sShy;
	cin >> numCases;

	for (int i = 0; i < numCases; i++){

		cin >> maxS >> sShy;

		acc = 0;
		fri = 0;

		for (int j = 0; j < maxS + 1; j++){

			int num = sShy[j] - '0';

			if (num > 0){
				if (acc >= j){
					acc += num;
				}
				else {
					while (acc != j){
						fri++;
						acc++;
					}
					acc += num;
				}
			}
		}

		cout << "Case #" << i + 1 << ": " << fri << "\n";
	}

}
