#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;

int s[50][50]={0};
int n,x,y,z;
double ans,gg;

void dfs(int a,int b,int c){
    if(a>=n){
        if(c >= y+1)
            ans++;
        gg++;
        return;
    }
    if(b < x+y)
        dfs(a+1,b+1,c);
    if(c < x+y)
        dfs(a+1,b,c+1);
}

int main(void){

    for(int i=0;i<25;i++)
        s[i][i]=s[i][0]=1;
    for(int i=2;i<25;i++)
        for(int j=1;j<i;j++)
            s[i][j] = s[i-1][j]+s[i-1][j-1];
    /*for(int i=0;i<21;i++,puts(""))
        for(int j=0;j<=i;j++)
            printf("%d ",s[i][j]);*/
    

    int t;
    scanf("%d",&t);
    for(int tt=1;tt<=t;tt++){
        scanf("%d%d%d",&n,&x,&y);
        x = abs(x);
        z = x+y;
        z = z/2+1;
        if(x == 0){
            if(n < z*(z*2-1))
                printf("Case #%d: 0.0\n", tt);
            else
                printf("Case #%d: 1.0\n", tt);
            continue;
        }
        if(n >= z*(z*2-1)){
            printf("Case #%d: 1.0\n", tt);
            continue;
        }
        
        int fix = (z-1)*((z-1)*2-1);
        n = n-fix;
        if(n < y+1){
            printf("Case #%d: 0.0\n", tt);
            continue;
        }
        
        ans = 0;gg=0;
        dfs(0,0,0);
        //fprintf(stderr,"%d: %.0lf %.0lf\n",tt,ans,gg);
        
        printf("Case #%d: %.8lf\n", tt, ans/gg);
    }
    return 0;
}

