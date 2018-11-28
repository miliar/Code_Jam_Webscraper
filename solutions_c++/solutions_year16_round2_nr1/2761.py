#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
using namespace std;

string decrypt(string& str) {
	vector<int> v_int;
	int pos;
	while ((pos = str.find('Z')) != string::npos) {
		str.erase(pos, 1);
		str.erase(str.find('E'), 1);
		str.erase(str.find('R'), 1);
		str.erase(str.find('O'), 1);
		v_int.push_back(0);
	}
	while ((pos = str.find('W')) != string::npos) {
		str.erase(pos, 1);
		str.erase(str.find('T'), 1);
		str.erase(str.find('O'), 1);
		v_int.push_back(2);
	}
	while ((pos = str.find('X')) != string::npos) {
		str.erase(pos, 1);
		str.erase(str.find('S'), 1);
		str.erase(str.find('I'), 1);
		v_int.push_back(6);
	}
	while ((pos = str.find('S')) != string::npos) {
		str.erase(pos, 1);
		str.erase(str.find('E'), 1);
		str.erase(str.find('V'), 1);
		str.erase(str.find('E'), 1);
		str.erase(str.find('N'), 1);
		v_int.push_back(7);
	}
	while ((pos = str.find('V')) != string::npos) {
		str.erase(pos, 1);
		str.erase(str.find('F'), 1);
		str.erase(str.find('I'), 1);
		str.erase(str.find('E'), 1);
		v_int.push_back(5);
	}
	while ((pos = str.find('F')) != string::npos) {
		str.erase(pos, 1);
		str.erase(str.find('O'), 1);
		str.erase(str.find('U'), 1);
		str.erase(str.find('R'), 1);
		v_int.push_back(4);
	}
	while ((pos = str.find('O')) != string::npos) {
		str.erase(pos, 1);
		str.erase(str.find('N'), 1);
		str.erase(str.find('E'), 1);
		v_int.push_back(1);
	}
	while ((pos = str.find('R')) != string::npos) {
		str.erase(pos, 1);
		str.erase(str.find('T'), 1);
		str.erase(str.find('H'), 1);
		str.erase(str.find('E'), 1);
		str.erase(str.find('E'), 1);
		v_int.push_back(3);
	}
	while ((pos = str.find('N')) != string::npos) {
		str.erase(pos, 1);
		str.erase(str.find('I'), 1);
		str.erase(str.find('N'), 1);
		str.erase(str.find('E'), 1);
		v_int.push_back(9);
	}
	while (str.size() > 0) {
		str.erase(str.find('E'), 1);
		str.erase(str.find('I'), 1);
		str.erase(str.find('G'), 1);
		str.erase(str.find('H'), 1);
		str.erase(str.find('T'), 1);
		v_int.push_back(8);
	}
	sort(v_int.begin(), v_int.end());
	ostringstream oss;
	for (int i = 0; i < v_int.size(); ++i) {
		oss << v_int[i];
	}

	return oss.str();
}

int main(int argc, char const *argv[])
{
	int T;
	cin >> T;
	string S;
	int phoneNumber;
	for (int c = 0; c < T; ++c) {
		cin >> S;
		cout << "Case #" << c + 1 << ": " << decrypt(S) << endl;
	}
	return 0;
}
