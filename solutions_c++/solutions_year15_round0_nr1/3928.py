#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int T, S;
string str;

int main(){
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	fin >> T;
	int t = T;
	while (T--) {
		fin >> S;
		fin >> str;
		int ans = 0;
		int sum = 0;
		for (int i=0; i<=S; i++) {
			if (sum<i) {
				ans += i-sum;
				sum = i;
			}
			sum += str[i]-'0';
		}
		fout << "Case #" << t-T << ": " << ans << endl;
	}
}
