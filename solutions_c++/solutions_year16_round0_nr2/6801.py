#include<iostream>
#include<fstream>
#include<string>
#include <cstdio>
#define Aone 1023
using namespace std;

int main(int argc, char** argv) {
	int T;
	int test_case;
	int len;
	int count = 0;
	freopen("B-large.in", "r", stdin);

	scanf("%d", &T);
	for (test_case = 1; test_case <= T; ++test_case) {
		string s;
		cin >> s;
		len = strlen(s.c_str());
		count = 0;
		for (int i = 0; i < len; i++) {
			if (i == len - 1) {
				if (s[len - 1] == '-') {
					count++; break;
				}
				else break;
			}
			if (s[i] == s[i + 1]) {
				continue;
			}
			else {
				count++;
				continue;
			}
		}

		cout << "Case #" << test_case << ": " << count << endl;;
		
	}
}