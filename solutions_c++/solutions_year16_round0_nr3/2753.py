#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
#include <stack>
#include <assert.h>
#include <algorithm>
#include <math.h>
#include <ctime>
#include <functional>
#include <string.h>
#include <stdio.h>
#include <numeric>
#include <float.h>

using namespace std;

int N = 16, J = 50; 

struct Rec {
	string s; 
	vector<int> v; 

	Rec(string& ss) : s(ss) {}
};

map<int, vector<Rec>> result; 

bool nextstr(string& s, string& nexts) {
	nexts = s;
	int over = 1; 
	for (int i = s.size() - 2; i >= 1; i--) {
		int a = s[i] - '0'; 
		a += over; 
		if (a == 0) {
			over = 0; 
			nexts[i] = '0'; 
		}
		else if (a == 1) {
			over = 0; 
			nexts[i] = '1'; 
		}
		else {
			over = 1; 
			nexts[i] = '0'; 
		}
		if (over == 0) break;
	}
	if (over == 1) return false;
	return true; 
}

bool isPrime(long long num, long long &factor) {
	for (long long l = 2; l <= (long long)sqrt(num); l++) {
		if (num % l == 0) {
			factor = l; 
			return false; 
		}
	}
	return true; 
}

bool goodString(Rec& rec) {
	for (long long l = 2; l <= 10; l++) {
		long long val = 0;
		string s = rec.s; 
		for (int i = s.size() - 1; i >= 0; i--) {
			val += pow(l, s.size() - 1 - i) * (s[i] - '0'); 
		}
		long long factor = 0; 
		if (isPrime(val, factor)) {
			return false; 
		}
		rec.v.push_back(factor); 
	}
	return true; 
}

void f() {
	for (int n = 2; n <= N; n++) {
		string s = "1"; 
		for (int i = 0; i < (n - 2); i++) s.push_back('0'); 
		s.push_back('1'); 

		while (result[n].size() < J) {
			Rec rec(s); 
			if (goodString(rec)) {
				result[n].push_back(rec); 
			}
			string ns; 
			if (!nextstr(s, ns)) {
				break;
			}
			else {
				s = ns; 
			}
		}
	}
}

int main(int argc, char* argv[]) {
	f(); 
	cout << "begin" << endl; 
	string fn; cin >> fn; 

	ifstream inf(fn);
	int TC = 0; inf >> TC;
	for (int tc = 1; tc <= TC; tc++) {
		int n, j; inf >> n >> j; 
		cout << "Case #" << tc << ": " << endl; 
		for (int i = 0; i < j; i++) {
			cout << result[n][i].s; 
			for (int j = 0; j < result[n][i].v.size(); j++) {
				cout << " " << result[n][i].v[j]; 
			}
			cout << endl; 
		}
	}

	return 0; 
}

/*
int main(int argc, char* argv[]) {
	ifstream inf(argv[1]);
	int TC = 0; inf >> TC;

	for (int tc = 1; tc <= TC; tc++) {
		string s; inf >> s; 

		char c = s[0]; 
		int ans = 0; 
		for (int i = 1; i < s.size(); i++) {
			if (c != s[i]) {
				c = s[i]; 
				ans++; 
			}
		}
		if (c == '-') ans++;
		cout << "Case #" << tc << ": " << ans << endl; 
	}

	return 0;
}
*/

/*
string add(string& s1, string& s2) {
	string result; 

	int over = 0; 
	for (int i = 0; i < max(s1.size(), s2.size()); i++) {
		int a = 0, b = 0; 
		if (i < s1.size()) {
			a = s1[s1.size() - i - 1] - '0'; 
		}
		if (i < s2.size()) {
			b = s2[s2.size() - i - 1] - '0'; 
		}

		int tr = a + b + over; 
		result.insert(result.begin(), '0' + (tr % 10)); 
		over = tr / 10; 
	}
	if (over > 0) result.insert(result.begin(), '0' + over); 
	return result; 
}

int main(int argc, char* argv[]) {
	ifstream inf(argv[1]);
	int TC = 0; inf >> TC; 

	for (int tc = 1; tc <= TC; tc++) {
		string s; inf >> s; 
		if (s == "0") {
			cout << "Case #" << tc << ": INSOMNIA" << endl; 
		}
		else {
			vector<bool> digits(10, false); 
			string now = s; 
			while (true) {
				for (int i = 0; i < now.size(); i++) {
					digits[now[i] - '0'] = true; 
				}

				bool allVisited = true;
				for (int i = 0; i < digits.size(); i++) {
					if (!digits[i]) {
						allVisited = false;
						break;
					}
				}
				if (allVisited) {
					cout << "Case #" << tc << ": " << now << endl;
					break;
				}

				now = add(now, s); 
			}
		}
	}

	return 0;
}
*/

/*
int main(int argc, char* argv[]) {
	ifstream inf(argv[1]); 

	int T = 0; inf >> T;
	for (int t = 1; t <= T; t++) {
		int row, col; inf >> row >> col; 
		vector<string> grid; 
		for (int i = 0; i < row; i++) {
			string str; inf >> str; 
			grid.push_back(str);
		}

		bool impossible = false; 
		int ans = 0; 
		for (int r = 0; r < row && !impossible; r++) {
			for (int c = 0; c < col && !impossible; c++) {
				if (grid[r][c] == '.') continue;
				bool b1 = false, b2 = false, b3 = false, b4 = false; 
				for (int i = 0; i < c; i++) {
					if (grid[r][i] != '.') {
						b1 = true;
						break;
					}
				}
				for (int i = c + 1; i < col; i++) {
					if (grid[r][i] != '.') {
						b2 = true;
						break;
					}
				}
				for (int i = 0; i < r; i++) {
					if (grid[i][c] != '.') {
						b3 = true;
						break;
					}
				}
				for (int i = r + 1; i < row; i++) {
					if (grid[i][c] != '.') {
						b4 = true;
						break;
					}
				}

				if (!b1 && !b2 && !b3 && !b4) {
					impossible = true;
				}
				else if (!b1 && grid[r][c] == '<') {
					ans++; 
				}
				else if (!b2 && grid[r][c] == '>') {
					ans++;
				}
				else if (!b3 && grid[r][c] == '^') {
					ans++;
				}
				else if (!b4 && grid[r][c] == 'v') {
					ans++;
				}
			}
		}


		cout << "Case #" << t << ": ";
		if (impossible) cout << "IMPOSSIBLE" << endl;
		else cout << ans << endl; 
	}

	return 0;
}
*/


/*
int main(int argc, char* argv[]) {
	long long *l = new long long();


	return 0;
}
*/

/*
4.6.3
*/
/*
int totalUsedTime = 0; 
vector<string> process; 

struct Rec {
	int id = 0, times = 0; 
	Rec(int aid, int atimes) : id(aid), times(atimes) {}
};
bool operator<(Rec &rec1, Rec &rec2) {
	return rec1.times < rec2.times;
}1

void solution(vector<Rec> times) {
	sort(times.begin(), times.end());
	int n = times.size(); 
	vector<bool> overRiver(n, false); 
	while (n > 0) {
		if (n == 1 || n == 2) {
			int usedTime = 0; 
			string pro; 
			for (int i = 0; i < times.size(); i++) {
				if (!overRiver[i]) {
					usedTime = max(usedTime, times[i].times);
					if (!pro.empty()) pro.push_back(' ');
					char buf[10] = { 0 };
					sprintf(buf, "%d", times[i].times);
					pro += buf;
					overRiver[i] = true;
				}
			}
			n = 0; 
			totalUsedTime += usedTime;
			process.push_back(pro);
		}
		else {
			if (overRiver[0] == false && overRiver[1] == false) {
				// go
				totalUsedTime += times[1].times;
				char buf[100] = { 0 };
				sprintf(buf, "%d %d", times[0].times, times[1].times);
				process.push_back(buf);
				overRiver[0] = true;
				overRiver[1] = true;
				// back
				totalUsedTime += times[0].times;
				memset(buf, 0, sizeof(buf));
				sprintf(buf, "%d", times[0].times);
				process.push_back(buf);
				overRiver[0] = false;
			}
			else {
				bool gotSlowest = false;
				int p1 = 0, p2 = 0;
				for (int i = times.size() - 1; i >= 0; i--) {
					if (!overRiver[i]) {
						if (gotSlowest) {
							p2 = i; 
							break;
						}
						else {
							gotSlowest = true;
							p1 = i; 
						}
					}
				}
				if (2 * times[1].times > times[p2].times + times[0].times) {
					// go 
					char buf[100] = { 0 };
					sprintf(buf, "%d %d", times[0].times, times[p1].times);
					process.push_back(buf);
					overRiver[p1] = true;
					overRiver[0] = true;
					totalUsedTime += times[p1].times;
					// back
					memset(buf, 0, sizeof(buf));
					sprintf(buf, "%d", times[0].times);
					process.push_back(buf);
					overRiver[0] = false;
					totalUsedTime += times[0].times;
				}
				else {
					// go 
					char buf[100] = { 0 };
					sprintf(buf, "%d %d", times[p2].times, times[p1].times);
					process.push_back(buf);
					overRiver[p1] = true;
					overRiver[p2] = true;
					totalUsedTime += times[p1].times;
					// back
					memset(buf, 0, sizeof(buf));
					sprintf(buf, "%d", times[1].times);
					process.push_back(buf);
					overRiver[1] = false;
					totalUsedTime += times[1].times;
				}
			}
			n -= 1;
		}
	}
}

int main() {
	int TC = 0; cin >> TC;
	bool blank = false; 
	for (int tc = 1; tc <= TC; tc++) {
		int num = 0; cin >> num; 
		vector<Rec> times; 
		for (int i = 0; i < num; i++) {
			int d = 0; cin >> d; 
			times.push_back(Rec(i+1, d)); 
		}

		if (blank) cout << endl; 
		blank = true;

		solution(times);
		cout << totalUsedTime << endl; totalUsedTime = 0; 
		for (int i = 0; i < process.size(); i++) cout << process[i] << endl; 
		process.clear();
	}
	return 0; 
}
*/