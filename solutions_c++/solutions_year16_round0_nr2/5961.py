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

using namespace std;



int flipPancakeArray(vector<bool>* array) {
	//Follow algorithm, start from the end, and flip everything a - is seen
	int size = array->size() -1;
	int numIterations = 0;
	while(true) {
		if(size == -1) {
			return numIterations;
		}
		//cout << "The value of array size is " << (*array)[size] << endl;
		if((*array)[size] == false) {
				//Flip the whole array starting from size coordinate
				//cout << "Flipping the array in coordinate " << size << endl;
				for(int p = size; p >= 0; p--) {
					(*array)[p] = !(*array)[p];
				}
				numIterations++;
		}
		size--;
	}
}


void fillPancakeArray(vector<bool> *array) {
	string nextChar;
	cin >> nextChar;
	//cout << "The next char is " << nextChar << endl;
	int i = 0;
	while(true) {
		if(nextChar[i] != '\0') {
			switch (nextChar[i]) {
				case '+' : 
					//cout << "Introduced a +" << endl;
					array->push_back(true);
					break;
				case '-':
					//cout << "Introduced a -" << endl;
					array->push_back(false);
					break;
				default:
						cout << "An error happened, different character when parsing pancake array" << endl;
						exit(1);
			}
		}
		else {
			return;
		}
		i++;
	}
}
int main(int argc, char **argv)
{
	//Get the number of cases
	int cases = 0;
	cin >> cases;

	//Vector to store the seen number
	vector<bool> pancakeArray;
	//TRUE stands for +
	//FALSE stands for -
	
	//cout << "The number of cases is " << cases << endl;
	int N = 0;
	int multiplier = 0;
	for(int i = 1; i <= cases; i++) {
			//Fill the pancake array
			fillPancakeArray(&pancakeArray);
			//Go to method in order to flip the array accordingly
			int numIterations = flipPancakeArray(&pancakeArray);
			cout << "Case #" << i << ": " << numIterations << endl;
			//Clear the pancake array for the next iteration
			pancakeArray.clear();
			
	}
	
	return 0;
}

