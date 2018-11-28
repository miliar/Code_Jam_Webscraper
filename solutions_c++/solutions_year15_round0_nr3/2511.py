#include <bits/stdc++.h>
using namespace std;

char s[1<<20];

struct node{
	int s,v;
	node () {}
	node (int s, int v) : s(s), v(v) {}
	bool operator == (const node &b) const{
		return s==b.s && v==b.v;
	}
	void print () { printf("node: %d,%d\n", s, v); } 
}pre[1<<20],suf[1<<20];

node mult (node a, node b){
	int s = a.s * b.s;
	int v = (a.v==3 || b.v==3) ? (a.v+b.v-3) : (-1);
	if (v==-1){
		if (a.v == b.v)
			s*=-1, v=3;
		else{
			v=3-a.v-b.v;
			if ((a.v+1)%3 != b.v)
				s*=-1;
		}
	}
	return node(s,v);
}

node get (char s){
	if (s == 'i') return node(1, 0);
	if (s == 'j') return node(1, 1);
	if (s == 'k') return node(1, 2);
	assert(false);
}

void main2(){
	int L,X; scanf("%d%d", &L, &X);
	scanf("%s", s);
	for (int i=L; i<L*X; i++)
		s[i] = s[i-L];
	pre[0] = node(1, 3);
	int n = L*X;
	pre[0] = get(s[0]);
	for (int i=1; i<n; i++)
		pre[i] = mult(pre[i-1], get(s[i]));
	suf[n-1] = get(s[n-1]);
	for (int i=n-2; i>=0; i--)
		suf[i] = mult(get(s[i]), suf[i+1]);
	for (int i=0; i+1<n; i++) if (pre[i] == get('i')){
		node cur = get(s[i+1]);
		for (int j=i+2; j<n; j++){
			if (cur == get('j') && suf[j] == get('k')){
				puts("YES");
				return;
			}
			cur = mult(cur, get(s[j]));
		}
	}
	puts("NO");
}

int main(){
	int t; scanf("%d", &t);
	for (int o=1; o<=t; o++){
		printf("Case #%d: ", o); 
		main2();
	}
	return 0;
}
