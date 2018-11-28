#include <cstdio>

using namespace std;

int T,len,total,sol;
char s[1024];

int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&T);
    for (int t=1; t<=T; t++) {
        scanf("%d",&len);
        scanf("%s",s);
        total=0;
        sol=0;
        for (int i=0; i<=len; i++) {
            if (total<i) {
                sol+=i-total;
                total=i;
            }
            total+=s[i]-'0';
        }
        printf("Case #%d: %d\n",t,sol);
    }

    return 0;
}
