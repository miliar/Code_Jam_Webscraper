#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> d[105], invert[55];
vector<vector<int> > test, original;
vector<int> output;
bool visited[105];
int N;

bool cmp(vector<int>& a, vector<int>& b) {
	for(int i = 0; i < a.size(); i++) {
		if(a[i] != b[i]) return a[i] < b[i];
	}
	return false;
}

bool eq(vector<int>& a, vector<int>& b) {
	for(int i = 0; i < a.size(); i++) {
		if(a[i] != b[i]) return false;
	}
	return true;
}

bool dfs(int curr, int depth) {
	visited[curr] = true;
	if(depth == N) {
		for(int i = 0; i < 2 * N - 1; i++) {
			if(visited[i]) test.push_back(d[i]);
			else original.push_back(d[i]);
		}
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < N; j++) {
				invert[i].push_back(test[j][i]);
			}
		}
		int ptr;
		for(ptr = 0; ptr < N - 1; ptr++) {
			if(!eq(invert[ptr], original[ptr])) break;
		}
		output = invert[ptr];
		for(; ptr < N - 1; ptr++) {
			if(!eq(invert[ptr+1], original[ptr])) {
				for(int j = 0; j < 55; j++) invert[j].clear();
				test.clear();
				original.clear();
				visited[curr] = false;
				return false;
			}
		}
		for(int j = 0; j < 55; j++) invert[j].clear();
		test.clear();
		original.clear();
		visited[curr] = false;
		return true;
	}
	for(int i = curr + 1; i < N + depth; i++) {
		bool flag = true;
		for(int j = 0; j < N; j++) {
			if(d[i][j] <= d[curr][j]) {flag = false; break;}
		}
		if(!flag) continue;
		if(dfs(i, depth + 1)) {visited[curr] = false; return true;}
	}
	visited[curr] = false;
	return false;
}

int main()
{
	int casenum, temp;
	cin >> casenum;
	for(int id = 1; id <= casenum; id++) {
		cin >> N;
		for(int i = 0; i < 2 * N - 1; i++) {
			d[i].clear();
			for(int j = 0; j < N; j++) {
				cin >> temp;
				d[i].push_back(temp);
			}
		}
		sort(d, d + 2 * N - 1, cmp);
		memset(visited, sizeof(visited), false);
		for(int i = 0; i < N; i++) {
			if(dfs(i, 1)) break;
		}
		printf("Case #%d:", id);
		for(int i = 0; i < N; i++) printf(" %d", output[i]);
		cout << endl;
	}

	return 0;
}