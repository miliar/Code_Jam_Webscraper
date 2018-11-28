/*
 * pancake.cxx
 * 
 * Copyright 2016 Antonio <salvata@ubuntu>
 * 
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 * 
 * 
 */


#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>

using namespace std;

bool testPrimeNumber(unsigned long long int number, unsigned long long int *divisor) {
		*divisor = 0;
		if(number > 3) {
			//Calculate the square root
			unsigned long long int root = sqrt(number);
			for(unsigned long long int i = 2; i <= root; i++) {
				unsigned long long int modulo = number%i;
				if(modulo == 0) {
					*divisor = i;
					return true;//The number is not prime
				}
			}	
			return false;//The number is prime		
		}
		else {
			return false;
		}
}



unsigned long long int convertToRealValue(vector<unsigned int> *coinTentativeArray,unsigned int base) {
	unsigned long long int realValue = 0;
	int p = 0;
	for(int i = (*coinTentativeArray).size() - 1; i >= 0; i--) {
		unsigned int currentValue = (*coinTentativeArray)[i];
		if(currentValue != 0) {
			realValue += pow(base, p);
		}
		p++;
	}
	return realValue;
}

void addOneMiddleArray(vector<unsigned int> *coinArray, int lengthCoins);


void findTentativeCoin(vector< vector<unsigned int>*> *confirmArray, vector<vector<unsigned int>*> *divisorArray, int lengthCoins, int numberCoins) {
	//Second rule, por digits must be zero or 1
	vector<unsigned int> *coinTentantiveArray = new vector<unsigned int> (lengthCoins,0);
	//First rule for this type of coins
	(*coinTentantiveArray)[0] = 1;
	(*coinTentantiveArray)[coinTentantiveArray->size()-1] = 1;
	
	//Tentative vector for divisors
	vector<unsigned int> *divisorArrayTentative = new vector<unsigned int>;
	
	//Start testing with free for coins
	if(lengthCoins > 2) {
		while(numberCoins > 0) {
			for(int p =2; p <= 10; p++) {
				//Convert coin tentative array to real value
				unsigned long long int value = convertToRealValue(coinTentantiveArray,p);
				bool result = false;
				unsigned long long int divisor = 0;
				result = testPrimeNumber(value, &divisor);
				if(result == true) { //The number is not prime in that base
					(*divisorArrayTentative).push_back(divisor);
					if(p == 10) { //The coin is completely valid =)
							//Move the array to valid, request new memory spaces for the next one if needed
							(*confirmArray).push_back(coinTentantiveArray);
							(*divisorArray).push_back(divisorArrayTentative);
							vector<unsigned int> *tempVector = (*confirmArray).back();
							coinTentantiveArray = new vector<unsigned int> (lengthCoins,0);
							(*coinTentantiveArray) = (*tempVector); 
							divisorArrayTentative = new vector<unsigned int>;
							numberCoins--;
							addOneMiddleArray(coinTentantiveArray, lengthCoins); //Move to the next coin
					}
				}
				else {
					//The number is prime in a base, clear everything for next step
					(*divisorArrayTentative).clear();
					//Add 1 to the coin Tentative array
					addOneMiddleArray(coinTentantiveArray, lengthCoins);
					break;
				}
			}
		}
	}
	else {
			confirmArray = NULL;
			divisorArray = NULL;
			return;//Couldn't find any, 11 is not a valid coin
	}
}

void addOneMiddleArray(vector<unsigned int> *coinArray, int lengthCoins) {
	unsigned int middleLength = lengthCoins - 2;//Rule 2, MSB and LSP are 1s
	unsigned long long int value  = 0;
	unsigned int base;
	unsigned int power = 0;
	for(int i = (*coinArray).size()-2; i > 0; i--) {
		base = 2*(*coinArray)[i];
		if(base > 0) {
			value += pow(base, power);
		}
		power++;
	}
	//Add 1 to this new valie
	value++;
	//Convert back to an array
	unsigned long long int mask = 1;
	for(int i = (*coinArray).size()-2; i > 0; i--) {
		unsigned int store = value & mask;
		if(store > 0) {
			(*coinArray)[i] = 1;
		}
		else {
			(*coinArray)[i] = 0;
		}
		mask = mask << 1;
	}
}


int main(int argc, char **argv)
{
	//Get the number of cases
	int cases = 0;
	cin >> cases;

	//Vectors to store confirm coins and tentative
	vector<vector<unsigned int>*> coinConfirmArray;
	vector<vector<unsigned int>*> divisorArray;
	
	int numberCoins; 
	int lengthCoins;
	
	//cout << "The number of cases is " << cases << endl;
	for(int i = 1; i <= cases; i++) {
			//Fill the pancake array
			cin >> lengthCoins;
			cin >> numberCoins;
			
			//cout << "The length of the coins is " << lengthCoins << endl;
			//cout << "The number of coins is " << numberCoins << endl;
			
			//Go to the method who finds the 
			findTentativeCoin(&coinConfirmArray, &divisorArray, lengthCoins, numberCoins);
			
			cout << "Case #" << i << ":" << endl;
			//Print the values found in the array
			if(&coinConfirmArray != NULL && &divisorArray != NULL) {
				for(int k=0; k < coinConfirmArray.size(); k++) {
					vector<unsigned int> *array = coinConfirmArray[k];
					for(int j = 0; j < array->size(); j++) {
						cout << (*array)[j];
					}
					cout << " ";
					array = divisorArray[k];
					for(int j = 0; j < array->size(); j++) {
						cout << (*array)[j];
						cout << " ";
					}
					cout << endl;
				}
			}
			//FIXME-TODO : Not cleaning vectors per test case, not mind the memory leaking
			coinConfirmArray.clear();
			divisorArray.clear();
	}
	
	return 0;
}


