#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <algorithm>
#include <cmath>
#include <sstream>
#include <climits>
#include <cstdlib>
#include <cctype>
#include <fstream>

using namespace std;

void solveA() {
	ifstream myfile("A-large.in");
	ofstream outfile("A-large.out");
	if (!myfile.is_open()) {
		return;
	}
	string line;
	getline(myfile, line);
	stringstream ssline(line);
	int num_case;
	ssline >> num_case;
	for (int i = 0; i < num_case; i++) {
		outfile << "Case #" << i + 1 << ": ";
		getline(myfile, line);
		stringstream ssline(line);
		string res;
		if(line.size() == 1) {
			res = line;
		}else{
			res.push_back(line[0]);
			for(int j = 1; j < line.size(); j++) {
				if(line[j] >= res[0]) {
					res.insert(res.begin(), line[j]);
				}else{
					res.push_back(line[j]);
				}
			}
		}
		outfile << res << endl;
	}
	outfile.close();
	myfile.close();
}

int main() {
	solveA();
}

