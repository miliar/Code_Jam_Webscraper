#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,k,n,a[5][5],i,j,ans,count,m,b[20],x;
    cin>>t;
    for(k=1;k<=t;k++)
    {
        count=0;
        for(i=1;i<=16;i++)
            b[i]=0;
        cin>>n;
        for(i=1;i<=4;i++)
        for(j=1;j<=4;j++)
        scanf("%d",&a[i][j]);
        for(j=1;j<=4;j++)
        {
            x=a[n][j];
            b[x]++;
        }
        scanf("%d",&m);
        for(i=1;i<=4;i++)
        for(j=1;j<=4;j++)
        scanf("%d",&a[i][j]);
        for(j=1;j<=4;j++)
        {
            x=a[m][j];
            b[x]++;
            if(b[x]==2)
            {
                //cout<<x<<endl;
                count++;
                ans=x;
            }
        }
        if(count==1)
            printf("Case #%d: %d\n",k,ans);
        else if(count>1)
            printf("Case #%d: Bad magician!\n",k);
        else if(count==0)
            printf("Case #%d: Volunteer cheated!\n",k);
    }
    return 0;
}
