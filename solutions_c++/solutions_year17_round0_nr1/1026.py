#include<cstdio>
#include<cstring>
#include<algorithm>

char str[1004];
int k;

int solve(){
    int len = strlen(str), cnt = 0;
    for (int i=0;i<len-(k-1);i++){
        if (str[i] == '-'){
            for (int j=0;j<k;j++)
                str[i+j] = str[i+j]=='-'? '+': '-';
            cnt ++;
        }
    }
    if ( std::all_of(str+len-(k-1), str+len, [](char c){return c!='-';}) )
        return cnt;
    else return -1;
}

int main (){
    int T;
    scanf("%d", &T);
    for (int i=1;i<=T;i++){
        scanf("%s%d", str, &k);
        int sol = solve();
        printf("Case #%d: ", i);
        if (sol < 0) printf("IMPOSSIBLE\n");
        else printf("%d\n", sol);
    }
}
