#include <cstdlib>
#include <vector>
#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
#include <queue>
#include <stack>
#include <list>

using namespace std;

int main(int argc, char** argv) {
	int Tmax;
	scanf("%d", &Tmax);
	for (int T=1; T<=Tmax; T++) {
		string S;
		cin >> S;
		list<char> l = {S[0]};
		for (int i=1; i<S.size(); i++) {
			if (S[i] < l.front()) {
				l.push_back(S[i]);
			} else {
				l.push_front(S[i]);
			}
		}
		printf("Case #%d: ", T);
		for (auto i: l) {
			cout << i;
		}
		printf("\n");
	}
	
	return 0;
}

