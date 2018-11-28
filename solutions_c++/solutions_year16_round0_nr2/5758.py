#include <iostream>
#include <vector>
#include <unordered_set>
#include <queue>

using namespace std;

bool isFinal(string s) {
	if (s.find("-") == string::npos) return true;
	return false;
}

string generate(string s, int index) {
	string ret = s;
	for (int i = 0; i<=index; i++) {
		ret[i] = (s[index - i] == '+') ? '-' : '+';
	}
	return ret;
}
long getResults(string start) {
	if (isFinal(start)) return 0;
	queue<string> Q;
	unordered_set<string> states;
	states.insert(start);
	Q.push(start); 
	int steps = 0;
	while (!Q.empty()) {
		int size = Q.size();
		for (int i = 0; i<size; i++) {
			string head = Q.front();
			for (int j = 0; j<head.size(); j++) {
				string s = generate(head, j);
				if (isFinal(s)) return steps + 1;
				if (states.find(s) == states.end()) {
					Q.push(s);
					states.insert(s);
				}
			}
			Q.pop();
		}
		steps += 1;
	} 
	cout << "cannot be here" << endl;
	return steps;

}
int findFirstPlus(string &start, int index) {
	for (int i = index; i>=0; i--) {
		if (start[i] == '+') return i;
	}
	//
	cout << "cannot be here" << endl;
	return -1;
}
void changeState(string &str, int index) {
	string ret = str;
	for (int i = 0; i<=index; i++) {
		ret[i] = (str[index - i] == '+') ? '-' : '+';
	}
	str = ret;
}
long getResultsLarge(string start) {
	if (isFinal(start)) return 0;
	long ret = 0;
	for (int j = start.size()-1; j>=0; j--) {
		if (start[j] == '+') continue;
		if (start[0] == '-') {
			ret += 1;
			changeState(start, j);
			continue;
		}
		auto plusIndex = findFirstPlus(start, j);
		changeState(start, plusIndex);
		changeState(start, j);
		ret += 2;
	}
	return ret;
}

int main() {
	int cases;
	cin >> cases;
	for (int i = 0; i<cases; i++) {
		string start;
		cin >> start;
		cout << "Case #" << i + 1 << ": " << getResultsLarge(start) << endl;
	}
}