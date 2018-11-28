#include<cstdio>
#include<cstring>



int T, N;
int ans[3][1000000], R, P, S, cnt;
char sym[3] = {'P', 'R', 'S'};

void search(int now, int deep, int id) {
    if(deep == 0) {
        ans[cnt][id] = now;
        return;
    }
    search(now, deep - 1, id * 2);
    search((now + 1) % 3, deep - 1, id * 2 + 1);
    
}

bool check(int k) {
    int n[3];
    n[0] = n[1] = n[2] = 0;
    for(int i = 0; i < (1 << N); i++) {
        n[ans[k][i]]++;
    }
    if(n[0] == P && n[1] == R && n[2] == S) {
        return true;
    }
    return false;
}

bool compare(int n, int m, int left1, int right1, int left2, int right2) {
    for(int i = left1, j = left2; i < right1; i++, j++) {
        if(ans[n][i] > ans[m][j]) return true;
        if(ans[n][i] < ans[m][j]) return false;
    }
    return false;
}

void refine(int k) {
    for(int len = 2; len <= (1 << N); len *= 2) {
        for(int i = 0; i < (1 << N); i += len) {
            if(compare(k, k, i, i + len / 2, i + len / 2, i + len)) {
                int tmp;
                for(int j = i; j < i + len / 2; j++) {
                    tmp = ans[k][j];
                    ans[k][j] = ans[k][j + len / 2];
                    ans[k][j + len / 2] = tmp;
                }
            }
        }
    }
}

int main() {
    scanf("%d", &T);
    for(int cas = 1; cas <= T; cas++) {
        printf("Case #%d: ", cas);
        scanf("%d", &N);
        scanf("%d%d%d", &R, &P, &S);
        cnt = 0;
        for(int i = 0; i < 3; i++) {
            search(i, N, 0);
            if(check(cnt)){
                cnt++;
                refine(cnt - 1);
            }
        }
        int best = 0;
        for(int i = 0; i < cnt; i++) {
            if( compare(best, i, 0, (1 << N), 0, (1 << N)) ) {
                best = i;
            }
        }
        if(cnt == 0) {
            puts("IMPOSSIBLE");
        }
        else {
            for(int i = 0; i < (1 << N); i++) {
                printf("%c", sym[ans[best][i]]);
            }
            puts("");
        }
    }
    return 0;
}