#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <set>

using namespace std;

void help(map<char,int>& m, char x, int val, string word, map<int,int>& s) {
	while (m.count(x)>=1) {
		//for (auto it=m.begin(); it!=m.end(); ++it)
		//	for (int i=0; i < it->second; ++i) cout << it->first;
		//cout << endl;
		//cout << "Found " << x << endl;
		if (s.count(val) > 0) {
			s.at(val)++;
		} else {
			s.insert(make_pair(val,1));
		}
		for (auto it=word.begin(); it!=word.end(); ++it) {
			//cout << "Removing " << *it << endl;
			if (m.at(*it)==1) {
				m.erase(*it);
			} else if (m.at(*it) > 1) {
				m.at(*it)--;
			}
		}
	}
}


string num(string str) {
	map<char,int> m;
	for(auto it=str.begin(); it!=str.end(); ++it) {
		if(m.count(*it)>0) {
			m.at(*it)++;
		} else {
			m.insert(make_pair(*it,1));
		}
	}

	map<int, int> s;
	
	help(m, 'Z', '0', "ZERO", s);
	help(m, 'W', '2', "TWO", s);
	help(m, 'X', '6', "SIX", s);
	help(m, 'G', '8', "EIGHT", s);
	help(m, 'H', '3', "THREE", s);
	help(m, 'R', '4', "FOUR", s);
	help(m, 'O', '1', "ONE", s);
	help(m, 'F', '5', "FIVE", s);
	help(m, 'V', '7', "SEVEN", s);
	help(m, 'N', '9', "NINE", s);
	
	string out = "";

	for (auto it=s.begin(); it!=s.end(); ++it) {
		while(it->second>0) {
			out += it->first;
			it->second--;
		}
	}
	return out;
}

int main(int argc, char * argv[]) {
    int t;
    cin >> t;

    for (int c=1; c <= t; ++c) {
	string str;
	cin >> str;
	cout << "Case #" << c << ": " << num(str) << endl;
    }
}
