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

const int N = 55; 

int arr[N][N]; 
int n;

vector< vector<int> > numbers; 

bool complete() {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (arr[i][j] <= 0) return false;
		}
	}
	return true; 
}

bool validArr() {
	for (int i = 0; i < n; i++) {
		int num = -2; 
		bool valid = true; 
		for (int j = 0; j < n; j++) {
			if (arr[i][j] < 0) continue;
			if (arr[i][j] <= num) {
				return false; 
			}
			num = arr[i][j]; 
		}
	}
	for (int i = 0; i < n; i++) {
		int num = -2;
		bool valid = true;
		for (int j = 0; j < n; j++) {
			if (arr[j][i] < 0) continue;
			if (arr[j][i] <= num) {
				return false;
			}
			num = arr[j][i];
		}
	}
	return true; 
}

bool force(int lineNum) {
	if (lineNum >= numbers.size())
		if (complete())
			return true;
		else
			return false; 

	int arrBack[N][N];

	for (int i = 0; i < n; i++) {
		memcpy(arrBack, arr, sizeof(arr));
		bool isValid = true; 
		for (int j = 0; j < n; j++) {
			if (arr[i][j] == -1) {
				arr[i][j] = numbers[lineNum][j]; 
			}
			else {
				if (arr[i][j] != numbers[lineNum][j]) {
					isValid = false; 
					break;
				}
			}
		}
		if (isValid && validArr()) {
			bool tr = force(lineNum + 1); 
			if (tr) {
				return true; 
			}
		}
		memcpy(arr, arrBack, sizeof(arr));
	}

	for (int i = 0; i < n; i++) {
		memcpy(arrBack, arr, sizeof(arr));
		bool isValid = true;
		for (int j = 0; j < n; j++) {
			if (arr[j][i] == -1) {
				arr[j][i] = numbers[lineNum][j];
			}
			else {
				if (arr[j][i] != numbers[lineNum][j]) {
					isValid = false;
					break;
				}
			}
		}
		if (isValid && validArr()) {
			bool tr = force(lineNum + 1);
			if (tr) {
				return true;
			}
		}
		memcpy(arr, arrBack, sizeof(arr));
	}
	return false; 
}

int main(int argc, char* argv[]) {
	ifstream inf(argv[1]);
	int TC = 0; inf >> TC;

	for (int tc = 1; tc <= TC; tc++) {
		inf >> n;
		memset(arr, -1, sizeof(arr));

		numbers.clear(); 
		for (int i = 0; i < (2 * n-1); i++) {
			vector<int> line; 
			for (int j = 0; j < n; j++) {
				int num; inf >> num; 
				line.push_back(num); 
			}
			numbers.push_back(line); 
		}

		force(0);

		cout << "Case #" << tc << ":";
		bool findAns = false;

		for (int i = 0; i < n; i++) {
			bool find = false; 
			for (int j = 0; j < numbers.size(); j++) {
				bool same = true; 
				for (int k = 0; k < n; k++) {
					if (arr[i][k] != numbers[j][k]) {
						same = false;
						break;
					}
				}
				if (same) {
					find = true; 
					numbers.erase(numbers.begin() + j); 
					break;
				}
			}
			if (!find) {
				for (int j = 0; j < n; j++) {
					cout << " " << arr[i][j]; 
				}
				cout << endl;
				findAns = true;
				break;
			}
		}

		if (!findAns) {
			for (int i = 0; i < n; i++) {
				bool find = false;
				for (int j = 0; j < numbers.size(); j++) {
					bool same = true;
					for (int k = 0; k < n; k++) {
						if (arr[k][i] != numbers[j][k]) {
							same = false;
							break;
						}
					}
					if (same) {
						find = true;
						numbers.erase(numbers.begin() + j);
						break;
					}
				}
				if (!find) {
					for (int j = 0; j < n; j++) {
						cout << " " << arr[j][i];
					}
					cout << endl;
					findAns = true;
					break;
				}
			}
		}
	}

	return 0;
}

/*
struct Rec {
	vector<int> line; 
};
bool operator<(Rec rec1, Rec rec2) {
	for (int i = 0; i < rec1.line.size(); i++) {
		if (rec1.line[i] < rec2.line[i]) return true; 
	}
	return false; 
}

vector<Rec> numbers; 
int n; 

bool solve(int pos, int recNum) {
	bool result = false; 
	if (pos == 0) {
		if (numbers[0].line[0] == numbers[1].line[0]) {
			for (int i = 0; i < n; i++) {
				arr[0][i] = numbers[0].line[i]; 
				arr[i][0] = numbers[1].line[i]; 
			}
			result = solve(1, 2); 
		}
		else {
			for (int i = 0; i < n; i++) {
				arr[i][0] = numbers[0].line[i]; 
			}
			result = solve(1, 1); 
		}
	}
	else {
		if (arr[0][pos] == -1) {

		}
		else {

		}
	}
}

int main(int argc, char* argv[]) {
	ifstream inf(argv[1]);
	int TC = 0; inf >> TC;

	for (int tc = 1; tc <= TC; tc++) {
		inf >> n; 
		memset(arr, -1, sizeof(arr)); 

		numbers.clear(); 
		for (int i = 0; i < n - 1; i++) {
			Rec rec; 
			for (int j = 0; j < n; j++) {
				int n = 0; inf >> n; 
				rec.line.push_back(n); 
			}
			numbers.push_back(rec);
		}

		sort(numbers.begin(), numbers.end()); 




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