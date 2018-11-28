#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
using namespace std;

bool vis[20];

int main()
{
    freopen("D:\\a.in","r", stdin);
    freopen("D:\\b.txt","w", stdout);


    int q;
    cin>>q;

    for(int t=1;t<=q;t++)
    {
        memset(vis,0,sizeof(vis));

        int type = 0;
        int ans = 0;
        int num = 0;
        int row1,row2;

        cin>>row1;

        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
            {
                cin>>num;
                if(i == row1)
                {
                    vis[num]=1;
                }
            }

        cin>>row2;

        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
        {
            cin>>num;
            if(i==row2)
            {
                if(vis[num] == 1)
                {
                    type++;
                    ans = num;
                }
            }
        }

        cout<<"Case #"<<t<<": ";
        if(type == 0) cout<<"Volunteer cheated!"<<endl;
        else if(type ==1) cout<<ans<<endl;
        else cout<<"Bad magician!"<<endl;

    }

}
