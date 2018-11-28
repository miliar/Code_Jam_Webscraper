/*
 * main.cpp
 *
 *  Created on: Mar 22, 2015
 *      Author: Dusty
 *
 *  Notes:
 *  	Input will have 2000 circuits, 12000 jugglers, 6 J/C
 *  	Est. 10 circuits per juggler
 *  	Conservative est. of 60 jugglers possible per circuit, gives ~50,000,000 possibilities per circuit
 *  	~1x10^11 total possible combinations
 */
//Includes
#include <iostream>
#include <fstream>
#include <list>
#include <algorithm>
#include <stdlib.h>

using namespace std;

//Global Vars
int numTestCases=0;
int peopleStanding = 0;
int maxShyness = 0;
int currentShyness = 0;
int peopleAdded = 0;
char tempChar;
int tempInt;

list<int> people;
//Functions

//Main
int main() {
	//Import Data
    //Get number of Test cases
    ifstream infile;
    infile.clear();
    infile.open("A-Large.in");
    infile >> numTestCases;
    int solution[numTestCases];
	ofstream outfile;
outfile.open("LargeCase.out");
    for(int i=0; numTestCases > i; i++ ) {
		peopleStanding = 0;
		maxShyness = 0;
		currentShyness = 0;
		peopleAdded = 0;
		people.clear();
		infile >> maxShyness;
		//Get rid of space
		infile.get();
		//Add people to list;
		for(int j=0; j<=maxShyness; j++ ){
    		tempChar = infile.get();
       		tempInt = tempChar - '0';
       		people.push_back(tempInt);
	   }
		
		while( !people.empty() ) {
			if(currentShyness > peopleStanding) {
				peopleAdded++;
				peopleStanding++;
			}
			tempInt = people.front();
//cout << "TempInt is: " << tempInt << endl;		
			people.pop_front();
			peopleStanding += tempInt;
//cout << "PeopleStanding is: " << peopleStanding << endl;
//cout << "CurrentShyness is: " << currentShyness << endl;
			currentShyness++;
		}
		
		solution[i]=peopleAdded;
		cout << "Case #" << i+1 << ": " << solution[i] << endl;
		outfile << "Case #" << i+1 << ": " << solution[i] << endl;
    }
	

}
