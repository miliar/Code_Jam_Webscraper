#include <iostream>
#include <algorithm>

using namespace std;

int main(int argc, char const *argv[]) {
	int nTestCases;
	cin >> nTestCases;

	for (int i = 0; i < nTestCases; ++i) {
		int nParties;
		cin >> nParties;

		int nPeople[nParties];
		int nTotal = 0;
		for (int pId = 0; pId < nParties; ++pId) {
			cin >> nPeople[pId];
			nTotal += nPeople[pId];
		}

		cout << "Case #" << i+1 << ": ";
		while (nTotal > 0) {
			int* maxAddr1 = max_element(nPeople, nPeople+nParties);
			int maxIdx1 = maxAddr1 - nPeople;
			char c1 = maxIdx1 + 'A';
			nPeople[maxIdx1]--;
			nTotal--;

			int* maxAddr2 = max_element(nPeople, nPeople+nParties);
			int maxIdx2 = maxAddr2 - nPeople;
			char c2 = maxIdx2 + 'A';
			nPeople[maxIdx2]--;
			nTotal--;

			int* maxAddr3 = max_element(nPeople, nPeople+nParties);
			int maxIdx3 = maxAddr3 - nPeople;
			if (nPeople[maxIdx3]*2 > nTotal) {
				nPeople[maxIdx2]++;
				nTotal++;
				cout << c1 << " ";	
			} else {
				cout << c1 << c2 << " ";
			}
		}

		cout << endl;	
	}

	return 0;
}