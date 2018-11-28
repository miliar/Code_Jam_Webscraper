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


#include <stdio.h>
using namespace std;

int main () {

}