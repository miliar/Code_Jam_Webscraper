#include<iostream>
#include<vector>
#include<cstdio>
using namespace std;
int main()
{
    long long t;
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    cin>>t;
    for(int i=0;i<t;i++)
    {
        int ans1,ans2,p,k;
        vector<int> a,b;
        cin>>ans1;
        for(int j=0;j<4;j++)
            for(int o=0;o<4;o++)
            {
                cin>>p;
                if(j==ans1-1)a.push_back(p);
            }
        cin>>ans2;
        int cnt=0,card;
        for(int j=0;j<4;j++)
            for(int o=0;o<4;o++)
            {
                cin>>p;
                if(j==ans2-1)
                    for(int t=0;t<4;t++)
                        {
                            if(a[t]==p){cnt++;card=a[t];break;}
                        }
            }
        if(cnt==0)cout<<"Case #"<<i+1<<": "<<"Volunteer cheated!"<<endl;
        else if(cnt==1)cout<<"Case #"<<i+1<<": "<<card<<endl;
        else cout<<"Case #"<<i+1<<": "<<"Bad magician!"<<endl;
    }
    return 0;
}
