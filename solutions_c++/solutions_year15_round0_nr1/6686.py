#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <iomanip>
using namespace std;

int main() {
	ifstream ifs;
	ifs.open("ProblemA.in");
	ofstream ofs;
	ofs.open("ProblemA.out");
	int cases;
	ifs >> cases;
	for (int i = 1; i <= cases; i++) {
		int maxShy;
		ifs >> maxShy ;
		vector<int> people;
		for (int j = 0; j <= maxShy; j++) {
			char temp;
			ifs >> temp;
			people.push_back(int(temp) - 48);
		}
		int peopleUp = 0;
		int peopleNeeded = 0;
		for (int k = 0; k <= maxShy; k++) {
			if (people[k] > 0) {
				if (peopleUp >= k) {
					peopleUp += people[k];
				}
				else {
					peopleNeeded += (k - peopleUp);
					peopleUp += (k - peopleUp) + people[k];
				}
			}
			people[k];
		}
		ofs << "Case #" << i << ": " << peopleNeeded << endl;
	}
	ifs.close();
	ofs.close();
}