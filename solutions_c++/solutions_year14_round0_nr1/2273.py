#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<vector>
using namespace std;
int main()
{
    int T;
    freopen("A-small-attempt1.in","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>T;
    for(int tt=1;tt<=T;tt++)
    {


        int map[5][5];
        int ans1;
        cin>>ans1;
        vector<int>res1;
        vector<int>res2;
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                cin>>map[i][j];
                if(i==ans1)
                {
                    res1.push_back(map[i][j]);
                }
            }
        }
        int ans2;
        cin>>ans2;
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                cin>>map[i][j];
                if(i==ans2)
                {
                    res2.push_back(map[i][j]);
                }
            }
        }
        int cnt=0;
        int mark=0;
        /*
        for(int i=0;i<4;i++)
        {
            cout<<res1[i]<<" ";
        }
        cout<<endl;
        for(int i=0;i<4;i++)
        {
            cout<<res2[i]<<" ";
        }
        cout<<endl;
        */
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                if(res1[i]==res2[j])
                {
                    cnt++;
                    mark=res1[i];
                }
            }
        }
        cout<<"Case #"<<tt<<": ";
        if(cnt==1)
        {
            cout<<mark<<endl;
        }
        else if(cnt>1)
        {
            cout<<"Bad magician!"<<endl;
        }
        else
        {
            cout<<"Volunteer cheated!"<<endl;
        }
    }
    return 0;
}
