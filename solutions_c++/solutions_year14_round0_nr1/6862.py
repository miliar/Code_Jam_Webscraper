#include <bits/stdc++.h>

using namespace std;

main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);
    int T;
    cin>>T;
    for(int z=0;z<T;z++)
    {
        int pos[4],can=0,ans=0,t,f;
        cin>>f;
        cout<<"Case #"<<z+1<<": ";
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
            {
                cin>>t;
                if(i+1==f)
                    pos[j]=t;
            }
        cin>>f;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
            {
                cin>>t;
                if(i+1==f)
                    for(int k=0;k<4;k++)
                        if(pos[k]==t)
                            can++,ans=t;
            }
        if(!can)
            cout<<"Volunteer cheated!\n";
        else if(can==1)
            cout<<ans<<"\n";
        else
            cout<<"Bad magician!\n";

    }
}
