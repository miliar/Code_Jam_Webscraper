#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
	int casenum;
	string p;

	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	cin >> casenum;
	for(int i = 1; i <= casenum; i++) {
		cin >> p;
		char pivot = p[0];
		int cnt = 1;
		for(int j = 1; j < p.size(); j++) {
			while(j < p.size() && p[j] == pivot) j++;
			if(j < p.size()) {pivot = p[j]; cnt++;}
		}
		if(pivot == '+') cnt--;
		printf("Case #%d: %d\n", i, cnt);
	}

	return 0;
}