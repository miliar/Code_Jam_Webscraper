#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
const int maxn=5;
int a[8][8],b[8][8];
int main(){
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int T,r1,r2,cas=1;
    scanf("%d",&T);
    while(T--){
        scanf("%d",&r1);
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
                scanf("%d",&a[i][j]);
        scanf("%d",&r2);
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
                scanf("%d",&b[i][j]);
        int cnt=0,val;
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
                if(a[r1][i]==b[r2][j]) cnt++,val=a[r1][i];
        printf("Case #%d: ",cas++);
        if(cnt==1) printf("%d\n",val);
        else if(cnt==0) puts("Volunteer cheated!");
        else puts("Bad magician!");
    }
}
