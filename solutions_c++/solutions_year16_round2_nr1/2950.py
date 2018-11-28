#include <iostream>
#include <string>
#include <map>
#include <set>

using namespace std;

int arr [] = {5, 4, };

string associate(int i) {
	switch (i) {
		case 0:
			return "ZERO";
		case 1:
			return "ONE";
		case 2:
			return "TWO";
		case 3:
			return "THREE";
		case 4:
			return "FOUR";
		case 5:
			return "FIVE";
		case 6:
			return "SIX";
		case 7:
			return "SEVEN";
		case 8:
			return "EIGHT";
		case 9:
			return "NINE";
		default:
			return "";
	}
}

void printMap(map<char, int> &mymap) {
	for (map<char, int>::iterator it = mymap.begin(); it != mymap.end(); ++it) {
		std::cout << it->first << " " << it->second << endl;
	}
	std::cout << std::endl;
}

void dec(map<char, int> &mymap, int i) {
	string num = associate(i);
	for (int i = 0; i < (int)num.size(); i++) {
		mymap[num[i]]--;
	}
}

void exists(map<char, int> &mymap, map<int, int> &tel) {
	while (mymap['Z'] > 0) {
		dec(mymap, 0);
		tel[0]++;
	}
	while(mymap['W'] > 0) {
		dec(mymap, 2);
		tel[2]++;
	}
	while(mymap['U'] > 0) {
		dec(mymap, 4);
		tel[4]++;
	}
	while(mymap['X'] > 0) {
		dec(mymap, 6);
		tel[6]++;
	}
	while(mymap['G'] > 0) {
		dec(mymap, 8);
		tel[8]++;
	}
	while(mymap['F'] > 0) {
		dec(mymap, 5);
		tel[5]++;
	}
	while(mymap['H'] > 0) {
		dec(mymap, 3);
		tel[3]++;
	}
	while(mymap['S'] > 0) {
		dec(mymap, 7);
		tel[7]++;
	}
	while(mymap['O'] > 0) {
		dec(mymap, 1);
		tel[1]++;
	}
	while(mymap['I'] > 0) {
		dec(mymap, 9);
		tel[9]++;
	}
}

int main() {
	int n; cin >> n;
	for (int i = 0; i < n; i++) {
		string str; cin >> str;
		map<char, int> mymap;
		for (int j = 0; j < (int)str.size(); j++) {
			mymap[str[j]]++;
		}
		map<int, int> tel;
		exists(mymap, tel);
		cout << "Case #" << i + 1 << ": ";
		for (map<int, int>::iterator it = tel.begin(); it != tel.end(); ++it) {
			int t = it->second;
			while (t > 0) {
				cout << it->first;
				t--;
			}
		}
		std::cout << std::endl;
	}
}
