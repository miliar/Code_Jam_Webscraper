#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
	ifstream fin("A-large.in");
	ofstream fout("output.txt");
	int n;
	int len, count, ans;
	string str;
	fin >> n;
	int a[2000];
	for (int i=0; i<n; i++) {
		fin >> len >> str;
		for (int j=0; j<str.length(); j++)
			a[j] = str[j]-48;
		count = 0;
		ans = 0;
		for (int j=0; j<str.length(); j++) {
			if (j <= count) {
				count += a[j]; 
			}
			else {
				ans += j-count;
				count = a[j] + j;
			}
		}
		fout << "Case #" << i+1 << ": " << ans << endl;
	}
	fin.close();
	fout.close();
}
