#include<cstdio>
#include<iostream>
#include<cstring>
#include<string>
#include<algorithm>
using namespace std;

int T, N, R, P, S;
int r[11], p[11], s[11];
string str[11];

string dfs(int dep, char ch) {
	if (dep==1) {
		if(ch=='R') return "RS";
		if(ch=='P') return "PR";
		if(ch=='S') return "PS";
	}
	string s1, s2;
	if(ch=='R') {
		s1=dfs(dep-1, 'R');
		s2=dfs(dep-1, 'S');
	}
	if(ch=='P') {
		s1=dfs(dep-1, 'P');
		s2=dfs(dep-1, 'R');
	}
	if(ch=='S') {
		s1=dfs(dep-1, 'P');
		s2=dfs(dep-1, 'S');
	}
	if(s1+s2<s2+s1) return s1+s2;
	return s2+s1;
}

void gen(int id, char ch) {
	str[id] = dfs(N, ch);
	for(int i=0;i<str[id].size();i++) {
		if(str[id][i] == 'R') r[id] ++;
		if(str[id][i] == 'P') p[id] ++;
		if(str[id][i] == 'S') s[id] ++;
	}
}

int main() {
	scanf("%d", &T);
	for(int CASE = 1; CASE <= T; CASE++) {
		scanf("%d%d%d%d", &N, &R, &P, &S);
		memset(r, 0, sizeof r);
		memset(p, 0, sizeof p);
		memset(s, 0, sizeof s);
		gen(0, 'R');
		gen(1, 'P');
		gen(2, 'S');
		string ans = "";
		for(int i=0;i<3;i++)
			if(r[i]==R&&p[i]==P&&s[i]==S) {
				if(ans.length()==0 || ans>str[i]) ans = str[i];
			}
		cout<<"Case #"<<CASE<<": ";
		if(ans.length()==0) cout<<"IMPOSSIBLE"<<endl;
		else cout<<ans<<endl;
	}
	
	return 0;
}