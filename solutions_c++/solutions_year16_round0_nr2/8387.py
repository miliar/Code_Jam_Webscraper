#include <iostream>
#include<string>
using namespace std;



int main()
{
	int t;
	cin >> t;

	for (int X = 1; X <= t; X++) {
		string s;
		cin >> s;
		char shd = '+';
		int mc = 0;
		for (int i = s.size() - 1; i >= 0; i--) {
			if (s[i] != shd) {
				mc++;
				shd = (shd == '+') ? '-' : '+';
			}
		}
		cout << "Case #" << X << ": " << mc << endl;
	}
    return 0;
}


