#include<cstdio>
#include<vector>
#include<algorithm>
#include<cmath>
#include<cstring>
using namespace std;

int p1[5],p2[5];
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int t,ti=1;scanf("%d",&t);
    while(t--)
    {
        printf("Case #%d: ",ti++);
        int a,b;
        scanf("%d",&a);
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
                if(i!=a-1)scanf("%*d");
                else scanf("%d",p1+j);
        }
        scanf("%d",&b);
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
                if(i!=b-1)scanf("%*d");
                else scanf("%d",p2+j);
        }
        int cnt=0,fin;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                if(p1[j]==p2[i])cnt++,fin=p1[j];
        if(cnt==0)puts("Volunteer cheated!");
        else if(cnt==1)printf("%d\n",fin);
        else puts("Bad magician!");
    }
    return 0;
}
