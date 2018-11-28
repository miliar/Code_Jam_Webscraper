#include <iostream>
#include <map>
#include <string>
#include <queue>

using namespace std;

int SolveSlow(string s) {
	map <string, int> flag;
	
	queue <string> q;
	q.push(s);
	flag[s] = 1;

	while (!q.empty()) {
		string front = q.front();
		int val = flag[front];
		q.pop();

		for (int i = 0; i < s.size(); i++) {
			string temp = front;
			reverse(temp.begin(), temp.begin() + i + 1);
			for (int k = 0; k <= i; k++)
				temp[k] = temp[k] == '+' ? '-' : '+';
			if (!flag[temp]) {
				flag[temp] = val + 1;
				q.push(temp);
			}
		}		
	}
	string search = "";
	for (int i = 0; i < s.size(); i++)
		search += "+";
	return flag[search] - 1;
}

int SolveFast(string s) {
	int cnt = 0;
	for (int i = 1; i < s.size(); i++)
		cnt += s[i] != s[i - 1];
	cnt += s[s.size() - 1] == '-';
	return cnt;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	cin >> t;
	string s;
	for (int test = 1; test <= t; test++) {
		cout << "Case #" << test << ": ";
		cin >> s;
		//cout << SolveSlow(s) << " " 
		cout << SolveFast(s) << endl;
	}

	return 0;
}