#include <iostream>
#include <string>
#include <vector>

using namespace std;


string clearInput (string input) {
	int index = input.size() - 1;
	while (input[index] == '+' && input.size() > 1)
		input.erase(index--, 1);

	for (int i = 0; i < input.size() - 1; i++) {
		if (input[i] == input[i + 1]) {
			input.erase(i, 1);
			i = -1;
		}
	}
	return input;
}


int main () {
	unsigned int T;

	cin >> T;
	string N[T];
	for (unsigned int i = 0; i < T; i++)
		cin >> N[i];
	string tmp;
	for (unsigned int i = 0; i < T; i++) {
		cout << "Case #" << i + 1 << ": ";
		tmp = clearInput(N[i]);
		if (tmp.compare("+") == 0)
			cout << 0 << endl;
		else cout << tmp.size() << endl;
	}


}