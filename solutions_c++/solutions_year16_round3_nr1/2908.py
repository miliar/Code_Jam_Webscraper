#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int max(vector<pair<int, int> > p){
	int n = p.size();
	int m = 0;
	for (int i = 0; i < n; i++){
		m = max ( m, p[i].first);
	}
	return m;
}

int main(){
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++){
		int n;
		cin >> n;
		vector<pair<int, int> > p(n);
		int common = 0;
		for (int j = 0; j < n; j++){
			cin >> p[j].first;
			p[j].second = j;
			common += p[j].first;
		}
		cout << "Case #" << i + 1 << ": ";
		while (common > 0){
			int takeOne = -1;
			for (int j = 0; j < n; j++){
				if (p[j].first == 0){
					continue;
				}
				p[j].first--;
				int m = max(p);
				p[j].first++;
				if (m <= (common-1) / 2){
					takeOne = j;
					break;
				}
			}

			int takeTwo1 = -1, takeTwo2 = -1;
			bool fl = 0;
			for (int j = 0; j < n && !fl; j++){
				if (p[j].first == 0){
					continue;
				}
				for (int k = 0; k < n; k++){
					if (p[j].first == 0){
						continue;
					}
					p[j].first--;
					p[k].first--;
					int m = max(p);
					p[j].first++;
					p[k].first++;
					if (m <= (common-2) / 2){
						takeTwo1 = j;
						takeTwo2 = k;
						fl = 1;
						break;
					}
				}
			}
			if (takeTwo1 != -1 && takeTwo2 != -1){
				p[takeTwo1].first--;
				p[takeTwo2].first--;
				cout << (char)('A' + p[takeTwo1].second) << (char)('A' + p[takeTwo2].second) << ' ';
				common -= 2;
			}
			else{
				p[takeOne].first--;
				cout << (char)('A' + p[takeOne].second) << ' ';
				common--;
			}
		}
		cout << endl;
	}
	return 0;
}