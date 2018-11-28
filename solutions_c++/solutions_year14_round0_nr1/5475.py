#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
#define MAXN 17
int f[MAXN];
int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t, tt;
	for (scanf("%d ", &tt), t = 0; t < tt; ++t){
		memset(f, 0, sizeof(f));
		int n;
		cin>>n;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j){
				int x;
				cin>>x;
				if (n - 1 == i) ++f[x];
			} 
		cin>>n;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j){
				int x;
				cin>>x;
				if (n - 1 == i) ++f[x];
			} 
		int cnt = 0;
		int k;
		for (int i = 1; i < MAXN; ++i)
			if (f[i] > 1){
				++cnt;
				k = i;
			}
		if (cnt == 0) printf("Case #%d: Volunteer cheated!\n", t + 1);
		else if (cnt >= 2) printf("Case #%d: Bad magician!\n", t + 1);
		else printf("Case #%d: %d\n", t + 1, k);
	}
} 
