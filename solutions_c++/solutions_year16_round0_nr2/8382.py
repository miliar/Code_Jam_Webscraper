#include <iostream>
#include <string>
using namespace std;

bool binaryPancakes[100000];

void toBinary(char *panks, bool bin[]) {
	int n = strlen(panks);
	for(int i = 0; i < n; i++) {
		if(panks[i] == '-') bin[i] = 0;
		else bin[i] = 1;
	}
}

int flipCount(bool panks[], int n) {
	int count = 0;
	bool last = panks[0];

	for(int i = 0; i < n; i++) {
		bool pan = panks[i];
		if(pan == last) continue;
		count++;
		last = pan;
	}
	if(!last) count++;
	return count;
}

int main() {
	int n;
	string pancakes;
	cin >> n;
	for(int i=0; i<n; i++) {
		cin >> pancakes;
		char* pancakesChr = strdup(pancakes.c_str());
		int n = strlen(pancakesChr);
		toBinary(pancakesChr, binaryPancakes);
		int count = flipCount(binaryPancakes, n);
		cout << "Case #" << i+1 << ": "<< count << endl;
	}
}