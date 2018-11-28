#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
using namespace std;

ifstream f;

const char *numbers[10] = {
	"ZERO",
	"ONE",
	"TWO",
	"THREE",
	"FOUR",
	"FIVE",
	"SIX",
	"SEVEN",
	"EIGHT",
	"NINE"};
int cnt[100];
// attempt order is important
int order[10] = {0,6,7,5,4,2,8,3,1,9};

bool check(int i) {
	const char *p = numbers[i];
	for (; *p; p++) {
		if (cnt[*p-'A'] == 0) return false;
	}
	p = numbers[i];
	for (; *p; p++) cnt[*p-'A']--;
	return true;
}

void process(string &s) {
	// cache first
	int r[10];
	for (int i=0; i<10; i++) r[i]=0;
	for (int i=0; i<100; i++) cnt[i]=0;
	for (int i=0; i<s.length(); i++) {
		cnt[s[i]-'A']++;
	}

	string rs;
	bool end = false;
	while (!end) {
		end = true;
		for (int i=0; i<10; i++) {
			if (check(order[i])) {
				r[order[i]]++;
				end = false;
				break;
			}
		}
	}

	// ordered result
	for (int i=0;i<10; i++) {
		for (;r[i]; r[i]--) {
			rs.push_back('0'+i);
		}
	}

	cout << rs;
}

int main(int argc, char** argv) {
	f.open("input.txt");
	int t;	f >> t;
	for (int i=0; i<t; i++) {
		string s;
		f >> s;
		cout << "Case #" << i+1 << ": ";
		process(s);
		cout << endl;
	}
	return 0;
}
