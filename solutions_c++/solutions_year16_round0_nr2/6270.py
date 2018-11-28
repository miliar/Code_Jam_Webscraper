#include <iostream>
#include <fstream>
// #include <map>

using namespace std;


string flip(string a, int index) {
	for (int i = 0; i <= index; i++) {
		if (a[i] == '+')
			a[i] = '-';
		else if (a[i] == '-')
			a[i] = '+';
	}
	return a;
}

string findpos_flip(string a) {
	int i = 0;
	while (a[i] == '+')
		i++;
	i--;
	return flip(a, i);
}


string f_last_neg_flip(string a) {
	for (int i = a.size()-1; i >= 0; i--) {
		if (a[i]=='-')
			return flip(a, i);
	}
	return a;
}

bool check(string a) {
	for (int i = 0; i < a.size(); i++) {
		if (a[i] == '-')
			return false;
	}
	return true;
}
int main() {
	ifstream file("2input.txt");
	int times;
	file >> times;
	for (int i = 0; i < times; i++) {
		cout << "Case #" << i +1 << ": ";
		string a;
		file >> a;
		// a = flip(a, 4);
		int j =0;
		while (!check(a)) {
			if (a[0] == '+') {
				a =findpos_flip(a);
				j++;
			}
			// cout << a << "ss\n";
			a = f_last_neg_flip(a);
			j++;
			// cout << a << "\n";
		}



		cout << j << "\n";
	}
}