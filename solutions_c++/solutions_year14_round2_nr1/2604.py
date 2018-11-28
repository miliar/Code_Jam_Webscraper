#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<algorithm>
int a[100][100];
int ak[100];
char as[128];
int am[100];
int getres(int *a, int n){
    int avg, i;
    int mres = 1000000;
    for(avg = 1; avg <= 100; avg++){
        int res = 0;
        for(i = 0; i < n;i++)
            res += abs(a[i] - avg);
        if(res < mres)
            mres = res;
    }
    return  mres;
}
int b[100];
void solve(){
    int n, i;
    char s[128],s2[128];
    scanf("%d",&n);
    memset(as, -1, sizeof(as));
    /*    scanf("%s%s", s,s2);
        s[std::unique(s, s+strlen(s)) - s]=0;
        s2[std::unique(s2, s2+strlen(s2)) - s2]=0;
        if(strcmp(s,s2))
            printf("Fegla Won\n");
        else printf("\n");*/
    for(i = 0; i < n; i++){
        scanf("%s", s);
        char c = s[0];
        ak[i] = 0;
        a[i][ak[i]] = 0;
        if(as[ak[i]] != -1 && as[ak[i]] != c){
            printf("Fegla Won\n");
            return;
        }
        as[ak[i]] = c;
        for(int j = 0; s[j];j++)
            if(c == s[j]){
                a[i][ak[i]]++;
            }
            else{
                c = s[j];
                 ak[i]++;
                 if(as[ak[i]] != -1 && as[ak[i]] != c){
                     printf("Fegla Won\n");
                     return;
                 }
                 as[ak[i]] = c;
                a[i][ak[i]] = 1;
            }
        ak[i]++;
        if(i && ak[i] != ak[i-1]){
            printf("Fegla Won\n");
            return;
        }
    }
    int k = ak[0];
    int res = 0;
    for(i = 0;i <k;i++){
        for(int j= 0;j<n;j++)
            b[j] = a[j][i];
        res += getres(b, n);
    }
    printf("%d\n", res);
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
