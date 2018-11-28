#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
int cnt[17];
int main()
{
    freopen("A-small-attempt0 (1).in","r",stdin);
    freopen("op1.txt","w",stdout);
    int t;
    cin>>t;
    int q=0;
    while(t--)
    {
        q++;
        int f,s,i,j,ans=0,c=0;
        memset(cnt,0,sizeof(cnt));
        int a[4][4],b[4][4];
        cin>>f;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                cin>>a[i][j];
            }
        }
        for(i=0;i<4;i++)
            cnt[a[f-1][i]]++;

        cin>>s;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                cin>>b[i][j];
            }
        }
        for(i=0;i<4;i++)
            cnt[b[s-1][i]]++;
        for(i=1;i<=16;i++)
        {
            if(cnt[i]==2)
            {
                c++;
                ans=i;
            }
        }
        if(c<1)
            cout<<"Case #"<<q<<": Volunteer cheated!\n";
        else if(c==1)
            printf("Case #%d: %d\n",q,ans);
        else
            printf("Case #%d: Bad magician!\n",q);
    }
    return 0;
}
