#include <cstdio>
#include <iostream>
#include <cstring>
#include <vector>
#include <queue>
#include <set>

using namespace std;

int test, ttest;
int n, l;
char s[1000010];
multiset<int> f;
deque<int> q;

bool consonants(char c) {
	return c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u';
}

bool isnext(const int j, const int i) {
	if (q.empty()) return i-j-2 + consonants(s[i]) + consonants(s[j+1]) >= n;

	bool ret = 0;	
	if (q.front() == j) {
		q.pop_front();
		if (q.empty()) ret = i-j-2 + consonants(s[i]) + consonants(s[j+1]) >= n;
		else {
			f.erase(q.front()-j-1);
			ret = f.lower_bound(n) != f.end() || i-q.back()-1+consonants(s[i]) >= n || q.front()-j-1-1+consonants(s[j+1]) >= n;
			f.insert(q.front()-j-1-1);
		}
		
		q.push_front(j);
	}
	else {
		ret = f.lower_bound(n) != f.end() || i-q.back()-1+consonants(s[i]) >= n || q.front()-j-1-1+consonants(s[j+1]) >= n;
	}
	return ret;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);

	scanf("%d", &test);
	for(ttest = 1; ttest <= test; ttest++) {
		scanf("%s%d", s+1, &n);
		l = strlen(s+1);
		f.clear();
		q.clear();
		long long ret = 0;
		for(int i = 1, j = 0; i <= l; i++) {
			if (!consonants(s[i])) {
				if (!q.empty()) f.insert(i-q.back()-1);
				q.push_back(i);
			}
			while (isnext(j, i)) {
				if (!q.empty() && q.front() == j) {
					q.pop_front();
					if (!q.empty()) f.erase(q.front()-j-1);
				}
				j++;
			}
			ret += j;
			// if (ttest == 7) cout << i << " " << j << endl;
		}
		printf("Case #%d: %lld\n", ttest, ret);
	}

	return 0;
}