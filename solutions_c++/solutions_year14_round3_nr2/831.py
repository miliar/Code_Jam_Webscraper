#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std;

#define ms(a,b) memset(a,b,sizeof(a))

const int MOD = 1000000007;

char str[110][110];
int ord[10];
int N;

bool check(void);

int main(){
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("out", "w", stdout);
    int T, cnt = 0;
    scanf("%d", &T);
    while(T--){
        scanf("%d", &N);
        for(int i = 0; i < N; i++) ord[i] = i;
        for(int i = 0; i < N; i++){
            scanf("%s", str[i]);
        }
        int ans = 0;
        while(1){
/*            for(int i = 0; i < N; i++) printf("%d ", ord[i]);
            printf("\n");*/
            if(check()) ans++;
            if(!next_permutation(ord, ord+N)) break;
        }
        printf("Case #%d: %d\n", ++cnt, ans);
    }
    return 0;
}

bool check(void){
    bool appear[30];
    ms(appear, false);
/*    for(int i = 0; i < N; i++){
        printf("%s", str[ord[i]]);
    }
    printf("\n");*/
    for(int i = 0; i < N; i++){
        int preLen;
        if(i) preLen = strlen(str[ord[i-1]]);
        int len = strlen(str[ord[i]]);
        for(int j = 0; j < len; j++){
            if(appear[str[ord[i]][j]-'a']){
                char pre;
                if(j) pre = str[ord[i]][j-1];
                else pre = str[ord[i-1]][preLen-1];
                if(str[ord[i]][j] != pre)
                    return false;
            }
            else appear[str[ord[i]][j]-'a'] = true;
        }
    }
    return true;
}
