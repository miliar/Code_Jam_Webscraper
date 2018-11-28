#include<stdio.h>
#include<string.h>
#include<math.h>
#include<vector>
#include<queue>
#include<algorithm>
using namespace std;

int t,x,m,n;

int main()
{
#ifdef Haha
    freopen("D-small-attempt0.in","r",stdin);
    freopen("D-small-attempt0.out","w",stdout);
#endif // Haha
    scanf("%d",&t);
    for(int cas=1;cas<=t;cas++){
        scanf("%d%d%d",&x,&n,&m);
        printf("Case #%d: ",cas);
        if(x==1) printf("GABRIEL\n");
        else if(x==2)
        {
            if(n%2==0||m%2==0) printf("GABRIEL\n");
            else printf("RICHARD\n");
        }
        else if(x==3){
            if(n==2&&m==3) printf("GABRIEL\n");
            else if(n==3&&m==3) printf("GABRIEL\n");
            else if(n==3&&m==2) printf("GABRIEL\n");
            else if(n==4&&m==3) printf("GABRIEL\n");
            else if(n==3&&m==4) printf("GABRIEL\n");
            else printf("RICHARD\n");
        }
        else{
            if(n==3&&m==4) printf("GABRIEL\n");
            else if(n==4&&m==4) printf("GABRIEL\n");
            else if(n==4&&m==3) printf("GABRIEL\n");
            else printf("RICHARD\n");
        }
    }
    return 0;
}
