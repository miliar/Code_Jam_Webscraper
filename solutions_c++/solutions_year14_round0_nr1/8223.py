#include <cstdio>
#include <cstring>

int a[22], b[22], vis[22];

int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("oo.out", "w", stdout);
    int t, r1, r2, cas = 1;
    scanf("%d", &t);
    while(t--){
        scanf("%d", &r1);
        for(int i = 0;i < 16; i++)  scanf("%d", &a[i]);
        scanf("%d", &r2);
        r1--; r2--;
        for(int i = 0;i < 16; i++)  scanf("%d", &b[i]);
        memset(vis, 0, sizeof(vis));
        for(int i = r1*4;i < (r1+1)*4; i++) vis[a[i]]++;
        for(int i = r2*4;i < (r2+1)*4; i++) vis[b[i]]++;
        int cnt = 0, id;
        for(int i = 1;i <= 16; i++) if(vis[i] > 1)
            cnt++, id = i;
        printf("Case #%d: ", cas++);
        if(cnt == 1)    printf("%d\n", id);
        else if(cnt == 0)   puts("Volunteer cheated!");
        else    puts("Bad magician!");
    }
    return 0;
}
