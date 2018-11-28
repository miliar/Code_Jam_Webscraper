#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    for(int p=1;p<=t;p++)
    {
        int f,s,first[6][6],second[6][6],cnt=0,ans=0,i,j;
        cin>>f;
        for(i=1;i<5;i++)
        {
            for(j=1;j<5;j++)
            {
                cin>>first[i][j];
            }
        }
        cin>>s;
        for(i=1;i<5;i++)
        {
            for(j=1;j<5;j++)
            {
                cin>>second[i][j];
            }
        }
        for(i=1;i<5;i++)
        {
            for(j=1;j<5;j++)
            {
                if(first[f][i]==second[s][j])
                {
                    cnt++;
                    ans=first[f][i];
                }
            }
        }
        if(!cnt)
            printf("Case #%d: Volunteer cheated!\n",p);
        else if(cnt==1)
        {
            printf("Case #%d: %d\n",p,ans);
        }
        else if(cnt>=2)
        {
            printf("Case #%d: Bad magician!\n",p);
        }
    }
    return 0;
}
