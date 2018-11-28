#include <iostream>
#include <vector>
#include <algorithm>
#include <bitset>
#include <fstream>

using namespace std;

typedef long long ll;

int main() { 
	ofstream fout;
	fout.open ("ayylmao.txt");
	ifstream fin;
	fin.open ("B-large.in");

	int t; fin>>t;
	for (int i = 1; i <= t; i++) {
		string s; fin>>s;
		char fc = s[0];
		fout<<"Case #"<<i<<": ";
		int count = 1;
		for (int j = 1; j < s.length(); j++) {
			if (s[j] != s[j - 1]) {
				count++;
			}
		}
		//cout<<count<<' '<<fc<<endl;
		if (fc == '-' && count%2 == 1) {
			fout<<count<<endl;
		}
		else if (fc == '-' && count%2 == 0) {
			fout<<count - 1<<endl;
		}
		else if (fc == '+' && count%2 == 1) {
			fout<<count - 1<<endl;
		}
		else {
			fout<<count<<endl;
		}
	}
	return 0;
}