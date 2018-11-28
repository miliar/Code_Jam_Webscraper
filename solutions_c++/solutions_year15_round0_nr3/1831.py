#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;
int n, m;
char s[10010];
int a[80080];
int dir[4][4] = {{0, 1, 2, 3},
				{1, 0, 3, 2},
				{2, 3, 0, 1},
				{3, 2, 1, 0}};
int dir2[4][4] = {{1, 1, 1, 1},
				{1, -1, 1, -1},
				{1, -1, -1, 1},
				{1, 1, -1, -1}};
int gao(){
	int t = min(m, 8) * n;
	for (int i = 0; i < n; ++i)
		if (s[i] == 'i') a[i] = 1;
		else if (s[i] == 'j') a[i] = 2;
		else a[i] = 3;
		
	for (int i = 0, j = n; j < t; ++j, ++i)
		a[j] = a[i];
		
	int sig = 1;
	int now = 0;
	int state = 0;
	int sig2, now2;
	for (int i = 0; i < t; ++i){
		sig *= dir2[now][a[i]];
		now = dir[now][a[i]];
		a[i] = sig * (now + 1);
		//cout<<' '<<a[i];
		if ((state == 0)&&(sig * now == 1))
			state = 1;
		if ((state == 1)&&(sig * now == 3))
			state = 2;
	}
	//cout<<' '<<state<<' '<<a[n - 1]<<endl;
	if (state != 2) return false;
	if (a[n - 1] == 1) return false;
	if (a[n - 1] == -1) return m % 2 == 1;
	return m % 4 == 2;
}
int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t = 0, tt;
	for (scanf("%d ", &tt); t < tt; ++t){
		scanf("%d %d ", &n, &m);
		scanf("%s ", s);
		int ans = gao();
		//for (int i = 0; i < n; ++i)
		//	printf("%d ", d[i]);
		printf("Case #%d: %s\n", t + 1, ans? "YES" : "No");
	}
} 
