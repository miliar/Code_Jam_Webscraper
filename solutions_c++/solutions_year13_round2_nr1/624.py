#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;

int s[200],p[200][200];
int main(void){
    int t;
    scanf("%d",&t);
    for(int tt=1;tt<=t;tt++){
        int n,m;
        scanf("%d%d",&m,&n);
        for(int i=0;i<n;i++)
            scanf("%d",&s[i]);
        sort(s,s+n);
        memset(p,0,sizeof(p));
        p[0][0] = m;
        for(int i=0;i<n;i++)
            for(int j=0;j<n;j++){
                p[i][j+1] = max(p[i][j+1], p[i][j]*2-1);
                if(p[i][j] > s[i])
                    p[i+1][j] = max(p[i+1][j], p[i][j]+s[i]);
                
            }

        int ans = n;
        for(int i=n-1;i>=0;i--)
            for(int j=n-1;j>=0;j--)
                if(s[i] < p[i][j])
                    ans = min(ans, j+(n-1-i));
        
        printf("Case #%d: %d\n", tt, ans);
        /*
        for(int i=0;i<n;i++,puts(""))
            for(int j=0;j<n;j++)
                printf("%d ",p[i][j]);
        */
    }
    return 0;
}

