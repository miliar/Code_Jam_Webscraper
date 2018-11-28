#include"stdafx.h"
#include<iostream>
#include<fstream>
#include<string>
#include<algorithm>
using namespace std;

int main()
{
	ifstream infile;
	ofstream outfile;

	int testCase,  i, number,numIter,number_orig;
	string numString;
	char temp;
	/*number = 2345;
	numString = to_string(number);
	cout << numString << endl<<numString.size()<<endl;
	numString = numString + '9';
	int c = numString.find("8");
	cout << c << endl;
	cout << numString << endl << numString.size() << endl;
	number = stoi(numString);
	cout << number << endl;
	cin >> i;*/
	
	infile.open("A-large.in");
	outfile.open("A-large-output.out");

	infile >> testCase;
	//testCase = 1;
	for (int iter = 0; iter<testCase; iter++){
		//cout << "iteration" << endl;
		infile >> number_orig;
		//number_orig = 1692;
		number = number_orig;
		numString = to_string(number);
		//cout << numString << " given" << endl;
		string digits = "";
		
		for ( numIter = 1; numIter<100; numIter++){
			//cout << "iteration " << numIter << endl;
			for ( i = 0; i<numString.size() ; i++){
				temp = numString[i];
				if (digits.find(temp)==string::npos){
					digits = digits + temp;
					//cout << digits <<" update"<< endl;
				}
			}
			number = stoi(numString);
			number =number_orig* (numIter+1);
			numString = to_string(number);
			if (digits.size() == 10){
				break;
			}
		}
		outfile << "Case #" << iter+1 << ": ";
		if (numIter == 100){
			outfile << "INSOMNIA" << endl;
		}
		else{
			outfile << numIter*number_orig << endl;
		}

	}

	infile.close();
	outfile.close();
	getchar();
	return 0;
}
