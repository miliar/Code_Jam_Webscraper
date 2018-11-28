#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<algorithm>
const int mod = 1000000007;
char a[1000][102];
int p[8];
int n, k;
int x, y;
int cmps(const void*e1, const void*e2){
    return strcmp(((char*)e1), ((char*)e2));
}
int compref(char*s, char*t){
    int i;
    for(i = 0; s[i] && t[i] && s[i] == t[i];i++);
    return i;
}
int count(int j){
    char last[102];
    last[0] = 0;
    int cnt=1;
    for(int  i = 0;i <n;i++)
        if(p[i] == j){
            cnt+=strlen(a[i])-compref(last, a[i]);
            strcpy(last, a[i]);
        }
    return cnt;
}
void R(int i){
    if(i == n){
        int rx = 0;
        for(int j = 0; j < k; j++){
            int c = count(j);
            if(c==1)return;
            rx += c;
        }
        if(rx > x)
            x = rx, y=0;
        if(rx == x)
            y++;
        return;
    }
    for(int j=0;j<k;j++){
        p[i] = j;
        R(i+1);
    }
}
void solve(){
    int  i;
    scanf("%d%d\n", &n, &k);
    for(i = 0; i < n; i++)
        gets(a[i]);
    x = 0;y=0;
    qsort(a, n, 102, cmps);
    R(0);
    printf("%d %d\n", x, y);
}
int main(void){
#ifdef _DEBUG
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    int T;
    scanf("%d", &T);
    for(int i = 1; i <= T; i++){
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
