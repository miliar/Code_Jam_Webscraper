#include <fstream>
#include <string>

using namespace std;

int invite(int s_max, string map) {
	int curr = map[0] - '0';
	int f = 0;
	for (int i=1; i<=s_max; i++) {
		if (curr<i) {
			f += i-curr;
			curr = i;
		}
		curr += map[i]-'0';
	}
	return f;
}

int main() {
	int t;
	ifstream fin("in.in");
	ofstream fout("out.out");
	fin>>t;
	for (int i=0; i<t; i++) {
		int s_max;
		string map;
		fin>>s_max>>map;
		fout<<"Case #"<<i+1<<": "<<invite(s_max, map)<<endl;
	}
	return 0;
}
