#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int smax, standing = 0, diff = 0, j = 1;
		cin >> smax;
		string shy;
		cin >> shy;
		standing = ((int) shy[0])-48;
		while (j < shy.size()) {
			if (((int) shy[j])-48 == 0) {
				j++;
				continue;
			}
			if (standing < j) {
				diff += j-standing;
				standing += j;
			}
			standing += ((int) shy[j])-48;
			j++;
		}
		cout << "Case #" << (i+1) << ": " << diff << "\n";
	}
}	
