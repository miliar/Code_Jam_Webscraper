#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<set>
#include<queue>
#include<map>
using namespace std;
#define PII pair<int,int>
#define X first
#define Y second
#define PB push_back
#define FOR(i,a,b) for (int i=(a);i<(b);i++)
#define FOE(i,a,b) for (int i=(a);i<=(b);i++)
#define INF (1 << 30)
#define EPS (1e-9)
#define REP(i,n) FOR(i,0,n)
#define LL long long
int n, m;
char s[30][20000];
vector<string> vec[300];
map<string, int> mp;
int m2[30][3000];
int a[200000];
int d[100000];
int c[30];
int main(){
	int T;
	scanf("%d", &T);
	FOE(cc,1,T){
		int sz = 0;
		mp.clear();
		FOR(i,0,300) vec[i].clear();
		scanf("%d", &n);
		gets(s[0]);
		FOR(i,0,n) gets(s[i]);
		FOR(i,0,n){
			char *ptr = strtok(s[i], " ");
			int nw = 0;
			while(ptr != NULL){
		//		vec[i].PB(ptr);
				if (!mp.count(ptr)) mp[ptr] = sz++;
			//	printf("%d %d\n", i, nw);
				m2[i][nw++] = mp[ptr];
				ptr = strtok(NULL, " ");
			}
			c[i] = nw;
		}
		int ans = sz;
//		printf("%d\n", sz);
//		puts("asd");
		/*
		FOR(i,0,n){
//			FOR(j,0,vec[i].size()) cout << vec[i][j] << " " ;
			FOR(j,0,vec[i].size()) printf("%d %d\n", mp[vec[i][j]], m2[i][j]);
			puts("");
		}
		*/
//		printf("%d\n", n - 2);
		
//		FOR(i,0,n) printf("%d ", c[i]); puts("");

	FOR(j,0,sz) d[j] = 0;
			FOR(j,0,c[0]) d[m2[0][j]] |= 1;
			FOR(j,0,c[1]) d[m2[1][j]] |= 2;
		FOR(i,0,1 << (n - 2)){
					FOR(j,0,sz) a[j] = 0;
			FOR(j,0,n - 2){
				int tmp = 1 << j;
				if (i & tmp){
					FOR(k,0,c[j + 2]) a[m2[j + 2][k]] |= 2;
				}
				else{
					//				if (!i) printf("%d %d %d\n", i, j, tmp);
					FOR(k,0,c[j + 2]) a[m2[j + 2][k]] |= 1;
				}
			}
			int tc = 0;
			FOR(j,0,sz) if ((a[j] | d[j]) == 3) tc++;
			//		FOR(j,0,sz) printf("%d ", a[j]); puts("");
			//		printf("%d %d\n", i, tc);
			ans = min(ans, tc);
		}
		printf("Case #%d: ", cc);
		printf("%d\n", ans);
	}
	return 0;
}

