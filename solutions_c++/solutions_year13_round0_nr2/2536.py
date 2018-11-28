#include <vector>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;

const int MAXN = 110;
const int MAXM = 110;

int mat[MAXN][MAXM];
int h[MAXN][MAXM];
struct Edge{
    int x;
    int y;
    int h;
    bool operator<(const Edge &e)const{
	return h > e.h;
    }
};

int n, m;
bool check(int a, int b){
    bool ans = true;
    for(int i = 0; i < m; i++)
	if(mat[a][b] < mat[a][i])
	    ans = false;

    if(ans) return true;

    ans = true;
    for(int i = 0; i < n; i++)
	if(mat[a][b] < mat[i][b])
	    ans = false;

    return ans;
}

int main(){
    int t;
    scanf("%d", &t);
    for(int cas = 1; cas <= t; cas++){
	vector<Edge> ve;
	scanf("%d%d", &n, &m);

	bool can = true;	
	for(int i = 0; i < n; i++)
	    for(int j = 0; j < m; j++){
		scanf("%d", &mat[i][j]);
	    }

	int now = 0;
	for(int i = 0; i < n && can; i++)
	    for(int j = 0; j < m && can; j++){
		if(!check(i, j)){
		    can = false;
		}
		now++;
	    }
		
	if(can) printf("Case #%d: YES\n", cas);
	else printf("Case #%d: NO\n", cas);
    }
    return 0;
}
