#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

struct MyPair {
	int number;
	string name;
};

int myCompareFunc(MyPair a, MyPair b) {
	return a.number > b.number;
}

bool checkEmpty(vector<MyPair> &P) {
	for (int i = 0; i < P.size(); i++) {
		if (P.at(i).name.length() > 0)
			return false;
	}
	return true;
}

vector<string> processInput(vector<MyPair> &P) {
	vector<string> answer;
	while (!checkEmpty(P)) {
		sort(P.begin(), P.end(), myCompareFunc);

		string _pair = "";

		if (P.size() >= 3 && P.at(0).name.length() == 1 && P.at(1).name.length() == 1 && P.at(2).name.length() == 1) {
			_pair.push_back(P.at(0).name.at(0));
			P.at(0).name.pop_back();
			P.at(0).number--;
		}
		else if (P.size() >= 2 && P.at(0).name.length() == 1 && P.at(1).name.length() == 1) {
			_pair.push_back(P.at(0).name.at(0));
			P.at(0).name.pop_back();
			P.at(0).number--;
			_pair.push_back(P.at(1).name.at(0));
			P.at(1).name.pop_back();
			P.at(1).number--;
		}
		else {
			for (int i = 0; i < P.size(); i++) {
				if (_pair.length() >= 2)
					break;
				if (P.at(i).name.length() > 0) {
					_pair.push_back(P.at(i).name.at(0));
					P.at(i).name.pop_back();
					P.at(i).number--;
				}
			}
		}
		answer.push_back(_pair);
	}
	return answer;
}

int main(void) {
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int N;
		cin >> N;
		vector<MyPair> P;
		for (int j = 0; j < N; j++) {
			MyPair _P;
			cin >> _P.number;
			for (int k = 0; k < _P.number; k++)
				_P.name.push_back('A' + j);
			P.push_back(_P);
		}

		//for (int j = 0; j < N; j++)
		//	cout << P.at(j).number << " " << P.at(j).name << endl;

		vector<string> answer = processInput(P);

		cout << "Case #" << i + 1 << ":";
		for (int j = 0; j < answer.size(); j++) {
			cout << " " << answer.at(j);
		}
		cout << endl;
	}
	
	//system("pause");
	return 0;
}