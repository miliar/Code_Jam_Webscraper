#include <stdio.h>
#include <string.h>

int N, R, P, S;
bool fail;
char str[9000], str2[9000];

char mapp[6][3][2] = {
	{{'P', 'R'}, {'R', 'S'}, {'P', 'S'}},
	{{'P', 'R'}, {'S', 'R'}, {'P', 'S'}},
	{{'P', 'R'}, {'S', 'R'}, {'S', 'P'}},
	{{'R', 'P'}, {'S', 'R'}, {'S', 'P'}},
	{{'R', 'P'}, {'R', 'S'}, {'S', 'P'}},
	{{'R', 'P'}, {'R', 'S'}, {'P', 'S'}},
};

void Rec(int id, int p, int r, int s){
	if(id == N){
		if(p == 1) str[0] = 'P';
		if(r == 1) str[0] = 'R';
		if(s == 1) str[0] = 'S';
		//printf("str = %c\n", str[0]);
		return;
	}

	int np = (p+r+s)/2 - (s);
	int nr = (p+r+s)/2 - (p);
	int ns = (p+r+s)/2 - (r);
	
	if(np < 0) fail = true;
	if(nr < 0) fail = true;
	if(ns < 0) fail = true;
	if(fail) return;
	
	Rec(id+1, np, nr, ns);
	if(fail) return;
	
	int to = 1 << (N-id-1);
	int dd;
	
	for(int i=0; i<to; i++){
		if(str[i] == 'P') dd = 0;
		if(str[i] == 'R') dd = 1;
		if(str[i] == 'S') dd = 2;
		
		//printf("la %d %d %c %c\n", id%6, dd, mapp[id%6][dd][0], mapp[id%6][dd][1]);
		str2[i*2] = mapp[id%6][dd][0];
		str2[i*2+1] = mapp[id%6][dd][1];
		str2[i*2+2] ='\0';
	}
	strcpy(str, str2);
	//printf("jadi %s\n", str);
}

int main(){
	int jcase;
	
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	scanf("%d", &jcase);
	for(int icase=0; icase<jcase; icase++){
		scanf("%d %d %d %d", &N, &R, &P, &S);
		
		fail = false;
		Rec(0, P, R, S);
		
		if(fail) printf("Case #%d: IMPOSSIBLE\n", icase+1);
		else printf("Case #%d: %s\n", icase+1, str);
	}
	
	return 0;
}
