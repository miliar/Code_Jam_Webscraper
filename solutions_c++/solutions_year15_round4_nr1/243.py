//Fruit of Light
//FoL CC
//Apple Strawberry

#include<cstdio>
#include<algorithm>
#include<vector>
#include<iostream>
#include<set>
#include<map>
#include<queue>
#include<cmath>
#include<cstring>

using namespace std;

#define For(i, n) for(int i = 0; i<(n); ++i)
#define INF 1023456789
#define eps 1e-9

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

int r,s;
string M[147];
int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};
char dc[] = "^v<>";

int extra(){
    scanf("%d%d", &r, &s);
    For(i, r) cin >> M[i];
    int changes = 0;
    For(i, r) For(j, s) {
        if (M[i][j]=='.') continue;
        int lc = -1;
        For(d, 4) if (dc[d]==M[i][j]) {
            int x = i;
            int y = j;
            while(true){
                x+=dx[d];
                y+=dy[d];
                if (x<0 || x>=r || y<0 || y>=s) break;
                if (M[x][y] != '.') { lc = 0; break; }
            }
        }
        if (lc == 0) continue;
        For(d, 4) if (dc[d]!=M[i][j]) {
            int x = i;
            int y = j;
            while(true){
                x+=dx[d];
                y+=dy[d];
                if (x<0 || x>=r || y<0 || y>=s) break;
                if (M[x][y] != '.') { lc = 1; break; }
            }
            if (lc>=0) break;
        }
        if (lc>=0) changes++;
        else {
            printf("IMPOSSIBLE\n");
            return 0;
        }
    }
    printf("%d\n", changes);
}

int main(){
    int T;
    scanf("%d",&T);
    For(i,T){
        printf("Case #%d: ",i+1);
        extra();
    }
}
