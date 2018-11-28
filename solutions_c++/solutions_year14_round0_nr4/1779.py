#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int calculateWar(vector <double> naomiBlockWeights, vector <double> kenBlockWeights);
int calculateDeceitfulWar(vector <double> naomiBlockWeights, vector <double> kenBlockWeights);

int main(int argc, char const *argv[])
{
	int testCases;
	cin >> testCases;

	for (int i=0; i<testCases; i++) {
		int numberOfBlocks;
		cin >> numberOfBlocks;

		vector <double> naomiBlockWeights;
		vector <double> kenBlockWeights;
		double input;

		for (int j=0; j<numberOfBlocks; j++) {
			cin >> input;
			naomiBlockWeights.push_back(input);
		}
		for (int j=0; j<numberOfBlocks; j++) {
			cin >> input;
			kenBlockWeights.push_back(input);
		}

		int pointsWar = calculateWar(naomiBlockWeights, kenBlockWeights);
		int pointsDeceitfulWar = calculateDeceitfulWar(naomiBlockWeights, kenBlockWeights);

		cout << "Case #" << i + 1 << ": " << pointsDeceitfulWar << " " << pointsWar << endl;
	}

	return 0;
}

int calculateWar(vector <double> naomiBlockWeights, vector <double> kenBlockWeights)
{	
	//Sort (Small to largest)
	sort(naomiBlockWeights.begin(), naomiBlockWeights.end());
	sort(kenBlockWeights.begin(), kenBlockWeights.end());

	int naomiPoints = 0;

	for (int i=0; i<naomiBlockWeights.size(); i++) {
		double chosenNaomi = naomiBlockWeights[naomiBlockWeights.size() - 1 - i];
		if (chosenNaomi > kenBlockWeights[kenBlockWeights.size()-1]) { //Chosen Naomi wins
			naomiPoints++;
			kenBlockWeights.erase(kenBlockWeights.begin());
		} 
		else {
			kenBlockWeights.pop_back();
		}
	}

	return naomiPoints;
}

int calculateDeceitfulWar(vector <double> naomiBlockWeights, vector <double> kenBlockWeights)
{
	//Sort (Small to largest)
	sort(naomiBlockWeights.begin(), naomiBlockWeights.end());
	sort(kenBlockWeights.begin(), kenBlockWeights.end());

	int naomiPoints = 0;

	while (naomiBlockWeights.size() > 0) {
		double chosenNaomi = naomiBlockWeights[naomiBlockWeights.size() - 1];
		if (chosenNaomi > kenBlockWeights[kenBlockWeights.size()-1]) { //Chosen Naomi wins
			naomiPoints++;
			naomiBlockWeights.pop_back();
			kenBlockWeights.pop_back();
		} 
		else {
			naomiBlockWeights.erase(naomiBlockWeights.begin());
			kenBlockWeights.pop_back();
		}
	}

	return naomiPoints;
}