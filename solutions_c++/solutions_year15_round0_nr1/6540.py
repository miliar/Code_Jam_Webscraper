#include <stdio.h>
const int maxn = 1005;
char s[maxn];
int a[maxn];

int main()
{
    int T,n,ncase=0;
    scanf("%d",&T);
    while(T--) {
        scanf("%d%s",&n,s);
        int pre = 0, ans = 0;
        for(int i=0;i<=n;i++) {
            a[i] = s[i] - '0';
            if(i>pre)
            {
                ans+=i-pre;
                pre+=i-pre;
            }
            pre+=a[i];
        }
        printf("Case #%d: %d\n", ++ncase, ans);
    }

	return 0;
}
