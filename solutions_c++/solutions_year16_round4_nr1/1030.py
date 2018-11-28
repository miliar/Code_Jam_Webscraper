#define _CRT_SECURE_NO_WARNINGS
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<iostream>
#include<queue>
using namespace std;
typedef struct State{
	string s;
	char val;
	friend bool operator < (State a, State b){
		return a.s < b.s;
	}
}State;
State s[5005];
State Q[3][5005];
bool judge(int x, int y, int z,int N){
	int c[3] = { 0 };
	if (N == 0) return 1;
	int y1 = (1 << (N - 1)) - z;
	int z1 = x - y1;
	if (y1 < 0) return 0;
	if (y1 > y || y1 > x || x - y1 > z) return 0;
	for (int i = 0; i < (1 << N); i++){
		if (s[i].val == 'P') Q[0][c[0]++] = s[i];
		if (s[i].val == 'R') Q[1][c[1]++] = s[i];
		if (s[i].val == 'S') Q[2][c[2]++] = s[i];
	}
	sort(Q[0], Q[0] + c[0]);
	sort(Q[1], Q[1] + c[1]);
	sort(Q[2], Q[2] + c[2]);
	int j = 0, k = 0,i=0;
	for (i = 0; i < c[0]; i++){
		State s1 = Q[0][i],s2;
		if (j<y1){
			s2 = Q[1][j++];
			s1.val = 'P';
		}
		else{
			s2 = Q[2][k++];
			s1.val = 'S';
		}
		if (s1.s < s2.s) {
			s1.s += s2.s;
		}
		else {
			s1.s = s2.s + s1.s;
		}
		s[i] = s1;
	}
	for (; i < y - y1 + c[0]; i++){
		State s1 = Q[1][j++], s2=Q[2][k++];
		if (s1.s < s2.s) {
			s1.s += s2.s;
		}
		else {
			s1.s = s2.s + s1.s;
		}
		s1.val = 'R';
		s[i] = s1;
	}
	return	judge(y1, y - y1, z - y + y1, N - 1);
}
int P, R, S;
int main(){
	freopen("As.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t,n,ca=0;
	scanf("%d", &t);
	while (t--){
		scanf("%d%d%d%d", &n, &R, &P, &S);
		for (int i = 0; i < R; i++){
			s[i].s = "R";
			s[i].val = 'R';
		}
		for (int i = R; i < R+P; i++){
			s[i].s = "P";
			s[i].val = 'P';
		}
		for (int i = R+P; i < R+P+S; i++){
			s[i].s = "S";
			s[i].val = 'S';
		}
		printf("Case #%d: ", ++ca);
		if (!judge(P, R, S,n)){
			printf("IMPOSSIBLE\n");
		}
		else{
			printf("%s\n", s[0].s.c_str());
		}
	}
	return 0;
}