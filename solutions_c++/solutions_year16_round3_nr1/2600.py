#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

void printArr(vector<int> &p) {
	for (int i = 0; i < (int)p.size(); i++) {
		cout << p[i] << " ";
	}
	cout << endl;
}

string cutLine(vector<int> &p) {
	string str = "";
	vector<int>::iterator maxEl = max_element(p.begin(), p.end());
	int counter = 0;
	while (*maxEl > 0) {
		map<int, int> mymap;
		int inx = maxEl - p.begin();

		for (int i = 0; i < (int)p.size(); i++) {
			mymap[p[i]]++;
		}

		map<int, int>::reverse_iterator rit = mymap.rbegin();
		if (rit->second == 1 && mymap[rit->first - 1] > 0) {
			(*maxEl)--;
			counter += 2;
			str += string(1, 'A' + inx) + " ";
		}
		else if (rit->second == 1 && mymap[rit->first - 1] == 0) {
			(*maxEl) -= 2;
			str += string(2, 'A' + inx) + " ";
			counter+=2;
		}
		else if (rit->second == 3) {
			(*maxEl)--;
			str += string(1, 'A' + inx) + " ";
			counter+=2;
		}
		else {
			(*maxEl)--;
			str += string(1, 'A' + inx);
			maxEl = max_element(p.begin(), p.end());
			(*maxEl)--;
			inx = maxEl - p.begin();
			str += string(1, 'A' + inx) + " ";
			counter+=2;
		}
		maxEl = max_element(p.begin(), p.end());
	}
	//std::cout << str << std::endl;
	return str;
}

int main() {
	int t; cin >> t;
	for (int i = 0; i < t; i++) {
		int n; cin >> n;
		vector<int> p(n);
		for (int j = 0; j < n; j++) {
			cin >> p[j];
		}
		std::cout << "Case #" << i + 1 << ": " << cutLine(p)<< std::endl;
	}
}
