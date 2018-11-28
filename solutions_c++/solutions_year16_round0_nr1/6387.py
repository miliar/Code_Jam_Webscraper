// ConsoleApplication2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


#include <iostream>
#include <math.h>
#include <algorithm> 
#include <string>
#include <fstream>

using namespace std;

int main()
{
	ofstream myfile;
	myfile.open("example.txt");


	int n = 0, counter = 0;
	cin >> n;
	while (counter < n)
	{
		int r;
		cin >> r;
		if (r == 0){
			myfile << "Case #" << (1 + counter) << ": INSOMNIA"<<endl;
			++counter; 
			continue;
		}
			

		bool digits[10] = { false };

		bool awake = true; 
		int iter = 1; //first N * 1
		while (awake){
			int newNum; 
			string num = to_string(newNum = (r * iter++) );
			for (int i = 0; i < num.length(); ++i){
				digits[num[i]-48] = true; //look at the numbers
			}
			bool allTrue = true; 
			for (int x = 0; x < 10; x++){
				if (!digits[x]){
					allTrue = false;
					break;
				}
			}
			if (allTrue){
				myfile << "Case #" << (1 + counter) << ": " << newNum<< endl; 
				break; 
			}
		}


		++counter;
	}

	myfile.close();
	return 0;
}
