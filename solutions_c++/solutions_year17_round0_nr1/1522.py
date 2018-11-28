#include <bits/stdc++.h>

using namespace std;
typedef long long LL;

const int MAXN = 1010;
char str[MAXN];

void flip(int start, int end) {
	for (int i = start; i < end; i++) {
		if (str[i] == '-') str[i] = '+';
		else str[i] = '-';
	}
}

int main() {
  freopen("input", "r", stdin);
  freopen("output", "w", stdout);
  int T; cin >> T;
  for (int kase = 1; kase <= T; kase++) {
  	int K, ret = 0;
  	bool flag = true;
    cin >> str >> K;
    int len = strlen(str);
    for (int i = 0; i < len; i++) {
    	if (str[i] == '-') {
    		if (len - i >= K) {
	    		flip(i, i + K);
	    		ret++;
    		} else {
	    		flag = false;
	    		break;
	    	}
	    }
    }
    if (!flag) {
    	cout << "Case #" << kase << ": IMPOSSIBLE" << endl;
    } else {
    	cout << "Case #" << kase << ": " << ret << endl;
    }
  }
  return 0;
}
