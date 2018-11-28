#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>

using namespace std;

const size_t MAXLEN = 200;

char buff[MAXLEN];

int solve(const vector<bool>& vec) {
	int num = 0;
	for (int i = vec.size() - 1; i >= 0; --i) {
		if (vec[i] && (num % 2 == 1)) ++num;
		else if (!vec[i] && (num % 2 == 0)) ++num;
	}
	return num;
}
		
			

int main() {
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	int T;
	scanf("%d\n", &T);
	for (int i = 1; i <= T; ++i) {
		vector<bool> vec;
		scanf("%s", buff);
		int len = strlen(buff);
		for (int i = 0; i < len; ++i)
			vec.push_back(buff[i] == '+');
		printf("Case #%d: %d\n", i, solve(vec));
	}
	return 0;
}

	
	
