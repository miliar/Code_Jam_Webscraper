#include <stdio.h>
#include <stdlib.h>
#include <string>

int T;
char s[1000011];
int n;

int isC(int i){
    if (s[i] == 'a') return 0;
    if (s[i] == 'e') return 0;
    if (s[i] == 'i') return 0;
    if (s[i] == 'o') return 0;
    if (s[i] == 'u') return 0;
    return 1;
}

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&T);
    long long ans = 0; 
    int count = 0;
    long long j,m = 0;
    for (int ttt = 1 ;ttt <= T ; ttt++){
        scanf("%s",s);
        scanf("%d",&n);
        ans = 0;
        count = 0;
        m = 0;
        int l = strlen(s);
        for (int i = 0 ; i <l ; i++) {
            if (isC(i)) {
                count++;
                if (count >= n) {
                    j = i - n + 2;
                    ans += (j-m)*(l-i);
                    m = j;
                }
            } else {
                count = 0;
            }
        }
        printf("Case #%d: %lld\n",ttt,ans);
    }
}
