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

char s[110];
int que[110], f = 0;

int main() {
	int TT;
	scanf("%d", &TT);
	for(int cc = 1; cc <= TT; ++cc){
		f = 0;
		scanf("%s", s);
		int l = strlen(s);
		for(int i = 0; i < l; ++i){
			if(i == 0 || s[i] != s[i - 1]) {
				if(s[i] == '-')que[f++] = 0;
				else que[f++] = 1;
			}
		}
	  if(que[0] == 0) printf("Case #%d: %d\n", cc, 1+(f-1)/2*2);
		else printf("Case #%d: %d\n", cc, f/2*2);
	}
	return 0;
}

