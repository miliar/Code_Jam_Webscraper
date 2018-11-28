#include<fstream>
#include<iostream>
#include<vector>
#include<unordered_map>
#include<string>

using namespace std;

int main() {
	int t, tmp, ans, cnt, ret;
	unordered_map<int, vector<int> > arrangment;

	ifstream cin("A-small-attempt2.in", fstream::in);
	ofstream cout("out.out", fstream::out);

	if (!cin) return 1;
	cin >> t;
	for (int i = 0; i < t; i++) {
		arrangment.clear();
		for (int j = 0; j < 2; j++) {
			cin >> ans;
			for (int k = 0; k < ans - 1; k++){
				for (int h = 0; h < 4; h++) cin >> tmp;
			}
			for (int k = 0; k < 4; k++){
				cin >> tmp;
				arrangment[j].push_back(tmp);
			}
			for (int k = 0; k < 4 - ans; k++){
				for (int h = 0; h < 4; h++) cin >> tmp;
			}
		}

		cnt = 0;
		for (auto it1 = arrangment[0].begin(); it1 != arrangment[0].end(); it1++) {
			for (auto it2 = arrangment[1].begin(); it2 != arrangment[1].end(); it2++) {
				if (*it1==*it2){
					ret = *it1;
		     			cnt++;
				}
			}
		}

		cout << "Case #" << i + 1 << ": ";
		switch (cnt) {
		case 0:
			cout << "Volunteer cheated!";
			break;
		case 1:
			cout << ret;
			break;
		case 2:
		case 3:
		case 4:
			cout << "Bad magician!";
		}
		cout << endl;
	}

	return 0;
}