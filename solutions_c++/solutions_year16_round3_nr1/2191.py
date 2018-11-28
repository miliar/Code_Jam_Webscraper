#include <iostream>
#include <fstream>
#include <string>

using namespace std;

//don't worry - be happy :)

int main()
{
	ifstream in("input.txt");
	ofstream out("output.txt");


	int nTests;
	in >> nTests;
	
	for (int t = 1; t <= nTests; t++) {
		int nParties;
		in >> nParties;

		int eachParty[26];

		for (int i = 0; i < nParties; i++) {
			in >> eachParty[i];
		}
		
		int maxCount = eachParty[0], iOfMax = 0;
		for (int i = 0; i < nParties; i++) {
			if (eachParty[i] > maxCount) {
				maxCount = eachParty[i];
				iOfMax = i;
			}
		}
		int countOfMax;
		out << "Case #" << t << ": ";
		while (maxCount > 0) {
			countOfMax = 0;
			for (int i = 0; i < nParties; i++) {
				if (eachParty[i] == maxCount) {
					countOfMax++;
				}
			}
			out << char(iOfMax + 65);
			eachParty[iOfMax]--;			
			if (countOfMax % 2 == 0) {
				bool isFound = false;
				for (int i = 0; i < nParties; i++) {
					if ((eachParty[i] == maxCount) && (iOfMax != i)) {
						out << char(i + 65);
						eachParty[i]--;
						isFound = true;
						break;
					}
				}
				if (!isFound && eachParty[iOfMax] != 0) {
					out << char(iOfMax + 65);
					eachParty[iOfMax]--;
				}
			}
			out << " ";
			maxCount = 0;
			for (int i = 0; i < nParties; i++) {
				if (eachParty[i] > maxCount) {
					maxCount = eachParty[i];
					iOfMax = i;
				}
			}
		}
		out << endl;
	}
	return 0;
}