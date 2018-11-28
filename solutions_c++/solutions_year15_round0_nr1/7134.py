#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>
#define MAX 1000
using namespace std;

int main()
{
	ofstream fout("A.out");
	ifstream fin("A.in");

	int T; fin >> T;
	for (int t=1; t <= T; t++){
		int ans = 0, smax; string s;
		fin >> smax >> s;
		for (int i=1, npeople=s[0]-'0'; i < s.length(); i++){
			if (npeople < i) {ans += i-npeople; npeople += i-npeople;}
			npeople += s[i]-'0';
		}
		fout << "Case #" << t << ": " << ans << "\n";
	}
}