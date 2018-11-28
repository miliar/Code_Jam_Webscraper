#include<cstdio>
#include<cstring>
#include<cmath>
#include<climits>
#include<cfloat>

#include<iostream>
#include<string>
#include<limits>
#include<sstream>

#include<utility>
#include<vector>
#include<set>
#include<stack>
#include<queue>
#include<map>
#include<algorithm>

using namespace std;
typedef long long LL;

vector<int> v;

inline vector<int>::iterator doit(int &pos) {
	vector<int>::iterator index = v.begin();
	vector<int>::iterator i;
	int ii;
	for (i = v.begin(), ii = 0; i != v.end(); i++, ii++) {
		if (*i < *index) {
			index = i;
			pos = ii;
		}
	}

	return index;
}

int main() {
	int caseNum;
	char dummy; //read the '\n' after the caseNum
	scanf("%d%c", &caseNum, &dummy);
	for (int caseCount = 1; caseCount <= caseNum; caseCount++) {
		cout << "Case #" << caseCount << ": ";
		int n;
		scanf("%d", &n);
		v = vector<int>(n);
		for (int i = 0; i < n; i++) {
			cin >> v[i];
		}
		LL res = 0;
		while (v.size()) {
			int pos = 0;
			vector<int>::iterator in = doit(pos);
			res += min(pos, (int) (v.size() - 1 - pos));
			v.erase(in);
		}
		printf("%d\n", res);
	}
	return 0;
}
