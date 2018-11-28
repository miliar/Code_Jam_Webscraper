#include <iostream>
#include <queue>
#include <string>
#include <unordered_set>
#include <algorithm>

#define ll long long

using namespace std;


bool allHappy(string s) {
	for (char c : s)
		if (c == '-')
			return false;
	return true;
}

string flip(int i, string s) {
	string s1 = s.substr(0, i);
	string s2 = s.substr(i);
	reverse(s1.begin(), s1.end());
	for (int i = 0; i < s1.size(); i++) {
		if (s1[i] == '+')
			s1[i] = '-';
		else s1[i] = '+';
	}
	return (s1 + s2);
}

ll N(string pat) {
	unordered_set<string> v;
	if (allHappy(pat))
		return 0;
	queue<string> q, q2;
	q.push(pat);
	v.insert(pat);
	ll num = 0;
	while(!q.empty()) {
		while (!q.empty()) {
			string s = q.front();
			q.pop();
			for (ll i = 0; i < s.size(); i++) {
				string temp = flip(i+1, s);
				if (v.find(temp) == v.end()) { 
					q2.push(temp);
					v.insert(temp);				
				}
			}
		}
		num++;
		while (!q2.empty()) {
			if (allHappy(q2.front()))
				return num;	
			q.push(q2.front());
			q2.pop();
		}
	}
	return num;
}

int main() {
	ll t, ca = 1;
	cin >> t;
	cin.ignore(numeric_limits<streamsize>::max(), '\n');
	string line;
	while (t--) {
		getline(cin, line);
		cout << "Case #" << ca++ << ": " << N(line) << endl;
	}
}
