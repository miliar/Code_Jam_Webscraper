#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int ans[20];
int grid[4][4];
int main()
{
    int T;cin>>T;
    for (int cases = 0; cases < T; ++cases)
    {
        int a1,a2;
        int sum=0;
        int card=0;
        memset(ans,0,sizeof(ans));
        cin>>a1;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                cin>>grid[i][j];
        for(int i=0;i<4;i++)    ans[grid[a1-1][i]]=1;
        cin>>a2;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                cin>>grid[i][j];
        for (int i = 0; i < 4; ++i)
        {
            if(ans[grid[a2-1][i]]) 
            {
                sum++;
                card=grid[a2-1][i];
            }  
        }
        printf("Case #%d: ",cases+1);
        if(sum==1) cout<<card<<endl;
        else if(sum>1) cout<<"Bad magician!"<<endl;
        else cout<<"Volunteer cheated!"<<endl;
    }
    return 0;
}