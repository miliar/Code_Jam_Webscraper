#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<functional>
#include<algorithm>
#include<limits>
#include<utility>
#define PB push_back
#define MP make_pair
#define _F first
#define _S second
#define PP system("PAUSE");

using namespace std;

int N, M;
int mat[200][200];

bool check(int x, int y){
    int cnt = 0;
    int tmp = mat[x][y];
    for(int i = 0; i < N; i++)
        if(tmp < mat[i][y]){
            cnt = 1;
            break;
        }
    if(cnt == 0) return true;
    cnt = 0;
    for(int i = 0; i < M; i++)
        if(tmp < mat[x][i]){
            cnt = 1;
            break;
        }
    if(cnt == 0) return true;
    return false;
}

void solve(void){
    scanf("%d%d", &N, &M);
    for(int i = 0; i < N; i++)
        for(int j = 0; j < M; j++)
            scanf("%d", &mat[i][j]);
    bool flag = true;
    for(int i = 0; i<N && flag; i++)
        for(int j = 0; j<M && flag; j++)
            flag = check(i, j);
    if(flag) puts("YES");
    else puts("NO");
    return;
}

int main(void){
    int T;
    scanf("%d", &T);
    for(int i = 1; i <= T; i++){
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
    }
