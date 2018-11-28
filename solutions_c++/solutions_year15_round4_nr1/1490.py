#include <stdio.h>
using namespace std;
const int N = 1e2 + 11;
char s[N][N];
int n, m;
bool ok(int i, int j){
	if(s[i][j]=='.')	return 1;
	if(s[i][j]=='>' || s[i][j]=='<'){
		int d = s[i][j]=='>' ? 1 : -1;
		for(int k=j+d; k<m && k>=0; k+=d){
			if(s[i][k]^'.')	return 1;
		}
		return 0;
	}
	if(s[i][j]=='v' || s[i][j]=='^'){
		int d = s[i][j]=='v' ? 1 : -1;
		for(int k=i+d; k>=0 && k<n; k+=d){
			if(s[k][j]^'.')	return 1;
		}
		return 0;
	}
}
bool canchange(int i, int j){
	for(int k=0; k<m; k++){
		if(k==j)	continue;
		if(s[i][k]^'.')	return 1;
	}
	for(int k=0; k<n; k++){
		if(k==i)	continue;
		if(s[k][j]^'.')	return 1;
	}
	return 0;
}
int main()
{
	// freopen("in.txt", "r", stdin);
	// freopen("ou.txt", "w", stdout);
	int t, kase=0;
	scanf("%d", &t);
	while(t--){
		scanf("%d%d", &n, &m);
		for(int i=0; i<n; i++){
			scanf("%s", s[i]);
		}
		int yes = 1;
		int ans = 0;
		for(int i=0; i<n; i++){
			for(int j=0; j<m; j++){
				if(ok(i, j))	continue;
				if(canchange(i, j))	ans++;
				else	yes = 0;
			}
		}
		if(yes)	printf("Case #%d: %d\n", ++kase, ans);
		else	printf("Case #%d: IMPOSSIBLE\n", ++kase);
	}
	return 0;
}