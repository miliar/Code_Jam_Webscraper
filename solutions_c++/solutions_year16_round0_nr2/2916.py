#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<string>
#include<set>
#include<map>
#include<vector>
using namespace std;
typedef long long LL;
int T, f[102][2], slen, tlen;
char s[102], t[102];
int main(){
	freopen("B_in.txt", "r", stdin);
	freopen("B_out.txt", "w", stdout);
	scanf("%d", &T);
	for(int C = 1; C<=T; ++C){
		scanf("%s", s);
		slen = strlen(s);
		t[0] = s[0];
		tlen = 1;
		for(int i = 1; i<slen; ++i)
			if(s[i]!=s[i-1])
				t[tlen++] = s[i];
		f[0][0] = (t[0] == '+');
		f[0][1] = (t[0] == '-');
		for(int i = 1; i<tlen; ++i){
			f[i][0] = min(f[i-1][0] + (t[i] == '+')*2, f[i-1][1] + 1);
			f[i][1] = min(f[i-1][0] + 1, f[i-1][1] + (t[i] == '-')*2);
		}
		printf("Case #%d: %d\n", C, f[tlen-1][1]);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
