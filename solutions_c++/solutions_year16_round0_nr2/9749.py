#include <iostream>
using namespace std;

int pancake(string& cake) {		
	char sign;
	int count = 1;
	if (cake.size() == 1)
	  return cake[0] == '+' ? 0 : 1;
	sign = cake[0];
	for (int i = 1; i < cake.size(); i++) {
		while (i < cake.size() && cake[i] == cake[i - 1]) i++;
		if (i < cake.size()) {
			sign = cake[i];
			count++;
		}
	}
	if (sign == '+') count--;
	return count;
}
int main(int argc, char *argv[]) {
	int numCase;
	cin >> numCase;
	
	for (int i = 1; i <= numCase; ++i) {
		string cake;
		cin >> cake;
		cout << "Case #" << i << ": " << pancake(cake) << endl;
	}
	return 0;
}
