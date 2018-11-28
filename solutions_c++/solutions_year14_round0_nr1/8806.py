#include <vector>
#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T, i, j;
	int FirstAns, SecondAns;
	vector<int> temp(4);
	vector<int> FirstArr(4), SecondArr(4);
	vector<int> Sol(4);
	
	cin >> T;
	for (i = 1; i <= T; i++) {
		Sol.clear();
		cin >> FirstAns;
		for (j = 0; j < 4; j++) {
			if (j == FirstAns - 1) {
				cin >> FirstArr[0] >> FirstArr[1] >> FirstArr[2] >> FirstArr[3];
			}
			else cin >> temp[0]>>temp[1]>>temp[2]>>temp[3];
		}

		cin >> SecondAns;
		for (j = 0; j < 4; j++) {
			if (j == SecondAns - 1) {
				cin >> SecondArr[0] >> SecondArr[1] >> SecondArr[2] >> SecondArr[3];
				for each (int card in FirstArr)
				{
					for each (int c in SecondArr)
					{
						if (card.Equals(c)) Sol.insert(Sol.begin(), c);
					}
				}
			}
			else cin >> temp[0] >> temp[1] >> temp[2] >> temp[3];
		}

		cout << "Case #" << i << ": ";

		if (Sol.size() == 0)
			cout << "Volunteer cheated!";
		else if (Sol.size() > 1)
			cout << "Bad magician!";
		else cout << Sol[0];
		
		cout << endl;
	}

	fcloseall();
}