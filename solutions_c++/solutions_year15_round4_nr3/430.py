#include <map>
#include <iostream>
#include <cstring>
#include <cmath>
#include <sstream>
using namespace std;

map<string, int> words;
int code = 0;

int table[20][20];
int given[2][1005];

		bool english[8000];
		bool fran[8000];
int main() {
	int tt;
			std::string line;
			std::getline(cin, line);
		    std::istringstream iss(line);
		iss>>tt;
	for (int t=1;t<=tt;++t) {
			std::string line;
			std::getline(cin, line);
		    std::istringstream iss(line);
		int n;
		iss>>n;
		
		words.clear();
		code=0;
		
		memset(table, 0, sizeof(table));
		memset(given, 0, sizeof(given));
		
		for (int i = 0; i < n; ++i) {
			std::string line;
			std::getline(cin, line);
		    std::istringstream iss(line);
			string word;
			int c = 0;
			while (iss >> word) {
				int& v = words[word];
				if (!v) v = ++code;
				if (i < 2)
					given[i][c] = v;
				else
					table[i-2][c] = v;
				++c;
			}
		}
		
		unsigned comb = 0;
		unsigned max = pow(2, n-2);
		unsigned ress = -1;
		while (comb < max || comb == 0) {
			memset(english, 0, sizeof(english));
			memset(fran, 0, sizeof(fran));
			for (int i = 0; given[0][i]; ++i) english[given[0][i]] = 1;
			for (int i = 0; given[1][i]; ++i) fran[given[1][i]] = 1;
			
			for (int j = 0;j < n-2;++j)
				if (comb&(1<<j))
					for (int i = 0; table[j][i]; ++i) english[table[j][i]] = 1;
				else
					for (int i = 0; table[j][i]; ++i) fran[table[j][i]] = 1;
				
			unsigned res = 0;
			for (int j = 0; j < code+1; ++j) if (english[j] && fran[j]) ++res;
			if (res < ress) ress = res;
			++comb;
		}
		cout << "Case #" << t << ": " << ress << endl;
	}
}