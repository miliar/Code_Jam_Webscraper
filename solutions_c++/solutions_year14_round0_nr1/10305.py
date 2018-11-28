#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int txt=1;
int main()
{
    freopen("data.in","r",stdin);
    freopen("data.out","w",stdout);
    int i,j;
    int n,_;
    int a,b;
    int num1[4][4],num2[4][4];
    scanf("%d",&_);
    while(_--){
        int cont=0,t;
        scanf("%d",&a);
        for(i=0;i<4;i++)
            for(j=0;j<4;j++) scanf("%d",&num1[i][j]);
        scanf("%d",&b);
        for(i=0;i<4;i++)
            for(j=0;j<4;j++) scanf("%d",&num2[i][j]);
        for(i=0;i<4;i++)
            for(j=0;j<4;j++) if(num1[a-1][i]==num2[b-1][j]){cont++;t=num1[a-1][i];}
        if(cont==1) printf("Case #%d: %d\n",txt++,t);
         else if(cont==0) printf("Case #%d: Volunteer cheated!\n",txt++);
          else printf("Case #%d: Bad magician!\n",txt++);
    }
    return 0;
}
