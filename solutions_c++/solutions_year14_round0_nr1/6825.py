#include<bits/stdc++.h>
using namespace std;
typedef long long int i64;
int main()
{
    //freopen("A-small-attempt0.in","r",stdin);
    //freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cs = 1;cs<=t;cs++)
    {
        int n,num;
        int a[17]={0};
        scanf("%d",&n);
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                scanf("%d",&num);
                if(i==n-1)a[num]++;
            }
        }
        int cnt=0;
        int ans=0;
        scanf("%d",&n);
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                scanf("%d",&num);
                if(i==n-1)
                {
                    a[num]++;
                    if(a[num]==2)
                    {
                        cnt++;
                        ans = num;
                    }
                }
            }
        }
        printf("Case #%d: ",cs);
        if(cnt==1)printf("%d\n",ans);
        else if(cnt==0)printf("Volunteer cheated!\n");
        else printf("Bad magician!\n");
    }
	return 0;
}
