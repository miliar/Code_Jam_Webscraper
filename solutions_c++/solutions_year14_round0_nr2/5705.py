//#include <stdio.h>
//#include <queue>
//#include <algorithm>
//#include <stdio.h>
//using namespace std;
//
//struct str{
//	int x, y, value;
//	bool operator < (str b)const{
//		return value > b.value;
//	}
//}s;
//
//struct strr{
//	int x, y, value;
//	bool operator < (strr b)const{
//		if(value != b.value)
//		return value > b.value;
//		if(x != b.x) return x < b.x;
//		return y > b.value;
//	}
//}ss;
//
//
//int main () {
//	int t;
//	scanf("%d", &t);
//	for(int tt = 1; tt<=t; tt++){
//		bool mapx[120] = {}, mapy[120] = {};
//		
//		priority_queue<str> q;
//		priority_queue<strr> qq;
//		int m, n;
//		scanf("%d%d", &m, &n);
//		for(int i=0; i<m; i++){
//			for(int j=0; j<n; j++){
//				scanf("%d", &s.value);
//				s.x = i;
//				s.y = j;
//				q.push(s);
//				ss.x = i;
//				ss.y = j;
//				ss.value = s.value;
//				qq.push(ss);
//			}
//		}
//		int ans = 0, flag = 0;
//		int M;
//		M = m > n ? m : n;
//		while(flag < M){
//			s = q.top();
//			q.pop();
//			if(m == n && ( mapx[s.x] || mapy[s.y]) ) continue;
//			if(m > n && mapx[s.x]) continue;
//			if(n > m && mapy[s.y]) continue;
//			ans += s.value;
//			mapx[s.x] =1;
//			mapy[s.y] =1;
//			flag++;
//		}
//		int anss = 0, flagg = 0;
//		for(int i=0; i<119; i++) mapx[i] = mapy[i] = 0;
//		while(flagg < M){
//			ss = qq.top();
//			qq.pop();
//			if(m == n && ( mapx[ss.x] || mapy[ss.y]) ) continue;
//			if(m > n && mapx[ss.x]) continue;
//			if(n > m && mapy[ss.y]) continue;
//			anss += ss.value;
//			mapx[ss.x] =1;
//			mapy[ss.y] =1;
//			flagg++;
//		}
//		ans = ans < anss ? ans : anss;
//		printf("Case %d: ", tt);
//		printf("%d", ans);
//		if(tt != t) puts("");
//	}
//}

//#include <stdio.h>
//#include <string.h>
//#include <algorithm>
//using namespace std;
//
//bool mx[120], my[120];
//
//int main () {
//	int t;
//	scanf("%d", &t);
//	for(int tt = 1; tt <= t; tt++){
//		memset(mx, 0, sizeof(mx));
//		memset(my, 0, sizeof(my));
//
//	}
//}


#include <cstdio>
#include <iostream>
using namespace std;

double c, f, x;

double cal(int M){
	double MM = M;
	double tk = (x)/(2+MM * f);
	for(int i=0; i<M; i++) tk += c/(2+i*f);
	return tk;
}

int main () {
	//freopen("outt.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int tt = 1; tt <= t; tt ++){
		double m = 100000000, mm;
		scanf("%lf%lf%lf", &c, &f, &x);
		int L = 0, H = 1000000, T = 200;
		for(int i=0; i<=2000; i++){
			mm = cal(i);
			if(mm < m) m = mm;
		}
		//m = cal((L+H)/2);
		//while(H-L >1){
		//	int M = (H+L)/2;
		//	//printf("%d %d\n", L, H);
		//	double a = cal((M+H)/2), b = cal((M+L)/2);
		//	if(a > b) { H = M; m = min(m, b); }
		//	else { L = M; m = min(m, a);}
		//}
		printf("Case #%d: %.7lf\n",tt,  m);
	}
	//fclose(stdout);
}

//#include <cstdio>
//#include <cstring>
//using namespace std;
//
//int flag, r, c, m, ok, dir[16] = {1, 0, 1, 1, 0, 1, -1, 1, -1, 0, -1, -1, 0, -1, 1, -1};
//bool vis[20][20], map[20][20];
//
//void dfs(int x, int y){
//	int kk = 0;
//	for(int i=0; i<15; i+=2){ 
//		if(x + dir[i] > r || x + dir[i] <= 0 || y + dir[i+1] > c || y +dir[i+1] <=0) continue;
//		if(map[x + dir[i]][y + dir[i+1]]) {
//			vis[x][y] = 1;
//			kk = 1;
//			break;
//		}
//	}
//	flag++;
//	if(kk) return;
//	for(int i=0; i<15; i+=2){
//		if(x + dir[i] > r || x + dir[i] <= 0 || y + dir[i+1] > c || y +dir[i+1] <=0) continue;
//		if(vis[x+dir[i]][y + dir[i+1]]) continue;
//		vis[x+dir[i]][y + dir[i+1]] = 1;
//		dfs(x+dir[i], y + dir[i+1]);
//	}
//}
//
//void check(){
//	for(int i=1; i<=r; i++)
//		for(int j=1; j<=c; j++){
//			int kk = 0;
//			if(map[i][j]) continue;
//			for(int k = 0; k<15; k+=2)
//				if(map[i+dir[k]][j+dir[k+1]]) {kk = 1; break;}
//			if(kk) continue;
//			flag = 0;
//			memset(vis, 0, sizeof(vis));
//			vis[i][j] = 1;
//			dfs(i, j);
//			if(flag == r*c-m) {
//				for(int ii=1; ii<=r; ii++){
//					for(int jj = 1; jj <= c; jj++){
//						if(ii == i && jj == j) printf("c");
//						else if(map[ii][jj]) printf("*");
//						else printf(".");
//					}
//					puts("");
//				}
//				ok = 1;
//				return;
//			}
//			else return;
//		}
//}
//
//void rand(int x, int y, int stp){
//	if(ok) return;
//	if(stp == m){
//		check();
//	}
//	else {
//		for(int i=x; i<=r; i++){
//			for(int j=y; j<=c; j++){
//				if(map[i][j]) continue;
//				map[i][j] = 1;
//				rand(i, j, stp+1);
//				map[i][j] = 0;
//			}
//		}
//	}
//}
//
//int main () {
//	int t;
//	scanf("%d", &t);
//	for(int tt = 1; tt <= t; tt++){
//		memset(map, 0, sizeof(map));
//		printf("Case #%d:\n", tt);
//		ok = 0;
//		scanf("%d%d%d", &r, &c, &m);
//		if(r*c-m == 1) {
//			printf("c");
//			for(int j = 2; j<=c; j++) printf("*");
//			puts("");
//			for(int i = 2; i<=r; i++){
//				for(int j=1; j<=c; j++) printf("*");
//				puts("");
//			}
//			continue;
//		}
//		rand(1,1,0);
//		if(!ok) puts("Impossible");
//	}
//}