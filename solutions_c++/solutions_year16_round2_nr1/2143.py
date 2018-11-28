#include <cstdio>
#include <string>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

int n;

int inBuffer[26];
int outBuffer[10];

string s;

int t;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> t;
	int i;
	int j;
	for(i = 1; i <= t; i ++) {	
		cin >> s;
		memset(inBuffer, 0, sizeof(inBuffer));
		memset(outBuffer, 0, sizeof(outBuffer));
		cout << "Case #" << i << ": ";
		for(j = 0; j < s.length(); j++) {
			inBuffer[s[j] - 'A'] ++;
		}
		// 0 
		while(inBuffer['Z'-'A']--) {
			inBuffer['E' - 'A']--;
			inBuffer['R' - 'A']--;
			inBuffer['O' - 'A']--;
			outBuffer[0]++;
		}
		// 2 
		while(inBuffer['W'-'A']--) {
			inBuffer['T' - 'A']--;
			inBuffer['O' - 'A']--;
			outBuffer[2]++;
		}
		// 6
		while(inBuffer['X'-'A']--) {
			inBuffer['S' - 'A']--;
			inBuffer['I' - 'A']--;
			outBuffer[6]++;
		}
		// 8
		while(inBuffer['G'-'A']--) {
			inBuffer['E' - 'A']--;
			inBuffer['I' - 'A']--;
			inBuffer['H' - 'A']--;
			inBuffer['T' - 'A']--;
			outBuffer[8]++;
		}

		// 7
		while(inBuffer['S'-'A']--) {
			inBuffer['E' - 'A']--;
			inBuffer['V' - 'A']--;
			inBuffer['N' - 'A']--;
			inBuffer['E' - 'A']--;
			outBuffer[7]++;
		}
		// 3
		while(inBuffer['H'-'A']--) {
			inBuffer['T' - 'A']--;
			inBuffer['E' - 'A']--;
			inBuffer['R' - 'A']--;
			inBuffer['E' - 'A']--;
			outBuffer[3]++;
		}
		// 5
		while(inBuffer['V'-'A']--) {
			inBuffer['F' - 'A']--;
			inBuffer['I' - 'A']--;
			inBuffer['E' - 'A']--;
			outBuffer[5]++;
		}
		// 4
		while(inBuffer['F'-'A']--) {
			inBuffer['O' - 'A']--;
			inBuffer['U' - 'A']--;
			inBuffer['R' - 'A']--;
			outBuffer[4]++;
		}
		// 9
		while(inBuffer['I'-'A']--) {
			inBuffer['N' - 'A']--;
			inBuffer['N' - 'A']--;
			inBuffer['E' - 'A']--;
			outBuffer[9]++;
		}
		// 1
		while(inBuffer['N'-'A']--) {
			inBuffer['O' - 'A']--;
			inBuffer['E' - 'A']--;
			outBuffer[1]++;
		}
		for(j = 0; j < 10; j ++) {
			while(outBuffer[j]--) {
				cout << j;
			}
		}
		cout << endl;
	}

	
	fclose(stdin);
	fclose(stdout);
	return 0;
}
