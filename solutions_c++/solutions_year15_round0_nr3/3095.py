#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <unordered_map>
using namespace std;

bool isDijkstra(const string &s, long long X){
	unordered_map<string, int> unit {{"1", 0}, {"-1", 1}, {"i", 2}, {"-i", 3}, {"j", 4}, {"-j", 5}, {"k", 6}, {"-k", 7}};
	vector<vector<string>> dict {{"1", "-1", "i", "-i", "j", "-j", "k", "-k"}, {"-1", "1", "-i", "i", "-j", "j", "-k", "k"},
									{"i", "-i", "-1", "1", "k", "-k", "-j", "j"}, {"-i", "i", "1", "-1", "-k", "k", "j", "-j"},
									{"j", "-j", "-k", "k", "-1", "1", "i", "-i"}, {"-j", "j", "k", "-k", "1", "-1", "-i", "i"},
									{"k", "-k", "j", "-j", "-i", "i", "-1", "1"}, {"-k", "k", "-j", "j", "i", "-i", "1", "-1"}};
	string product = "1";
	bool isI = false;
	bool isJ = false;
	for(long long k = 0; k < X; ++k){
		for(int i = 0; i < s.size(); ++i){
			product = dict[unit[product]][unit[s.substr(i, 1)]];
			if(product == "i" && !isI)
				isI = true;
			else if(product == "k" && isI)
				isJ = true;
		}
	}
	return isI && isJ && (product == "-1");
}

int main() {
	
	ifstream infile{"C-small-attempt0.in"};
	ofstream outfile{"C-small-attempt0.out"};

	int t;
	infile >> t;

	for(int i = 1; i <= t; ++i){
		string s;
		long long L, X;
		infile >> L >> X;
		infile >> s;
		outfile << "Case #" << i << ": " << (isDijkstra(s, X) ? "YES" : "NO") << endl;
	}
}