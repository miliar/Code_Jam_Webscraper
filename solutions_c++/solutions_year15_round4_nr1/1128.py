#include<cstdio>
#include<cstring>
#include<set>
#include<map>
#include<vector>
#include<algorithm>
#include<iostream>
#include<cmath>

using namespace std;

const int N = 110;

char a[N][N];
char v[10] = "^>v<";
int vx[4] = {-1, 0, 1, 0};
int vy[4] = {0, 1, 0, -1};

int check(int x, int y){
    if (a[x][y] == '.') return 0;
    int ans = -1;
    for (int i=0; i<4; ++i){
	bool has = false;
	for (int j=1; ; ++j){
	    int tx = x + j * vx[i];
	    int ty = y + j * vy[i];
	    if (a[tx][ty] == 0) break;
	    if (a[tx][ty] != '.'){
		has = true;
		break;
	    }
	}
	if (has){
	    if (v[i] == a[x][y]) return 0;
	    ans = 1;
	}
    }
    return ans;
}

int gao(){
    int h, w;
    cin >> h >> w;
    memset(a, 0, sizeof(a));
    for (int i=1; i<=h; ++i) scanf("%s", &a[i][1]);
    int ans = 0;
    for (int i=1; i<=h; ++i){
	for (int j=1; j<=w; ++j){
	    int t = check(i, j);
	    if (t == -1) return -1;
	    else ans += t;
	}
    }
    return ans;
}


int main(){
    int T;
    cin >> T;
    for (int i=1; i<=T; ++i){
	printf("Case #%d: ", i);
	int ans = gao();
	if (ans == -1){
	    puts("IMPOSSIBLE");
	}else{
	    printf("%d\n", ans);
	}
    }
    return 0;
}
