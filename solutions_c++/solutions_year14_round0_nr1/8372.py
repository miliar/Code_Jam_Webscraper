#include <iostream>
#include <algorithm>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

int main()
{
    freopen("A-small-attempt2.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    for(int x=1;x<=t;x++)
    {
        int first,second;
        int magic[4][5];
        int hash1magic[4][17]={0},hash2magic[4][17]={0};
        cin>>first;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                cin>>magic[i][j];
                hash1magic[i][magic[i][j]]=1;

            }
        }
        cin>>second;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                cin>>magic[i][j];
                hash2magic[i][magic[i][j]]=1;
            }
        }
        int cnt=0,ans;
        for(int i=0;i<17;i++)
        {
            if(hash1magic[first-1][i]==1&&hash2magic[second-1][i]==1)
            {
                cnt++;
                ans=i;
            }
        }
        if(cnt==1)
                cout<<"Case #"<<x<<": "<<ans<<endl;
        else if(cnt>1)
                cout<<"Case #"<<x<<": Bad magician!"<<endl;
        else if(cnt==0)
                cout<<"Case #"<<x<<": Volunteer cheated!"<<endl;


    }

    return 0;
}
