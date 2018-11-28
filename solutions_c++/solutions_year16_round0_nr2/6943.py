#include <iostream>
#include <fstream>
#include <string>
#include <queue>
#include <set>
#include <map>
using namespace std;

int cntPlus(const string& s)
{
	int num_plus = 0;
	for (int i = 0; i < s.length(); ++i) {
		if (s[i] == '+') {
			num_plus++;
		}
	}
	return num_plus;
}

int cntBottomPlus(const string& s) {
	int result = 0;
	for (int i = s.length() - 1; i >= 0; --i) {
		if (s[i] == '+') {
			result++;
		} else {
			return result;
		}
	}
	return result;

}

int main()
{
	fstream f_in("B-small-attempt2.in", fstream::in);
	fstream f_out("B-small-attempt2.out", fstream::out);
	int n_case;
	f_in >> n_case;
	for (int i_case = 0; i_case < n_case; ++i_case) {
		printf("i_case %d\n", i_case);
		string s_origin;
		f_in >> s_origin;
		int step = 0;
		queue<string> que;
		que.push(s_origin);
		map<string, int> visited;
		visited[s_origin] = 0;
		int result = 0;
		while (!que.empty()) {
			string u = que.front();
			que.pop();
			//printf("%d %d\n", cntPlus(u));
			if (cntPlus(u) == u.length()) { 
				result = visited[u];
				break;
			}
			for (int i = 0; i < u.length(); ++i) {
				string v = u;
				for (int j = 0; j <= i; ++j) {
					if (u[j] == '-') {
						v[i - j] = '+';
					} else {
						v[i - j] = '-';
					}
				}
				if (visited.find(v) == visited.end()) {
					visited[v] = visited[u] + 1;
					que.push(v);
				}
			}
		}
		f_out << "Case #" << i_case + 1 << ": " << result << "\n";
	}
	system("pause");
	return 0;
}