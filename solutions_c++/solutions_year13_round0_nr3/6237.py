#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>
#include <math.h>
#include <map>
using namespace std;

string IntToString(int number)
{
  stringstream ss;
  ss << number;
  return ss.str();
}
int fair(int n) {
	string tmp = IntToString(n);

	int d = tmp.length() / 2.0;
	for (int i = 0; i < tmp.length() / 2.0; i++) {
		if (tmp[i] != tmp[tmp.length()-1-i]) return 0;
	}

	return 1;
}
int square(int n) {
	int tmp = (int)sqrt((double)n);
	if (tmp * tmp == n) {
		// 平方根もpalindromeでなければならない
		if (fair(tmp) == 1) {
			return 1;
		} else {
			return 0;
		}
	} else {
		return 0;
	}
}
int main(void)
{
	//ifstream cin("C-sample.txt");
	ifstream cin("C-small-attempt0.in");
	ofstream ofs("C-small-attempt0.out");

	int debug = 121;//12321;
	int d = square(debug);//fair(debug);

	int T = 0, A, B, count;
	cin >> T;
	cin.ignore();
	for (int i = 0; i < T; i++) {
		count = 0;
		cin >> A;
		cin >> B;

		// fairかつsquareかチェックする
		for (int j = A; j <=B; j++) {
			if (j == 484) {
				cout << "" << flush;
			}

			if (fair(j) == 1 && square(j) == 1) {//121,484,676
				count++;
			}
		}

		//ofs << count << endl;
		ofs << "Case #" << i+1 << ": " << count << endl;
	}

	return 0;
}