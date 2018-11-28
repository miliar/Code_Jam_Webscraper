#include<cstdio>

char dir[4] = {'^', '>', 'v', '<'};
char mmap[110][110];
int R, C;
int ans;
bool possible, empty;

bool goDir(int stR, int stC, char d){
    int chR = 0, chC = 0;
    if(d == '^') chR = -1, chC = 0;
    else if(d == '<') chR = 0, chC = -1;
    else if(d == '>') chR = 0, chC = 1;
    else if(d == 'v') chR = 1, chC = 0;
    int currR = stR+chR, currC = stC+chC;
    while(currR < R && currC < C && currR >= 0 && currC >= 0){
        if(mmap[currR][currC] != '.') return true;
        currR += chR;
        currC += chC;
    }
    return false;
}

void check(int r, int c){
    if(mmap[r][c] != '.'){
        empty = false;
        bool ok = goDir(r, c, mmap[r][c]);
        if(ok) return;
        ans++;
        for(int j = 0; j < 4 && !ok; j++){
            ok |= goDir(r, c, dir[j]);
            mmap[r][c] = dir[j];
        }
        if(!ok) possible = false;
    }
}

int main(){
    int T, cnt = 0;
    scanf("%d", &T);
    while(T--){
        scanf("%d%d", &R, &C);
        for(int i = 0; i < R; i++){
            scanf("%s", mmap[i]);
        }
        possible = true;
        ans = 0;
        empty = true;
        int st=0, red=R, ced=C;
        while(st < red && st < ced && possible){
            for(int i = st; i < red && possible; i++){
                check(i, st);
                check(i, ced-1);
            }
            for(int i = st; i < ced && possible; i++){
                check(st, i);
                check(red-1, i);
            }
//            R -= 2, C -= 2;
            st++, red--, ced--;
        }
        printf("Case #%d: ", ++cnt);
        if(possible) printf("%d\n", ans);
        else printf("IMPOSSIBLE\n");
    }
    return 0;
}
