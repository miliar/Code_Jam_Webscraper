/*
 * pancake.cpp
 *
 *  Created on: 10/04/2015
 *      Author: JoséIgnacio
 */

#include <iostream>
#include <string>
#include <list>

using namespace std;

struct quaternion{
	string value;

	quaternion(){
		value = "1";
	}

	void multiply(char letter){
		if(value == "1"){
			switch(letter){
				case 'i': value = "i";	break;
				case 'j': value = "j";	break;
				case 'k': value = "k";	break;
			}
		} else if(value == "-1"){
				switch(letter){
					case 'i': value = "-i";	break;
					case 'j': value = "-j";	break;
					case 'k': value = "-k";	break;
				}
		} else if(value == "i") {
				switch(letter){
					case 'i': value = "-1";	break;
					case 'j': value = "k";	break;
					case 'k': value = "-j";	break;
				}
		} else if(value == "-i") {
				switch(letter){
					case 'i': value = "1";	break;
					case 'j': value = "-k";	break;
					case 'k': value = "j";	break;
				}
		} else if(value == "j") {
				switch(letter){
					case 'i': value = "-k";	break;
					case 'j': value = "-1";	break;
					case 'k': value = "i";	break;
				}
		} else if(value == "-j") {
				switch(letter){
					case 'i': value = "k";	break;
					case 'j': value = "1";	break;
					case 'k': value = "-i";	break;
				}
		} else if(value == "k") {
				switch(letter){
					case 'i': value = "j"; 	break;
					case 'j': value = "-i";	break;
					case 'k': value = "-1";	break;
				}
		} else if(value == "-k") {
				switch(letter){
					case 'i': value = "-j"; 	break;
					case 'j': value = "i";	break;
					case 'k': value = "1";	break;
				}
		} else value = "";
	}
};

int main(){
	int testCases;
	cin >> testCases;

	int characters, times;
	char actualChar;
	string string;
	for(int ncase =  0; ncase < testCases; ncase++){
		cin >> characters >> times;
		cin >> string;

		quaternion first, second, third;

		list<char> toRead;

		for(int i = 0; i < characters*times; i++){

			if(toRead.empty()){
				for(int j = 0; j < characters; j++){
					toRead.push_back(string[j]);
				}
			}

			actualChar = toRead.front();
			toRead.pop_front();

			if(first.value != "i") first.multiply(actualChar);
			else if(second.value != "j") second.multiply(actualChar);
			else third.multiply(actualChar);

		}

		if(first.value == "i" && second.value == "j" && third.value == "k"){
			cout << "Case #" << ncase+1 << ": YES" << endl;
		} else{
			cout << "Case #" << ncase+1 << ": NO" << endl;
		}


	}

	return 0;
}


