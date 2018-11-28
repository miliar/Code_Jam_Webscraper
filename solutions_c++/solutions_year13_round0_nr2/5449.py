/*
 * main.cpp
 *
 *  Created on: 13.04.2013
 *      Author: HP-User
 */

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main() {
	ifstream inFile("input.txt");
	int t,m,n;
	vector<vector<int> > field;
	vector<bool> outcome, ok;

	inFile>>t;
	ok.resize(4);

	for (int index=0;index<t;index++) {
		inFile>>m;
		inFile>>n;

		field.resize(m);
		for (unsigned int i=0;i<field.size();i++) {
			field[i].resize(n);
		}

		for (unsigned int i=0;i<field.size();i++) {
			for (int j=0;j<field[i].size();j++) {
				inFile>>field[i][j];
			}
		}


		outcome.push_back(true);

		for (unsigned int i=0;i<field.size();i++) {
			for (unsigned int j=0;j<field[i].size();j++) {
				ok[0]=true;
				ok[1]=true;

				for (int indi=0;indi<field.size();indi++) {
					if (field[indi][j]>field[i][j])
						ok[0]=false;
				}
				for (int indi=0;indi<field[i].size();indi++) {
					if (field[i][indi]>field[i][j])
						ok[1]=false;
				}

				if ((!ok[0])&&(!ok[1])) {
					outcome[index]=false;
				}

				if (!outcome[index])
					break;
			}
			if (!outcome[index])
				break;
		}
	}

	inFile.close();

	ofstream outFile("output.txt");
	for (int i=0;i<t;i++) {
		if (outcome[i]) {
			outFile<<"Case #" << i+1 <<": YES" << endl;
		} else {
			outFile<<"Case #" << i+1 <<": NO" << endl;
		}
	}

	outFile.close();

	return 0;
}
