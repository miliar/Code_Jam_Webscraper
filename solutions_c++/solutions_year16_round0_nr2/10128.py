#include <stdio.h>
#include <iostream>
#include <string>
#include <algorithm>
#include <sstream>
#include <queue>
#include <set>

using namespace std;

string flip(string p, int pos) {
	string s = p.substr(0, pos);
	//cout << "substring: " << s << endl;
	for (int i=0; i<pos; i++) {
		char b = s[pos - 1 - i];
		p[i] = b == '+' ? '-' : '+';
	}

	return p;
	
}

bool isHappy(string &p) {
	for (int i=0; i< p.size(); i++) {
		if (p[i] == '-') {
			return false;
		}
	}

	return true;
}

void createNode(string s, queue<string> &nodes, set<string> &sets) {
	
	for (int j=1; j <= s.size(); j++) {
		string a = flip(s, j);
		//cout << "flip: " << a << endl;
		
		if (sets.count(a) == 0)
			nodes.push(a);	
		sets.insert(a);
		//cout << "node size" << nodes.size() << endl;
		//cout << "set size" << sets.size() << endl;
		
	}

}


int main() {	
	string c;
	int t;
	set<string> sets;
	getline(cin, c);
	stringstream(c) >> t;

	for (int i = 1; i<=t; i++) {
		string s;
		sets.clear();
		
		int depth = 0;
		bool isContinue = true;
		queue<string> nodes;
		getline(cin, s);
		nodes.push(s);
		sets.insert(s);
		do {
			queue<string> cur_nodes = nodes;
			nodes = queue<string>();
			
			while (!cur_nodes.empty()) {
				string node = cur_nodes.front();
				if (isHappy(node)) {
					isContinue = false;
					break;
				} 
				createNode(node, nodes, sets);
				cur_nodes.pop();
				//getchar();
			}

			if (isContinue)
				depth++;


		} while (isContinue);

		printf("Case #%d: %d\n", i, depth);
		

	}

	return 0;
}