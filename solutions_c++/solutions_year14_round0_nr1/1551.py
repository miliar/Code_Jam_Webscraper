#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

#define fr(a,b,c) for(int a = b; a < c; a++)
#define rep(a,b) fr(a,0,b)
#define pb push_back
#define db if(1)
#define ln puts("")

int n[2];
int r[2][4][4];

bool read(){
	rep(i,2){
		scanf("%d", &n[i]);
		n[i]--;
		rep(j,4) rep(k,4) scanf("%d", &r[i][j][k]);
	}	
	
	return true;
}

int cn = 1;

void process(){
	printf("Case #%d: ", cn++);

	int cont[17];
	memset(cont, 0, sizeof cont);
	
	rep(i,2) rep(j,4) cont[r[i][n[i]][j]]++;
	
	int res = -1;
	
	rep(i,17){
		if(cont[i] == 2){
			if(res == -1) res = i;
			else res = -2;
		}		
	}
	
	
	
	if(res == -2) puts("Bad magician!");
	else if(res == -1) puts("Volunteer cheated!");
	else printf("%d\n", res);
}

int main(){
	int t;
	scanf("%d", &t);
	
	while(t-- && read()) process();
	
	return 0;
}


