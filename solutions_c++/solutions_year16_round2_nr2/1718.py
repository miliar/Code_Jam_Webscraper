#include <cstring>
#include <cstdio>
#include <iostream>
using namespace std;
char a[100], b[100];
int dif;

void dfs(int d, char s[], char t[], int l) {
	if (d==l*2) {
		int diff=0;
		for (int i=0; i<l; ++i)
			diff=diff*10+s[i]-t[i];
		if (diff<0) diff=-diff;
		if (diff<dif || (diff==dif && strcmp(s, a)<0) ||
		(diff==dif && strcmp(s,a)==0 && strcmp(t,b)<0)) {
			dif=diff;
			strcpy(a,s);
			strcpy(b,t);
		}
	} else {
		if (d<l) {
			if (s[d]=='?') {
				for (s[d]='0'; s[d]<='9'; ++s[d])
					dfs(d+1, s, t, l);
				s[d]='?';
				}
			else dfs(d+1, s, t, l);
		} else {
			if (t[d-l]=='?') {
				for (t[d-l]='0'; t[d-l]<='9'; ++t[d-l])
					dfs(d+1, s, t, l);
				t[d-l]='?';
				}
			else dfs(d+1, s, t, l);
		}
	}
}

int main() {
	freopen("B-small-attempt1.in","r",stdin);
	freopen("b.out","w",stdout);
	char s[100], t[100];
	int TT;
	cin>>TT;
	for (int T=1; T<=TT; ++T) {
		scanf(" %s %s", s, t);
		int l=strlen(s);
		dif=99999;
		dfs(0, s, t, l);
		printf("Case #%d: %s %s\n", T, a, b);
	}
}
