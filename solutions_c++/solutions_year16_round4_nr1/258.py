#include<iostream>
#include<cstdio>
#include<cstring>
#define rep(i, l, r) for(int i = l; i <= r; ++i)
using namespace std;
int n, s[4];
char ans[10010], str[10001];
void dfs(int step, int k, int l, int r){
	if(!step) {
		if(!k) str[l] = 'R';
		else if(k == 1) str[l] = 'P';
		else str[l] = 'S';
		return ;
	}
	int mid = (l + r) >> 1;
	dfs(step - 1, k, l, mid);
	dfs(step - 1, (k - 1 + 3) % 3, mid + 1, r);
	int cnt = 0;
	bool flag = 1;
	for(int i = l; i <= mid; ++i){
		if(str[l + cnt] != str[mid + 1 + cnt]){
			if(str[l + cnt] < str[mid + 1 + cnt]) flag = 1;
			else flag = 0;
			break;
		}
		++cnt;
	}
	if(!flag){
		cnt = 0;
		rep(i, l, mid){
			swap(str[l + cnt], str[mid + 1 + cnt]);			
			++cnt;
		}
	}
}
int main(){
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	int T;
	cin >> T;
	rep(cas, 1, T){
		cin >> n;
		printf("Case #%d: ", cas);
		rep(i, 0, 2)
			cin >> s[i];
		bool ok = 0;
		rep(i, 0, 2){
			dfs(n, i, 1, (1 << n));
		//	printf("i = %d\n", i);
			//puts(str + 1);
			int cnt[4];
			memset(cnt, 0, sizeof(cnt));
			rep(j, 1, (1 << n))
				if(str[j] == 'R')++cnt[0];
				else if(str[j] == 'P') ++ cnt[1];
				else ++cnt[2];
		/*	rep(j, 0, 2)
				printf("cnt[%d] = %d\n", j, cnt[j]);
		*/	bool fail = 0;
			rep(j, 0, 2)
				if(s[j] != cnt[j]) fail = 1;
		//	printf("fail = %d\n", fail);
			if(fail)
				continue;
			if(!ok) {
				rep(j, 1, (1 << n))
					ans[j] = str[j];
				ok = 1;
			}
			else {
				bool flag = 0;
				rep(j, 1, (1 << n))
					if(ans[j] != str[j]){
						if(str[j] < ans[j]){
							flag = 1;
						}
						else flag = 0;
						break;
					}
				if(flag)
					rep(j, 1, (1 << n))
						ans[j] = str[j];
			}
		}
		if(!ok){
			puts("IMPOSSIBLE");
			continue;
		}
		rep(j, 1, (1 << n))
			putchar(ans[j]);
		printf("\n");
	}
	return 0;
}
