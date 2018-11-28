// ConsoleApplication2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


#include <iostream>
#include <math.h>
#include <algorithm> 
#include <string>
#include <fstream>

using namespace std;

string flip(string & newString){
	reverse(newString.begin(), newString.begin()); //reverse string 
	for (int i = 0; i < newString.length(); ++i){
		if (newString[i] == '+')
			newString[i] = '-';
		else
			newString[i] = '+';
	}
	return newString; 
}
int main()
{
	ofstream myfile;
	myfile.open("example.txt");


	int n = 0, counter = 0;
	cin >> n;
	while (counter < n)
	{
		string r;
		cin >> r;
		int flips = 0; 

		while (1){
			if (r.find("-") == string::npos)//no minuses, only way to get out of this loop 
				break; 

			int length = r.length(); 
			for (int x = 0; x < length; ++x){//removes last occurences of +'s
				if (r[length - 1 - x] == '+'){
					r.pop_back(); 
				}
				else{
					break; 
				}

			}
			//'-'
			if (r[0] == '-'){
				flip(r); 
				++flips;
				continue; 
			}
			else{
				int d = 0; 
				while (1){
					if (r[d] == '+')
						r[d] = '-';
					else
						break; 
					++d; 
				}
				++flips;
			}


				


		}

		myfile << "Case #" << (1 + counter) << ": " << flips << endl; 



		++counter;
	}

	myfile.close();
	return 0;
}
