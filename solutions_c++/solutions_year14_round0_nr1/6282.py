#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
int cnt[17];
int t;
int row;
int a;
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int cas = 1;
    cin>>t;
    while(t--)
    {
        memset(cnt,0,sizeof(cnt));
        cin>>row;
        for(int i=1;i<=4;++i)
            for(int j=1;j<=4;++j)
            {
                cin>>a;
                if(i==row)
                    cnt[a]++;
            }
        cin>>row;
        for(int i=1;i<=4;++i)
            for(int j=1;j<=4;++j)
            {
                cin>>a;
                if(i==row)
                    cnt[a]++;
            }
        int ans = 0;
        int ele = 0;
        for(int i=1;i<=16;++i)
        {
   //         cout<<i<<" "<<cnt[i]<<endl;
            if(cnt[i]==2)
            {
                ans++;
                ele=i;
            }
        }
        cout<<"Case #"<<cas++<<": ";
        if(ans==0)
        {
            cout<<"Volunteer cheated!"<<endl;
        }
        if(ans==1)
        {
            cout<<ele<<endl;
        }
        if(ans>1)
        {
            cout<<"Bad magician!"<<endl;
        }
    }
    return 0;
}
