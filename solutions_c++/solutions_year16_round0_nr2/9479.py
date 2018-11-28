#include <iostream>
#include <string>
#include <vector>

using namespace std;

int solver(vector<char> cakes) {
	int flip = 0;
	//if the last one is -, add one final movement to flip all of them.
	if (cakes.back() == '-')
		flip++;
	//flip from the top one (if needed)
	char prev = cakes[0];
	for (int i = 1; i < cakes.size(); i++) {
		if (cakes[i] != prev) {
			flip++;
			prev = cakes[i];
		}
	}
	return flip;
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

