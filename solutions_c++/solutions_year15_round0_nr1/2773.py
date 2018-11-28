/** CyCraig - Google Code Jam 2015 Qualification Problem A**/
#include <cstdio>
#include <cstring>

//int p[1005];

int main(void) {
    freopen("in.in", "r", stdin);
    freopen("out", "w", stdout);
    
    int n,c=0, invite, standing, m, curr;
    char ch;
    scanf("%d\n",&n);
    while(n--) {
        //memset(&p,0,sizeof(p));
        invite = standing = 0;
        scanf("%d ",&m);
        for(int i = 0; i <= m; i++) {
            scanf("%c",&ch);
            curr = ch-'0';
            //printf("i=%d standing=%d curr=%d\n",i,standing,curr);
            //if(curr == 0) invite++;
            if(standing < i && curr!=0) {
                invite += i-standing;
                standing += invite;
            }
            standing += curr;
        }
        printf("Case #%d: %d\n",++c,invite);
    }
    fflush(stdout);
    
    
    return 0;
}