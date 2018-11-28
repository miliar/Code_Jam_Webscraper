#include <iostream>
#include <string.h>
#include <stdio.h>

using namespace std;

void process(string s) {
	int sum = s[0] - '0';
	int numPeople = 0;
	for(int i = 1; i < s.size()+1; ++i) {
		//cout << "sum --- " << sum << " " << endl;
		//cout << "numPeople --- " << numPeople << " " << endl;
		if(i > sum ) {
			int t = (i - sum);
			numPeople = max(numPeople, t);
		}
		sum  += (s[i] - '0');
	}
	printf("%d\n", numPeople);
}

int main() {
	int T, S;
	string shy;
	scanf("%d", &T);
	int cases = 0;
	while(T--) {
		cases++;
		shy = "";
		scanf("%d", &S);
		for(size_t i = 0; i < S+1; ++i) {
			char c;
			cin >> c;
			shy += c;
		}
		printf("Case #%d: ", cases);
		process(shy);		
	}
}