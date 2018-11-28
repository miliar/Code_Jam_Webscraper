#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <stdio.h>
#include <iomanip>
#include <string>
#include <queue>
using namespace std;


int reverse(int a) {
	int b = 0;
	while (a) {
		b = b * 10 + (a % 10);
		a /= 10;
	}
	return b;
}


vector<int> graph[1000001];

void create_graph() {
	for (int i = 0; i < 1000001; i++) {
		int b = reverse(i);
		graph[i].push_back(i+1);
		if (b != i) graph[i].push_back(b);
	}
	return;
}

int ans[1000001];

void bfs() {
	bool visited[1000001] = {false};
	vector<int> boundary;
	boundary.push_back(1);
	visited[1] = true;
	int size = 1;
	while (true) {
		//cout << boundary.size() << endl;
		if (boundary.empty()) return;
		vector<int> new_boundary;
		for (int i = 0; i < boundary.size(); i++) {
			if (boundary[i] > 1000000) continue;
			//cout << "i " <<boundary[i] << endl;
			ans[boundary[i]] = size;
			for (int j = 0; j < graph[boundary[i]].size(); j++)	{
				if (!visited[graph[boundary[i]][j]]) {
					new_boundary.push_back(graph[boundary[i]][j]);
					visited[graph[boundary[i]][j]] = true;
				}
			}
		}
		boundary = new_boundary;
		size++;
	}
	return;
}

int main()
{
	create_graph();
	bfs();
    int t;
	cin >> t;
	for (int _t = 1; _t <= t; _t++) {
		int n;
		cin >> n;
		cout << "Case #" << _t << ": " << ans[n] << endl;
	}
    return 0;
}
