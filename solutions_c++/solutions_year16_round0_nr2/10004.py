#include <algorithm>
#include <functional>
#include <vector>
#include <map>    
#include <cstdio>
#include <queue>
#include <climits>
#include <stack>
#include <set>
#include <cmath>
#include <cstring>
#include <list>
#include <iostream>
#include <string>
using namespace std;

typedef long long ll;

const int INF = 987654321;
const ll INFF = 987654321213;
const ll MOD = 987654321;
const ll PLUS = 1000000;

int t;
string str;
map <string, int > m;

int bfs(string s) {

	queue<string> q;
	q.push(s);
	m[s]++;

	int cnt = 0;
	while (!q.empty()) {

		int Size = q.size();

		for (int i = 0; i < Size; i++) {
			string here = q.front();
			q.pop();


			bool flag = true;
			for (int j = 0; j < here.size(); j++) {
				if (here[j] == '-') {
					flag = false; break;
				}
			}
			if (flag == true) return cnt;

			for (int j = 0; j < here.size(); j++) {

				reverse(here.begin(), here.begin() + j + 1);
				for (int k = 0; k <= j; k++) {
					if (here[k] == '+') here[k] = '-';
					else here[k] = '+';
				}
				
				if (m.count(here) == 0) {
					m[here]++;
					q.push(here);
				}

				reverse(here.begin(), here.begin() + j + 1);
				for (int k = 0; k <= j; k++) {
					if (here[k] == '+') here[k] = '-';
					else here[k] = '+';
				}

			}


		}
		cnt++;
	}
}
int main() {
#ifdef _CONSOLE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w+", stdout);
#endif

	scanf("%d", &t);

	for (int testCase = 1; testCase <= t; testCase++) {

		cin >> str;

		printf("Case #%d: %d\n", testCase, bfs(str));
		m.clear();

	}

}
