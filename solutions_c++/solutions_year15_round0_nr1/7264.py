#include <iostream>
#include <string>

using namespace std;

int main() {
	int TC;
	cin >> TC;

	string s;
	getline(cin, s);
	for (int _ = 0; _ < TC; _++) {
		int MaxShy, counter = 0, ans = 0; string Shyness;
		getline(cin, s);

		MaxShy = atoi(s.substr(0,s.find(" ")).c_str());
		//cout << MaxShy << endl;

		Shyness = s.substr(s.find(" ") + 1, s.size());
		//cout << Shyness << endl;

		for (int i = 0; i <= MaxShy; i++)
		{
			if (counter >= i) {
				counter += (Shyness[i] - '0');
			}
			else {
				ans += (i - counter);
				counter += (i - counter);
				counter += (Shyness[i] - '0');			
			}
		}

		cout << "Case #" << _ + 1 << ": " << ans << endl;
	}
}