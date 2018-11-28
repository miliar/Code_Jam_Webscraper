#include<bits/stdc++.h>
#define fi first
#define se second
#define pb push_back
#define mk make_pair
#define vi vector<int>
using namespace std;
typedef pair<int, int> pii;
int T, k, n;
char s[1010];
void tran(int x){
	for(int i=x; i<x+k; i++){
		if(s[i]=='-')
			s[i]='+';
		else
			s[i]='-';
	}
}
int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &T);
	for(int cas=1; cas<=T; cas++){
		int ans=0;
		scanf("%s%d", s, &k);
		n=strlen(s);
		for(int i=0; i+k-1<n; i++){
			if(s[i]=='-'){
				ans++;
				tran(i);
			}
		}
		bool ok=1;
		for(int i=0; i<n; i++)
			if(s[i]=='-'){
				ok=0;
				break;
			}
		printf("Case #%d: ", cas);
		if(ok)printf("%d\n", ans);
		else puts("IMPOSSIBLE");
	}
	return 0;
}


