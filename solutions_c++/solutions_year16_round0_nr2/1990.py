#include<iostream>
#include<string.h>
#include<vector>
#include<set>
#include<map>
#include<fstream>
#include<string>
using namespace std;
int main() {
	ifstream in("B-large.in");
	ofstream out("output.txt");
	int t;
	in >> t;
	for (int z = 1; z <= t; ++z) {
		string s;
		int cnt = 0;
		in >> s;
		for (int i = s.size() - 1; i >= 0; --i) {
			cnt += ((s[i] == '-' && cnt%2 == 0) || (s[i] == '+' && cnt%2 != 0));
		}
		out << "Case #" << z << ": "<< cnt << endl;
	}
	return 0;
}