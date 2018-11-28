#include <bits/stdc++.h>

using namespace std;

int main()
{
        freopen("A-small-attempt0.in","r",stdin);
        freopen("out.txt","w",stdout);
        int t,cas=0;
        cin>>t;
        while(t--){
                int a[4][4], b[4][4];
                int ans1, ans2;
                cin>>ans1;
                for(int i=0;i<4;++i)
                        for(int j=0;j<4;++j)
                                cin>>a[i][j];
                cin>>ans2;
                for(int i=0;i<4;++i)
                        for(int j=0;j<4;++j)
                                cin>>b[i][j];
                int hash[17]={0},flag=0,val;

                for(int j=0;j<4;++j){
                        hash[a[ans1-1][j]]++;hash[b[ans2-1][j]]++;
                }


                for(int i=0;i<17;++i)
                {
                        //cout<<i<<" : "<<hash[i]<<endl;
                        if(hash[i]==2&&!flag)
                                flag=1,val=i;
                        else if(hash[i]==2)
                                flag=2;
                }

                cout<<"Case #"<<++cas<<": ";
                if(!flag)
                         cout<<"Volunteer cheated!"<<endl;
                else if(flag==1)
                        cout<<val<<endl;
                else if(flag==2)
                        cout<<"Bad magician!"<<endl;
        }
}

