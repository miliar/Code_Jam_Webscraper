#include <cstdio>
#include <iostream>
#include <map>
#include <string>

#include <vector>

using namespace std;
int cache[10001][ 10001];
int val[256][ 256 ];

void init() {
	val[ 1 ][ 1 ] = 1 ;
	val[ 1 ][ 'i' ] = 'i';
	val[ 1 ][ 'j' ] = 'j';
	val[ 1 ][ 'k' ] = 'k';
	val[ 'i' ][ '1' ] = 'i';
	val[ 'i' ][ 'i' ] = -1;
	val[ 'i' ][ 'j' ] = 'k';
	val[ 'i' ][ 'k' ] = -1 * 'j';
	val[ 'j' ][ '1' ] = 'j';
	val[ 'j' ][ 'i' ] = -1 * 'k';
	val[ 'j' ][ 'j' ] = -1;
	val[ 'j' ][ 'k' ] = 'i';
	val[ 'k' ][ '1' ] = 'k';
	val[ 'k' ][ 'i' ] = 'j';
	val[ 'k' ][ 'j' ] =  -1 *'i';
	val[ 'k' ][ 'k' ] = -1;
}

int eval(string str, int a, int b) {
        if (cache[a][b] != -1) return cache[a][b];
	int ans = str[0];
	for(int i = 1; i < str.size(); i++) {
		int sign = 1;
		if (ans < 0) {
			ans = ans * -1;
			sign = -1;
		}
		ans = val[ans][ str[i] ] ;
		ans = ans * sign;
	}
        cache[a][b] = ans;
	return ans;
}

bool is_possible(string str, int length, int repeat) {

	string res;
	for(int i = 0; i < repeat; i++) {
		res += str;
	}
	if (res.length() < 3) {
		return false;
	}

        for(int i = 0; i < res.size(); i++) {
          int partial_ans = 1;
          for(int j = i; j < res.size(); j++) {
            int sign = 1;

            if (partial_ans < 0) {
              sign = -1;
              partial_ans = partial_ans * -1;
            }

            partial_ans = sign * val[partial_ans][ res[j] ];
            cache[i][j] = partial_ans;
          }
          // cerr << "Iteration i " << i << endl;
        }

	for(int i = 1; i < res.length(); i++) {
		for(int j = i ; j < res.length() - 1; j++) {
			if (eval("", 0, i-1) == 'i' && eval("", i, j) == 'j' && eval("", j+1, res.length() - 1) == 'k') {
				return true;
			}
		}
	}
	return false;
}
int main() {
        init();
	int T;
	scanf("%d", &T);

	for(int cases = 1; cases <= T; cases ++) {
		int length;
		int repeat;
		string str;
		scanf("%d %d", &length, &repeat);
		cin >> str;
		if (is_possible(str, length, repeat)) {
			printf("Case #%d: YES\n", cases);
		} else {
			printf("Case #%d: NO\n", cases);
		}
	}
	return 0;
}
