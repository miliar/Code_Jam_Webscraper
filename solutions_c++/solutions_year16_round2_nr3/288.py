#include "stdafx.h"

#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <map>

using namespace std;

struct Bipartite {
	vector<vector<int> > adjLeft;
	vector<int> matchLeft, matchRight;
	vector<bool> visited;
	int matchingSize;

	Bipartite(int p = 0, int q = 0) :
		adjLeft(p), matchLeft(p, -1), matchRight(q, -1), matchingSize(0) {}

	bool depthFirstSearch(int x) {
		if (visited[x]) return false;
		visited[x] = true;
		for (int i = 0; i < (int)adjLeft[x].size(); ++i) {
			int y = adjLeft[x][i];
			int z = matchRight[y];
			if (z < 0 || depthFirstSearch(z)) {
				matchRight[y] = x;
				matchLeft[x] = y;
				return true;
			}
		}
		return false;
	}

	bool findAgumentingPath(void) {
		visited.assign(adjLeft.size(), false);
		for (int i = 0; i < (int)adjLeft.size(); ++i)
			if (matchLeft[i] == -1 && depthFirstSearch(i))
				return true;
		return false;
	}

	int maximumMatching(void) {
		while (findAgumentingPath()) ++matchingSize;
		return matchingSize;
	}
};


int main() {
	ifstream in;
	in.open("../Cin.txt");
	ofstream out;
	out.open("../Cout.txt");

	int T;
	in >> T;
	for (int icase = 1; icase <= T; ++icase) {
		out << "Case #" << icase << ": ";
		int n;
		in >> n;

		vector<pair<string, string>> stringEdge(n);
		for (int i = 0; i < n; ++i)
			in >> stringEdge[i].first >> stringEdge[i].second;

		map<string, int> mappingLeft;
		int p = 0;
		for (auto& e : stringEdge)
			if (mappingLeft.find(e.first) == end(mappingLeft)) {
				mappingLeft[e.first] = p;
				++p;
			}

		map<string, int> mappingRight;
		int q = 0;
		for (auto& e : stringEdge)
			if (mappingRight.find(e.second) == end(mappingRight)) {
				mappingRight[e.second] = q;
				++q;
			}
		Bipartite g(p + 1, q + 1);
		for (auto& e : stringEdge)
			g.adjLeft[mappingLeft[e.first]].push_back(mappingRight[e.second]);

		int matching = g.maximumMatching();
		int edgeCover = p + q - matching;
		out << n - edgeCover;

		out << "\n";
	}
}