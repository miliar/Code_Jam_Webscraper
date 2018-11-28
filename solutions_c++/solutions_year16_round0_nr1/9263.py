#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

void findValue(int n) {
	bool seen[10] = {false,false,false,false,false,false,false,false,false,false};
	int index = 1;
	int value = 1;
	while (true) {
			value = index++ * n;
			if (index > 2 && (value == n)) {
				cout << "INSOMNIA\n";
				return;
			}

			//cout << value << '\n';
			int copy = value;
			while (copy > 0) {
				int digit = copy % 10;
				//cout << digit << '\n';
				seen[digit] = true;
		 		copy /= 10;
		 		if (accumulate(seen, seen + 10, 0) == 10) {
		 			cout << value << '\n';
		 			return;
		 		}
			}
		}
}

int main(int argc, char *argv[])
{
	string line = "";
	int caseNum = 1;
	getline(cin,line);
	while (getline(cin, line)) {
		cout << "Case #" + to_string(caseNum++) + ": ";
		int n = stoi(line);
		findValue(n);
	}
}