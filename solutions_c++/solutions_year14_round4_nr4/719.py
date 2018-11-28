#include<cstdio>
#include<cstring>
#include<algorithm>
#include<iostream>
using namespace std;
const int MAX = 100 + 10;

int n, m;
string rec[MAX];
int stk[MAX], ans, cnt;

int cmp(string &A, string &B){
	int p = 0;
	int len = min(A.length(), B.length());
	while(p < len){
		if(A[p]==B[p]) p++;
		else return p;
	}
	return p;
}

void dfs(int x){
	if(x==n){
		int tans = 0;
		for(int i = 1 ; i <= m ; i++){
			int last = -1;
			for(int j = 0 ; j < n ; j++){
				if(stk[j]==i){
					if(last == -1){
						tans += rec[j].length();
					}else{
						tans += rec[j].length() - cmp(rec[j], rec[last]);
					}
					last = j;
				}
			}
			if(last != -1) tans++;
		}
		if(tans > ans) ans = tans, cnt = 1;
		else if(tans == ans) cnt++;
		return;
	}
	for(int i = 1 ; i <= m ; i++){
		stk[x] = i;
		dfs(x+1);
	}
}

int main(){
	freopen("Dsmall1.in", "r", stdin);
	freopen("Dsmall1.out", "w", stdout);
	int TN;
	scanf("%d", &TN);
	for(int casen = 1 ; casen <= TN ; casen++){
		scanf("%d %d", &n, &m);
		for(int i = 0 ; i < n ; i++){
			cin >> rec[i];
		}
		sort(rec, rec+n);
		ans = 0, cnt = 0;
		dfs(0);
		printf("Case #%d: %d %d\n", casen, ans, cnt);
	}
	return 0;
}
