/*
 * sheep.cxx
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

using namespace std;



void obtainDigits(int caseNumber,int processNumber,vector<int>* array) {
	//cout << "The value of process Number is " << processNumber << endl;
	int threshold = 1000000;//For now 1 million
	for(int i = 1; i <= threshold; i++) {
		int numberIn = processNumber;
		numberIn *= i;
		while(numberIn > 0) {
			//Divide between 10 and keep storing the values
			int digit = numberIn % 10;
			//Attempt to input number if it is not repeated
			if( !(std::find(array->begin(), array->end(), digit) != array->end()) ) {//Not contained
				//cout << "Pushing a digit for " << numberIn << endl;
				//cout << "The digit is " << digit << endl;
				array->push_back(digit);
			}
			//Check if it has number from 0 to 9
			if(array->size() == 10) {
				cout << "Case #" << caseNumber << ": " << processNumber*i << endl;
				return;
			}
			numberIn /= 10;
		}						
	}
	cout << "Case #" << caseNumber << ": INSOMNIA" << endl;
}



int main(int argc, char **argv)
{
	//Get the number of cases
	int cases = 0;
	cin >> cases;

	//Vector to store the seen number
	vector<int> seenNumberArray;

	
	//cout << "The number of cases is " << cases << endl;
	int N = 0;
	int multiplier = 0;
	for(int i = 1; i <= cases; i++) {
			//Get the number to start
			cin >> N;
			//Go to method to get all the digits until a threshold number
			obtainDigits(i,N,&seenNumberArray);
			seenNumberArray.clear();
	}
	
	return 0;
}

