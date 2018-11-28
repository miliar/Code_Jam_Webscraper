#include <iostream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

int main()
{
	int c;
	cin >> c;
	for (int cc = 1; cc <= c; cc++) {
		int K, C, S;
		cin >> K >> C >> S;
		cout << "Case #" << cc << ": 1";
		for (int i = 2; i <= S; i++)
			cout << " " << i;
		cout << endl;
	}
}