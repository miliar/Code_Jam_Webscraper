#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <stack>
#include <queue>
#include <set>
#include <map>
using namespace std;

void A(){
	int N;
	cin >> N;
	vector<pair<int, int>> P(N);
	for (int i = 0; i < N; i++) {
		int tmp;
		cin >> tmp;
		P[i] = { i, tmp };
	}
	while (!P.empty())
	{
		sort(P.begin(), P.end(), [](pair<int, int> x, pair<int, int> y){
			return x.second>y.second;
		});
		if (P.size() == 2){
			if (P[0].second == P[1].second){
				P[0].second--; P[1].second--;
				string s="AB";
				s[0] = 'A' + P[0].first;
				s[1] = 'A' + P[1].first;
				cout << s << " ";
			}
			else if (P[0].second == P[1].second + 1){
				P[0].second--;
				string s = "A";
				s[0] = 'A' + P[0].first;
				cout << s << " ";
			}
			else {
				P[0].second-=2;
				string s = "AB";
				s[0] = s[1] = 'A' + P[0].first;
				cout << s << " ";
			}
		}
		else{
			if (P[0].second == 1){
				P[0].second--;
				string s = "A";
				s[0] = 'A' + P[0].first;
				cout << s << " ";
			}
			else if (P[0].second == P[1].second){
				P[0].second--; P[1].second--;
				string s = "AB";
				s[0] = 'A' + P[0].first;
				s[1] = 'A' + P[1].first;
				cout << s << " ";
			}
			else{
				P[0].second -= 2;
				string s = "AB";
				s[0] = s[1] = 'A' + P[0].first;
				cout << s << " ";
			}
		}
		
		if (P[1].second == 0) P.erase(P.begin() + 1);
		if (P[0].second == 0) P.erase(P.begin());

	} 
}
void B(){
}
void C(){
	int N;
	cin >> N; cin.ignore(INT_MAX, '\n');
	set<string> top1, top2;
	set<string> real;
	int count = 0;
	for (int i = 0; i < N; i++){
		string str;
		getline(cin, str);
		int split = str.find(' ');
		string t1 = str.substr(0, split);
		string t2 = str.substr(split + 1, str.length() - split - 1);
		if (top1.count(t1) && top2.count(t2) && !real.count(str)) count++;
		top1.insert(t1); top2.insert(t2); real.insert(str);
	}
	cout << count;
}
void D(){
	int K, C, S;
	cin >> K >> C >> S;
	if (C*S < K){
		cout << "IMPOSSIBLE";
		return;
	}
	long long tmp = 0;
	for (int k = 0; k < K; k++){
		tmp = tmp*K + k;
		if (k + 1 == K || k%C == C - 1){
			cout << tmp + 1 << " ";
			tmp = 0;
		}
	}
}

int main(){
	int T;
	cin >> T; cin.ignore(INT_MAX, '\n');
	for (int t = 1; t <= T; ++t) {
		cout << "Case #" << t << ": ";
		A();
		cout << endl;
	}
	return 0;
}
