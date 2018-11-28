#include <stdio.h>
#include<algorithm>
using namespace std;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t,m,n,num=1;
    int s1[6][6],s2[6][6];
    int a[4],b[4];
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&m);
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
            scanf("%d",&s1[i][j]);
            int cnt1=0;
        for(int i=1;i<=4;i++)
        {
            a[cnt1++]=s1[m][i];
        }
        sort(a,a+4);
        scanf("%d",&n);
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
            scanf("%d",&s2[i][j]);
            int cnt2=0;
        for(int i=1;i<=4;i++)
        {
            b[cnt2++]=s2[n][i];
        }
        sort(b,b+4);
        int cnt=0,k;
        for(int i=0;i<=3;i++)
            for(int j=0;j<=3;j++)
            if(a[i]==b[j])
                {cnt++;k=a[i];}
        printf("Case #%d: ",num++);
        if(cnt==0) printf("Volunteer cheated!\n");
        else if(cnt==1) printf("%d\n",k);
        else printf("Bad magician!\n");
    }
}
