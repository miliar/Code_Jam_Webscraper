/*
 * A Large
 * TOPIC:
 * status:
 */
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
using namespace std;
#define N 0x400

char s[N];
int n;

int main() {
	int i,j,k,ts,cs = 0,m;
	for ( scanf("%d",&ts); ts--; ) {
		scanf("%s",s); n = strlen(s);
		string res = "";
		res += s[0];
		for ( m = 1, i = 1; i < n; ++i, ++m ) {
			char ch = s[i];
			for ( j = 0; j < m && res[j] == ch; ++j );
			if ( j == m ) { res += ch; continue ; };
			if ( res[j] < ch ) res = ch+res;
			else res += ch;
		}
		printf("Case #%d: %s\n",++cs,res.c_str());
	}
	return 0;
}

