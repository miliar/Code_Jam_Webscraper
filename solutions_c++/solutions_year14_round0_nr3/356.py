#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <stack>
#include <cstring>
#include <map>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
unsigned long long one = 1;

int t,r,c,m,x;
ii df;
int ans;
bool fs;
int memo[55][55][2525];
ii par[55][55][2525];
vector<int> tr;

int dp(int pos, int num, int mine){
	if (pos == r-1){
		if (mine == 0){
			if (fs){
				fs = false;
				ii p = par[pos][num][mine];
				int prev = 0;
				int id = pos-1;
				tr.push_back(p.second/2);
				tr.push_back(p.second/2);
				prev = p.second;
				p = par[id][p.first][p.second];
				while (p != df){
					tr.push_back(p.second-prev);
					prev = p.second;
					id--;
					p = par[id][p.first][p.second];
				}
			}
			return 1;
		}
		return 0;
	}
	if (memo[pos][num][mine] >= 0) return memo[pos][num][mine];
	int q = 0;
	if (pos == r-2){
		if (mine%2 == 1) return 0;
		for (int i=0; i<=num; i++){
			if (mine-(2*i) < 0) break;
			if (i == c-1) continue;
			par[pos+1][i][mine-(2*i)] = ii(num,mine);
			q = max(q, dp(pos+1,i,mine-(2*i)));
		}
	} else {
		for (int i=0; i<=num; i++){
			if (mine-i < 0) break;
			if (i == c-1) continue;
			par[pos+1][i][mine-i] = ii(num,mine);
			q = max(q, dp(pos+1,i,mine-i));
		}
	}
	return memo[pos][num][mine] = q;
}

int main(){
	scanf("%d",&t);
	for (int jj=1; jj<=t; jj++){
		scanf("%d%d%d",&r,&c,&m);
		printf("Case #%d:\n",jj);
		if (m == 0 || m == r*c-1){
			for (int i=0; i<r; i++){
				for (int j=0; j<c; j++){
					if (i==0 && j==0) printf("c");
					else if (m == 0) printf(".");
					else printf("*");
				}
				printf("\n");
			}
		} else if (r == 1 || c == 1){
			for (int i=0; i<m; i++){
				printf("*");
				if (c == 1) printf("\n");
			}
			for (int i=m; i<r*c-1; i++){
				printf(".");
				if (c == 1) printf("\n");
			}
			printf("c\n");
		} else {
			fs = true;
			tr.clear();
			memset(memo, -1, sizeof memo);
			df = ii(-1,-1);
			for (int i=0; i<55; i++){
				for (int j=0; j<55; j++){
					for (int k=0; k<2525; k++){
						par[i][j][k] = df;
					}
				}
			}
			ans = dp(0,c,m);
			if (ans == 0) printf("Impossible\n");
			else {
				for (int i=0; i<r; i++){
					for (int j=0; j<c; j++){
						if (i==0 && j==c-1) printf("c");
						else if (j < tr[i]) printf("*");
						else printf(".");
					}
					printf("\n");
				}
			}
		}
	}
	return 0;
}
