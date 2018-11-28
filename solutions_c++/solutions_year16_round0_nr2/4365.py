#include <iostream>
#include <string.h>
#include <stdlib.h>
using namespace std;

char line[256];

// scan from reversed side
int process() {
	char c=0;
	int r=0;
	for (int i=strlen(line); --i>=0;) {
		if (c) {
			if (line[i] != c) r++;
		}
		c = line[i];
	}
	if (line[strlen(line)-1] =='-') r++;
	return r;
}

int main() {
	cin.getline(line, 256);
	int n = atoi(line);
	for (int i=0; i<n; i++) {
		cin.getline(line, 256);
		int r = process();
		cout << "Case #" << i+1 << ": " << r << endl;
	}
	return 0;
}
