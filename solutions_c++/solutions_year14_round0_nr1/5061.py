#include<iostream>
#include<map>
#include<algorithm>
#include<cstdio>
#include<cstring>
using namespace std;
int main()
{
    int test=1,t;
    int i,j,row1,row2,ans,grid1[5][5],grid2[5][5],cnt;
    int hash1[17],hash2[17];
    cin>>t;
    while(test<=t)
    {
        cnt=0;
        memset(hash1,0,sizeof(hash1));
        memset(hash2,0,sizeof(hash2));
        cin>>row1;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                cin>>grid1[i][j];
            }
        }
        cin>>row2;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                cin>>grid2[i][j];
            }
        }
        for(i=1;i<=4;i++)
            hash1[grid1[row1][i]]=1;
        for(i=1;i<=4;i++)
            hash2[grid2[row2][i]]=1;
        for(i=1;i<=16;i++)
        {
            if(hash1[i]==hash2[i] && hash1[i]==1)
            {
                cnt++;
                ans=i;
            }

        }
        if(cnt==1)
        {
            cout<<"Case #"<<test<<":"<<" "<<ans<<endl;
        }
        else if(cnt>1)
        {
            cout<<"Case #"<<test<<":"<<" "<<"Bad magician!"<<endl;
        }
        else
        {
             cout<<"Case #"<<test<<":"<<" "<<"Volunteer cheated!"<<endl;
        }
        test++;
    }
}
