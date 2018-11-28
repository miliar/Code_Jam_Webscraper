#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
	unsigned int T, iter, a, currentCard;
	cin >> T;
	string result;
	iter = 0;
	while (iter++ < T) {
		vector <int> rowOne, intersect;
		cin >> a;
		int i,x;
		for (i = 0; i < 16; ++i) {
			if ((i / 4) == a - 1) {
				cin >> currentCard;
				rowOne.push_back(currentCard);
				continue;
			}
			cin >> currentCard;
		}
		cin >> a;
		for (i = 0; i < 16; ++i) {
			if ((i / 4) == a - 1) {
				cin >> currentCard;
				for (x = 0; x < 4; ++x)
				{
					if (rowOne[x] == currentCard) 
					{
						intersect.push_back(currentCard);
						break;
					}
				}
				continue;
			}
			cin >> currentCard;
		}
		int inSize = intersect.size();
		result = (inSize > 1) ? "Bad magician!" : ((inSize == 0) ? "Volunteer cheated!" : to_string(intersect[0]));
		cout << "Case #" << iter << ": " << result << endl;
	}
	return EXIT_SUCCESS;
}