#include <iostream>
using namespace std;

int main()
{
    struct array
    {
        int c[5][5];
    };

    int t;
    cin>>t;

    array arr1[t+1],arr2[t+1];
    int a1[t+1],a2[t+1],cnt[t+1],ans[t+1];

    for(int i=1;i<=t;i++)
    {
        cin>>a1[i];

        for(int j=1;j<=4;j++)
        {
            for(int k=1;k<=4;k++)
            {
                cin>>arr1[i].c[j][k];
            }
        }

        cin>>a2[i];

        for(int j=1;j<=4;j++)
        {
            for(int k=1;k<=4;k++)
            {
                cin>>arr2[i].c[j][k];
            }
        }
    }

    for(int i=1;i<=t;i++)
    {
        cnt[i]=0;

        for(int j=1;j<=4;j++)
        {
            for(int k=1;k<=4;k++)
            {
                if(arr1[i].c[a1[i]][j]==arr2[i].c[a2[i]][k])
                {
                    cnt[i]++;
                    ans[i]=arr2[i].c[a2[i]][k];
                }
            }
        }
        cout<<"Case "<<"#"<<i<<": ";
        if(cnt[i]==0)
        {
            cout<<"Volunteer cheated!";
        }
        else if (cnt[i]==1)
        {
            cout<<ans[i];
        }
        else
        {
            cout<<"Bad magician!";
        }
        cout<<endl;
    }

    return 0;
}
