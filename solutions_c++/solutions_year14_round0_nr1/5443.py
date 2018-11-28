#include <iostream>
#include <vector>
using namespace std;

int grid[4][4];
int main()
{
    int t,kase = 1;
    cin>>t;
    while(t--)
    {
        int r;
        cin>>r;
        --r;
        for(int i=0;i<4;++i)
            for(int j=0;j<4;++j)
                cin>>grid[i][j];
        vector<int> initials;
        for(int i=0;i<4;++i)
            initials.push_back(grid[r][i]);
        cin>>r;
        --r;
        for(int i=0;i<4;++i)
            for(int j=0;j<4;++j)
                cin>>grid[i][j];
        int cnt = 0,res;
        for(int i=0;i<4;++i)
            for(int j = 0;j<4;++j)
            {
                if(grid[r][j] == initials[i])
                {
                    res = grid[r][j];
                    ++cnt;
                }

            }
        cout<<"Case #"<<kase++<<": ";
        if(cnt == 0)
            cout<<"Volunteer cheated!"<<endl;
        else if(cnt == 1)
            cout<<res<<endl;
        else
            cout<<"Bad magician!"<<endl;
    }
}
