/*
 * pc.cxx
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
#include <sstream>

using namespace std;

int main()
{

	int NumofCases;
	std::vector<int> retV;

	ifstream infile ("B-large.in");
	if (infile.is_open()) {
		string caseNum;
		getline(infile, caseNum);
		NumofCases = atoi(caseNum.c_str());

		for ( int num = 0; num < NumofCases; ++num ) {
			// for every case
			string dinersline;
			getline(infile, dinersline);
			int dinners = atoi(dinersline.c_str());		// dinners with non-empty paltes

			std::vector<int> v;
			std::string line;
			getline(infile, line);
			std::stringstream strstr(line);

			// use stream iterators to copy the stream to the vector
			//	as whitespace separated strings
			std::istream_iterator<std::string> it(strstr);
			std::istream_iterator<std::string> end;
			std::vector<std::string> results(it, end);
			std::vector<std::string>::iterator sit1;

			for ( sit1 = results.begin(); sit1 != results.end(); ++sit1 ) {
				v.push_back(atoi((*sit1).c_str()));
			}

			int mint = 1000;
			for ( int k = 1; k < 1001; ++k ) {
				int time = 0;
				std::vector<int>::iterator iit;
				for ( iit = v.begin(); iit != v.end(); ++iit ) {

					time += (*iit -1)/k;
				}
				std::cout << std::endl;
				time += k;
				if ( time < mint)
					mint = time;
			}

			std::vector<int>::iterator iit;

			// set the test result
		retV.push_back(mint);
		std::cout << std::endl;
		}
	}

	ofstream outfile ("B-large.out");
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


