#include <iostream>
#include <string>
#include <vector>

using namespace std;

int solver(vector<char> cakes) {
	int flipped = 0;
	if (cakes.back() == '-')
		flipped++;
	char prev = cakes[0];
	for (int i = 1; i < cakes.size(); i++) {
		if (cakes[i] != prev) {
			flipped++;
			prev = cakes[i];
		}
	}
	return flipped;
}
int main()
{
        string str;
        getline(cin, str);
        int n = stoi(str);
        for (int k = 0; k < n; k++) {
                getline(cin, str);
		vector<char> cakes;
                int alineSize = str.length();
		for (int j = 0; j < alineSize; j++) {
                        cakes.push_back(str[j]);
		}
		cout << "Case #" << k+1 << ": " << solver(cakes) << endl;
	}

    return 0;
}
