#include<cstdio>
#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;
int a[20][20],b[20][20],c[20];
int hash[20];
int main()
{
    freopen("input-11.in","r",stdin);
    freopen("output-11.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int x=1;x<=t;x++)
    {
        memset(hash,0,sizeof(hash));
        int n1,n2,cnt=0,k=0;
        scanf("%d",&n1);
        for(int i=1;i<=4;i++)
                for(int j=1;j<=4;j++)
                                scanf("%d",&a[i][j]);
        for(int i=1;i<=4;i++)
        hash[a[n1][i]]=1;
        scanf("%d",&n2);
        for(int i=1;i<=4;i++)
                for(int j=1;j<=4;j++)
                                scanf("%d",&b[i][j]);
        for(int i=1;i<=4;i++)
        if(hash[b[n2][i]])
        c[k++]=b[n2][i];
        if(k==1)
        printf("Case #%d: %d\n",x,c[0]);
        else if(k==0)
        printf("Case #%d: Volunteer cheated!\n",x);
        else if(k>1)
        printf("Case #%d: Bad magician!\n",x);
    }
    return 0;
}
