#include <iostream>
#include <string>

using namespace std;

void flipUtil(string &s, int left, int right) {
	for (int ptr = left; ptr <= right; ++ptr) {
		s[ptr] = (s[ptr] == '+') ? '-' : '+';  
	}
}

int flip(string &s) {

	int right = s.length()-1;
	int count = 0;

	while (right >= 0) {

		while (right >= 0 && s[right] == '+') right--;
		if (right == -1) return count;

		flipUtil(s, 0, right);
		right--;
		count++;

	}
	
	return count;
}

int main(int argc, char const *argv[])
{
	int test_num;

	cin >> test_num;

	for (int t = 1; t <= test_num; ++t) {

		string s;
		cin >> s;

		cout << "Case #" << t << ": " << flip(s) << endl;

	}

	return 0;
}