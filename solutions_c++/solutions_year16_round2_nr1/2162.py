#include<iostream>
#include<fstream>
#include<string>
#include<vector>

using namespace std;

int main() {

	ifstream ifs("Text.txt");
	int numCases;
	ifs >> numCases;

	for (int nc = 0; nc < numCases; nc++) {
		vector<int> v(10, 0);
		string s;
		size_t t;
		ifs >> s;
		t = s.find("Z");
		while (t != string::npos) {
			v[0] ++;
			s.erase(t, 1);
			t = s.find("E");
			s.erase(t, 1);
			t = s.find("R");
			s.erase(t, 1);
			t = s.find("O");
			s.erase(t, 1);
			t = s.find("Z");
		}
		t = s.find("W");
		while (t != string::npos) {
			v[2] ++;
			s.erase(t, 1);
			t = s.find("T");
			s.erase(t, 1);
			t = s.find("O");
			s.erase(t, 1);
			t = s.find("W");
		}
		t = s.find("X");
		while (t != string::npos) {
			v[6] ++;
			s.erase(t, 1);
			t = s.find("S");
			s.erase(t, 1);
			t = s.find("I");
			s.erase(t, 1);
			t = s.find("X");
		}
		t = s.find("G");
		while (t != string::npos) {
			v[8] ++;
			s.erase(t, 1);
			t = s.find("E");
			s.erase(t, 1);
			t = s.find("I");
			s.erase(t, 1);
			t = s.find("H");
			s.erase(t, 1);
			t = s.find("T");
			s.erase(t, 1);
			t = s.find("G");
		}
		t = s.find("H");
		while (t != string::npos) {
			v[3] ++;
			s.erase(t, 1);
			t = s.find("T");
			s.erase(t, 1);
			t = s.find("R");
			s.erase(t, 1);
			t = s.find("E");
			s.erase(t, 1);
			t = s.find("E");
			s.erase(t, 1);
			t = s.find("H");
		}
		t = s.find("U");
		while (t != string::npos) {
			v[4] ++;
			s.erase(t, 1);
			t = s.find("F");
			s.erase(t, 1);
			t = s.find("O");
			s.erase(t, 1);
			t = s.find("R");
			s.erase(t, 1);
			t = s.find("U");
		}
		t = s.find("F");
		while (t != string::npos) {
			v[5] ++;
			s.erase(t, 1);
			t = s.find("I");
			s.erase(t, 1);
			t = s.find("V");
			s.erase(t, 1);
			t = s.find("E");
			s.erase(t, 1);
			t = s.find("F");
		}
		t = s.find("V");
		while (t != string::npos) {
			v[7] ++;
			s.erase(t, 1);
			t = s.find("S");
			s.erase(t, 1);
			t = s.find("E");
			s.erase(t, 1);
			t = s.find("E");
			s.erase(t, 1);
			t = s.find("N");
			s.erase(t, 1);
			t = s.find("V");
		}
		t = s.find("O");
		while (t != string::npos) {
			v[1] ++;
			s.erase(t, 1);
			t = s.find("N");
			s.erase(t, 1);
			t = s.find("E");
			s.erase(t, 1);
			t = s.find("O");
		}
		t = s.find("N");
		while (t != string::npos) {
			v[9] ++;
			s.erase(t, 1);
			t = s.find("I");
			s.erase(t, 1);
			t = s.find("N");
			s.erase(t, 1);
			t = s.find("E");
			s.erase(t, 1);
			t = s.find("N");
		}

		cout << "Case #" << nc + 1 << ": ";
		for (int i = 0; i < 10; i++) {
			while (v[i] > 0) {
				cout << i;
				v[i]--;
			}
		}
		cout << endl;


	}

}