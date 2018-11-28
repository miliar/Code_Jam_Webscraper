#include<iostream>
#include<vector>
#include<stdio.h>

using namespace std;

int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.txt", "w", stdout);

    int T, ans1, ans2, kase=0;
    cin>>T;
    int grid1[4][4], grid2[4][4], step1[4], step2[4];
    while(T--)
    {
        cin>>ans1;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
            {
                cin>>grid1[i][j];
                if(i==ans1-1)
                    step1[j]=grid1[i][j];
            }
        cin>>ans2;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
            {
                cin>>grid2[i][j];
                if(i==ans2-1)
                    step2[j]=grid2[i][j];
            }
        vector<int> v;
        v.clear();
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                if(step1[i]==step2[j])
                    v.push_back(step1[i]);
        cout<<"Case #"<<(++kase)<<": ";
        if(v.size()==1)
            cout<<v[0]<<endl;
        if(v.size()==0)
            cout<<"Volunteer cheated!"<<endl;
        if(v.size()>1)
            cout<<"Bad magician!"<<endl;








    }
}
