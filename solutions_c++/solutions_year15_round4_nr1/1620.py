#include <cstdio>
#include <algorithm>
using std::min;
using std::max;

char s[200][200];
int R, C;
int countX[200];
int countY[200]; 
int minX[200], minY[200];
int maxY[200], maxX[200];

int chech_point(int i, int j){
    if(s[i][j] == '.') return 0;
    bool flag = true;
    for(int r=1;r<i;r++) if(s[r][j] != '.') flag = false;
    for(int r=i+1;r<=R;r++) if(s[r][j] != '.') flag = false;
    for(int c=1;c<j;c++) if(s[i][c] != '.') flag = false;
    for(int c=j+1;c<=C;c++) if(s[i][c] != '.') flag = false;
    if(flag) return -1;

    flag = false;
    if(s[i][j] == '>'){
        for(int k=j+1;k<=C;k++) {if(s[i][k] != '.') flag = true;}
        if(!flag) return 1;
    }
    if(s[i][j] == '<'){
        for(int k=1;k<j;k++) {if(s[i][k] != '.') flag = true;}
        if(!flag) return 1;
    }
    if(s[i][j] == '^'){
        for(int k=1;k<i;k++) {if(s[k][j] != '.') flag = true;}
        if(!flag) return 1;
    }
    if(s[i][j] == 'v'){
        for(int k=i+1;k<=R;k++) {if(s[k][j] != '.') flag = true;}
        if(!flag) return 1;
    }
    return 0;
}

int solve(){
    int res = 0;
    for(int i=1;i<=R;i++){
        for(int j=1;j<=C;j++){
            int tmp = chech_point(i, j);
            if(tmp==-1) return -1;
            res += tmp;
        }
    }
    return res;
}

int main(){
    int Tn;
    scanf("%d", &Tn);
    for(int T=1;T<=Tn;T++){
        scanf("%d %d", &R, &C);
        for(int i=1;i<=R;i++)
            scanf("%s", s[i]+1);
        int res = solve();
        printf("Case #%d: ", T);
        if(res==-1) puts("IMPOSSIBLE");
        else printf("%d\n", res);
    }
    return 0;
}