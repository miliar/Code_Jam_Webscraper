#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <map>
#include <unordered_map>
#include <set>
#include <vector>
#include <algorithm>
#include <utility>
#include <iomanip>
#include <stack>
#include <string>

using namespace std;

int main() {
	FILE * stream1, *stream2;
	freopen_s(&stream1, "Text.txt", "r", stdin);
	freopen_s(&stream2, "OUTPUT.txt", "w", stdout);
	int T,times;
	cin >> T;
	times = 1;
	while (T--) {
		string S;
		cin >> S;
		string lastword = "";
		for (int i = 0; i < S.size(); i++) {
			if (lastword.size() == 0)
				lastword += S[i];
			else if (lastword[0] <= S[i])
				lastword = S[i] + lastword;
			else 
				lastword = lastword + S[i];
		}
		cout << "Case #" << times << ": " << lastword << endl;
		times++;
	}
	return 0;
}