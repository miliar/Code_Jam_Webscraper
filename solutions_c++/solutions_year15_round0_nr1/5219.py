#include <iostream>
#include <vector>

using namespace std;


int main(int argc, char* argv[]) {
	string shyness;
	int smax;
	int tests;
	int count = 1;

	cin >> tests;

	while (count <= tests) {
		cin >> smax >> shyness;
		unsigned int numFriends = 0;
		unsigned int currentlyUp = 0;
		vector<int> shychars(shyness.begin(), shyness.end());
		for (auto it = shychars.begin(); it != shychars.end(); ++it)
			*it -= 48;
		for (auto i : shychars) {
			currentlyUp += i;
			if (currentlyUp == 0)
				numFriends++;
			if (currentlyUp > 0)
				currentlyUp -= 1;
		}
		cout << "Case #" << count << ": " << numFriends << endl;
		count++;
	}

	//vector<Int> = read_input()
	return 0;
}