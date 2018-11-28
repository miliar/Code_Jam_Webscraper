#include <iostream>

using namespace std;

int main(int, char**) {
	int nb_tests;
	cin >> nb_tests;
	for (int test_i = 1; test_i <= nb_tests; ++test_i) {
    int smax;
    char digit_c;
    cin >> smax;
    ////cerr << smax << "  ";
    int nb = 0;
    int nb_missing = 0;
    for (int i = 0; i <= smax; i++) {
      cin >> digit_c;
      int digit = digit_c - '0';
      //cerr << "i: " << i << endl;
      //cerr << "digit " << digit << endl;
      //cerr << "nb " << nb << endl;
      if (digit > 0) {
        int total = nb + nb_missing;
        if (total < i) {
          nb_missing += i - total;
        }
        nb += digit;
      }
      //cerr << "missing " << nb_missing << endl;
      //cerr << "nb2 " << nb << endl;
    }
    //cerr << endl;

		cout << "Case #" << test_i << ": " << nb_missing  << endl;
	}
}
