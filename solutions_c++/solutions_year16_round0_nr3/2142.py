#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <set>
#include <string>
#include <vector>
using namespace std;

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	cin >> n;
	int k, num;
	cin >> k >> num;
	vector<int> mas(k);
	for (int i = 0; i < k; i++) {
		mas[i] = 0;
	}
	vector<pair<int, int> > first;
	for (int i = 1; i < k-2; i+=2) {
		for (int j = i + 2; j< k -1;  j+=2) {
			if (i != j) first.push_back(make_pair(i, j));
		}
	}
	vector<pair<int, int> > second;
	for (int i = 2; i < k - 2; i += 2) {
		for (int j = i + 2; j< k - 1; j += 2) {
			if (i != j) second.push_back(make_pair(i, j));
		}
	}
	cout << "Case #1:"<<endl;
	mas[0] = 1;
	mas[k-1] = 1;
	while(true) {
		for (int i = 0; i < first.size(); i++) {
			for (int j = 0; j < second.size(); j++) {
				mas[first[i].first] = 1;
				mas[first[i].second] = 1;
				mas[second[j].first] = 1;
				mas[second[j].second] = 1;
				for (int o = 0; o < mas.size(); o++) {
					cout << mas[o];
				}
				cout << " 3 2 3 2 7 2 3 2 3" << endl;
				num--;
				if (num == 0) return 0;
				mas[first[i].first] = 0;
				mas[first[i].second] = 0;
				mas[second[j].first] = 0;
				mas[second[j].second] = 0;
			}
		}
	}
	return 0;
}