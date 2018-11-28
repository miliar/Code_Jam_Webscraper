#include <iostream>
#include <climits>
#include <vector>
#include <string>
#include <cmath>
using namespace std;

int count_diff(string first, string second){
	if (first == second) return 0;
	int moves = 0;
	vector<pair<char,int> > t; 
	t.push_back(pair<char,int>(first[0], 1));
	for (int i = 1; i < first.length(); i++){
		if (first[i]==first[i-1]){
			t[t.size()-1].second++;
		} else {
			t.push_back(pair<char,int>(first[i],1));
		}
	}

	vector<pair<char,int> > w;
	w.push_back(pair<char,int>(second[0],1));
	for (int i = 1; i < second.length(); i++){
		if (second[i]==second[i-1]){
			w[w.size()-1].second++;
		} else {
			w.push_back(pair<char,int>(second[i],1));
		}
	}
	if (t.size() != w.size()) return -1;
	for (int i = 0; i < t.size(); i++){
		if (t[i].first != w[i].first) return -1;
		moves += (abs(t[i].second-w[i].second));
	}
	return moves;
}

int main(){
	int T; cin >> T;
	for (int tst = 1; tst <= T; tst++){
		int N; cin >> N;
		vector<string> arr; arr.resize(N);
		int min_len = 110;
		for (int i = 0; i < N; i++){
			string s;
			cin >> s;
			arr[i] = s;
			int len = s.length();
			min_len = min(min_len, len);
		}
		vector<string> smallest;
		bool impossible = false; 
		int min_moves = INT_MAX;
		for (int i = 0; i < N && !impossible; i++){
			string change_to = arr[i];
			int moves = 0;
			for (int j = 0; j < N; j++){
				int diff = count_diff(change_to, arr[j]);
				if (diff < 0){
					impossible = true;
					break;
				} else {
					moves += diff;
				}
			}
			min_moves = min(min_moves, moves);
		}

		if (impossible){
			cout << "Case #" << tst << ": Fegla Won" << endl;
		} else {
			cout << "Case #" << tst << ": " << min_moves << endl;
		}
	}

	return 0;
}