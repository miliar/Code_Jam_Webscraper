#include<cstdio>

int s[1001];

int main() {
    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.txt", "w", stdout);
    int t, smax, round = 0;
    scanf("%d", &t);
    while(t--) {
        int c = 0, cnow = 0;
        scanf("%d", &smax);
        for(int i=0; i<=smax; i++) {
            scanf("%1d", &s[i]);
            if(i>cnow && s[i]!=0) {
                c += (i-cnow);
                cnow += (i-cnow);
            }
            cnow += s[i];
        }
        printf("Case #%d: %d\n", ++round, c);
    }
    return 0;
}
