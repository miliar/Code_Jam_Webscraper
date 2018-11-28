#include <bits/stdc++.h>
using namespace std;

typedef struct {
	int p;
	int m;
	int ar;
} mSet;

int adj[60][60];
int nAdj[60];
int cor[60];
mSet cs[60];
int numCs;
int n;
void dfs(int x){
	cs[numCs].ar+=nAdj[x];
	if(x < n){
		cs[numCs].m++;
	} else {
		cs[numCs].p++;
	}
	for(int i = 0; i < nAdj[x]; i++){
		int next = adj[x][i];
		if(cor[next] == 0){
			cor[next] = 1;
			dfs(next);
		}
	}
}

bool comp(mSet a, mSet b){
	return max(a.m, a.p) > max(b.m, b.p);
}

int main(){
	int t;
	scanf(" %d", &t);
	for(int k = 1; k <= t; k++){
		scanf(" %d", &n);
		char s[30];
		
		for(int i = 0; i < 2*n; i++){
			nAdj[i] = 0;
			cor[i] = 0;
			cs[i].ar = 0;
			cs[i].p = 0;
			cs[i].m = 0;
		}
		for(int i = 0; i < n; i++){
			scanf(" %s", s);
			for(int j = 0; j < n; j++){
				if(s[j] == '0'){
					continue;
				}
				int y = j+n;
				adj[i][nAdj[i]] = y;
				nAdj[i]++;
				adj[y][nAdj[y]] = i;
				nAdj[y]++;
			}
		}
		numCs = 0;
		for(int i = 0; i < 2*n; i++){
			if(cor[i] != 0){
				continue;
			}
			cor[i] = 1;
			dfs(i);
			cs[numCs].ar/=2;
			numCs++;
		}
		int res = 0;
		for(int i = 0; i < numCs; i++){
			if(cs[i].p == cs[i].m){
				res+= cs[i].p*cs[i].m-cs[i].ar;
				cs[i].ar = -1;
				cs[i].p = -1;
				cs[i].m = -1;
			}
		}
		sort(cs, cs+numCs, comp);
		for(int i = 0; i < numCs; i++){
			int dif = cs[i].m-cs[i].p;
			if(cs[i].ar < 0){
				continue;
			}
			int flag = 0;

			for(int j = numCs-1; j > i; j--){
				if(cs[j].ar < 0){
					continue;
				}
				if(cs[j].m-cs[j].p+dif==0){
					flag = 1;
					res+=(cs[i].m+cs[j].m)*(cs[i].m+cs[j].m)-cs[i].ar-cs[j].ar;
					cs[j].ar = -1;
					break;
				}
			}
			while(flag == 0){
				for(int j = numCs-1; j > i; j--){
					if(cs[j].ar < 0){
						continue;
					}
					if((cs[j].m-cs[j].p)*dif < 0){
						cs[i].m+=cs[j].m;
						cs[i].p+=cs[j].p;
						cs[i].ar+=cs[j].ar;
						dif = cs[i].m-cs[i].p;
						cs[j].ar = -1;
						break;
					}
				}
				for(int j = numCs-1; j > i; j--){
					if(cs[j].ar < 0){
						continue;
					}
					if(cs[j].m-cs[j].p+dif==0){
						flag = 1;
						res+=(cs[i].m+cs[j].m)*(cs[i].m+cs[j].m)-cs[i].ar-cs[j].ar;
						cs[j].ar = -1;
						break;
					}
				}
			}
			cs[i].ar = -1;
		}
		printf("Case #%d: %d\n", k, res);
	}
	return 0;
}
			
			