/*
 * so.cxx
 *
 *  Created on: Apr 11, 2015
 *      Author: abcc
 */


#include <string>
#include <vector>
#include <iostream>
#include <iterator>
#include <string>
#include <fstream>
#include <cstdlib>

using namespace std;

int main()
{

	int NumofCases;
	std::vector<int> retV;

	ifstream infile ("A-small-attempt.in");
	if (infile.is_open()) {
		string caseNum;
		getline(infile, caseNum);
		NumofCases = atoi(caseNum.c_str());

		for ( int num = 0; num < NumofCases; ++num ) {
			// for every case
			string line;
			getline(infile, line);

			int people = line.at(0)- '0';

			int len = line.length();
			string subline = line.substr(2,len);

			int totalneed = 0;		// total people needed
			int sum = 0;		// the people already
			int k = 0;			// position, k, also the people needed for k position
			while ( k < len -2 ) {
				int ksum = subline.at(k) - '0'; // the people of k
				if ( ( ksum > 0) && ( k > sum)) {
					int kneed =  k -sum;
					if ( kneed > totalneed ) {
						totalneed = kneed;
					}
				}
				sum += ksum ;
				k++;
			}
			std::cout << std::endl;
			retV.push_back(totalneed);
		}
	}

	ofstream outfile ("A-small-attemp.out");
	if (outfile.is_open()) {
		int i = 1;
		std::vector<int>::iterator it;
		for ( it = retV.begin(); it != retV.end(); ++it ) {

			outfile << "Case #" << i << ": ";
			if ( *it == -1 ) {
				outfile  <<"Bad magician!" << std::endl;
			} else if ( *it == -2 ) {
				outfile <<"Volunteer cheated!" << std::endl;
			} else {
				outfile << *it << std::endl;
			}
			++i;
		}
	    outfile.close();
	}
	else {
		std::cout << "Unable to open file";
	}

	return 0;
}



