#include<bits/stdc++.h> 

using namespace std;

const int MAXN = 4e4 + 10;

typedef pair<int, int> PII;
typedef long long ll;

char s[MAXN], a[MAXN];

int main(){
	freopen("Al.in", "r", stdin);
	freopen("Al.out", "w", stdout);
	int T;
	cin>>T;
	for(int o = 1; o <= T; o++){
		printf("Case #%d: ", o);
		scanf("%s", s);
		int l = strlen(s);
		int cnt = 0, p = 0;
		for(int i = 0; i < l; i++){
			if (p && s[i] == a[p]){
				p--;
				cnt++;
			}
			else{
				a[++p] = s[i];
			} 
		}
		printf("%d\n", l / 2 * 5 + 5 * cnt);
	}
	return 0;
}
