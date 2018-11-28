#include<cstdio>
#include<cstring>
using namespace std;
int n,m;
int a[5][5],b[5][5];
int used[20];
void read()
{
    int i,j;
    scanf("%d",&n);
    for(i=1;i<=4;i++)
        for(j=1;j<=4;j++)
        scanf("%d",&a[i][j]);
    scanf("%d",&m);
    for(i=1;i<=4;i++)
        for(j=1;j<=4;j++)
        scanf("%d",&b[i][j]);
    memset(used,0,sizeof(used));
}
void solve()
{
    int i,j,br=0,y;
    for(j=1;j<=4;j++)
    {
        used[a[n][j]]++;
        used[b[m][j]]++;
    }
    for(i=1;i<=16;i++)
    if(used[i]==2)
    {
        y=i;
        br++;
    }
    if(br>1)printf("Bad magician!");
    if(br==1)printf("%d",y);
    if(!br)printf("Volunteer cheated!");
}
int main()
{
    int i,t;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        read();
        printf("Case #%d: ",i);
        solve();
        printf("\n");
    }
}
