#include<bits/stdc++.h>

using namespace std;

int main()
{
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("out", "w", stdout);
    int ma[4][4]={{1,2,3,4},{5,6,7,8},{9,10,11,12},{13,14,15,16}};
    int ans[16][4]={{1,0,0,0},{1,1,0,0},{1,0,0,0},{1,1,0,0},{1,1,0,0},{1,1,0,0},{1,1,1,0},{1,1,0,0},{1,0,0,0},{1,1,1,0},{1,0,1,0},{1,1,1,1},{1,1,0,0},{1,1,0,0},{1,1,1,1},{1,1,0,1}};
    int x,r,c,ans1,t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
    cin>>x>>r>>c;
    //cout<<ma[r-1][c-1];
    ans1=ans[ma[r-1][c-1]-1][x-1];
    if(ans1==1)
    {
        cout<<"Case #"<<i+1<<": "<<"GABRIEL\n";
    }
    else
        {
            cout<<"Case #"<<i+1<<": "<<"RICHARD\n";
        }
    }
    return 0;
}
