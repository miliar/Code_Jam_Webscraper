#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<string>
#include<cstdlib>
#include<cmath>
#include<cctype>
#include<ctime>
#include<algorithm>
#include<iomanip>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<cassert>
#include<bitset>

using namespace std;

const int N = 20010;
char s[N];

int main() {
	int T;
	scanf("%d", &T);
	for(int cc = 1; cc <= T; cc++){
		scanf("%s", s);
		int l, x = strlen(s);
		int ans = 0;
		int flag = 1;
		while(flag) {
			flag = 0;
			l = strlen(s);
			int nxt = 0;
			for(int i = 0; i < l; ++i){
				if(i == l - 1 || s[i] != s[i + 1]){
					s[nxt++] = s[i];
				} else {
					ans++;
					i++;
					flag = 1;
				}
			}
			s[nxt] = 0;
		}
		printf("Case #%d: %d\n", cc, x / 2 * 5 + ans * 5);
	}
	return 0;
}

