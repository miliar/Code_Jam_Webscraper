// GCodeJam_Round1.cpp : Defines the entry point for the console application.
//

#include <fstream>
#include <iostream>
#include <string>
#include <stdio.h>
#include <map>
#include <unordered_map>
#include <vector>
#include <math.h>

using namespace std;

typedef pair<unsigned char, int> ChPair;
typedef pair<unsigned char, double> ChPairDouble;

int main(int argc, char * argv[])
{
	ifstream ifile;
	ofstream outfile;
	ifile.open("input.txt");
	outfile.open("result.txt");
	if(!ifile.is_open() || !outfile.is_open())
		return 0;

	int T, N;
	ifile >> T;
	for(int i = 0 ; i < T ; i++) {
		ifile >> N;

		vector<string> inputs;
		string inp;
		for(int j = 0 ; j < N ; j++) {
			ifile >> inp;
			inputs.push_back(inp);
		}

		string testSame = inputs[0];
		bool bSame = true;
		for(int j = 1 ; j < N ; j++) {
			if(testSame.compare(inputs[j]) != 0) {
				bSame = false;
			}
		}
		if(bSame) {
			cout << "Case #" << i + 1  << ": 0" << endl;
			outfile << "Case #" << i + 1  << ": 0" << endl;
			continue;
		}

		// string check
		vector<vector<ChPair> *> allSets;
		for(int j = 0 ; j < N ; j++) {
			vector<ChPair> * sets = new vector<ChPair>;
			string strAtJ = inputs[j];
			for(size_t j = 0 ; j < strAtJ.length() ; j++) {
				unsigned char ch = strAtJ[j];

				size_t k = j;
				for( ; k < strAtJ.length() && strAtJ[j] == strAtJ[k] ; k++) {
				}

				sets->push_back(ChPair(ch, k - j));
				j = k - 1;
			}

			allSets.push_back(sets);
		}
		bool felgaWon = false;

		for(size_t j = 0 ; j < allSets.size() ; j++) {
			vector<ChPair> *sets = allSets.at(j);
			if(sets->size() != allSets.at(0)->size())
				felgaWon = true;
		}

		size_t maxSize = 0;
		for(size_t j = 0 ; j < allSets.size() ; j++) {
			vector<ChPair> * sets = allSets.at(j);
			if(sets->size() > maxSize)
				maxSize = sets->size();
		}

		vector<ChPairDouble> avgRepeats;
		
		for(size_t j = 0 ; j < maxSize && felgaWon == false; j++) {
			// set max size for each item.
			double avg = -1;
			vector<ChPair> * sets = allSets[0];
			ChPair ch = sets->at(j);
			char charToCompare = ch.first;
			avg = ch.second;
			for(size_t k = 1 ; k < allSets.size() ; k++) {
				vector<ChPair> * sets = allSets.at(k);
				ChPair ch = sets->at(j);
				if(charToCompare != ch.first) {
					felgaWon = true;
					break;
				}
				
				avg += ch.second;

			}
			if(felgaWon) break;

			avg /= allSets.size();
			avgRepeats.push_back(ChPair(charToCompare, avg));
		}

		// now get the difference from max.
		if(felgaWon) {
			cout << "Case #" << i + 1  << ": Fegla Won" << endl;
			outfile << "Case #" << i + 1 << ": Fegla Won" << endl;
		}
		else {
			size_t sum = 0;

			for(size_t k = 0;  k < allSets.size() ; k++) {
				for(size_t j = 0 ; j < avgRepeats.size() ; j++) {
					vector<ChPair> * sets = allSets.at(k);
					double tmp = abs(avgRepeats[j].second - (double)sets->at(j).second);
					sum += (size_t) floor(tmp + 0.5);
				}

			}

			cout << "Case #" << i + 1 << ": " << sum << endl;
			outfile << "Case #" << i + 1 << ": " << sum << endl;
		}

	}


	return 0;
}

