#include<iostream>
#include<cstdio>
#include<cstring>
#include<queue>
#include<ctime>
#include<cstdlib>
#define rep(i, l, r) for(int i = l; i <= r; ++i)
using namespace std;
//const int maxstate = 1 << 19;
int /*d[maxstate],*/ n;
char s[4000];
//queue<int> q;
//bool inq[maxstate];
/*bool bit(int state, int pos){
	return (state >> pos) & 1;
}*/
int main(){
	int cas;	
	cin >> cas;
	rep(Cas, 1, cas){
		scanf("%s", s + 1);
		//printf("Cas = %d\n", Cas);
		//memset(d, -1, sizeof(d));
		n = strlen(s + 1);
		/*n = 18;
		rep(i, 1, n) s[i] = rand() & 1 ? '+' : '-';
		int tmp = 0;
		rep(i, 1, n)
			if(s[i] == '+') tmp |= 1 << (i - 1);
		d[tmp] = 0;
		q.push(tmp);
		while(!q.empty()){
			int now = q.front(); q.pop();
			inq[now] = 0;
			rep(i, 1, n){
				int tmp = now;
				rep(j, 0, i - 1)if(bit(tmp, j)) tmp ^= 1 << j;
				rep(j, 0, i - 1)
					if(!bit(now, j)) tmp ^= 1 << (i - j - 1);
				//0printf("now = %d i = %d tmp = %d\n", now, i, tmp);
				if(d[tmp] == -1){
					d[tmp] = d[now] + 1;
					q.push(tmp);
				}
			}
		}*/
		//printf("Case #%d: %d\n", Cas, d[(1 << n) - 1]);
		int cnt = 0;
		rep(i, 1, n){
			if(s[i] == '-') {
				if(i == 1 || s[i - 1] != '-')++cnt;
			}
		}
		cnt <<= 1;
		if(cnt && s[1] == '-') --cnt;
		printf("Case #%d: %d\n", Cas, cnt);
		/*if(cnt != d[(1<<n) - 1]){
			cout << "error " << cnt << " " << d[(1 << n) - 1] << endl;
		}*/
	}
	return 0;
} 
