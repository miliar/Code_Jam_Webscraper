#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;

#define SI "GABRIEL"
#define NO "RICHARD"

int main()
{
    freopen("D-small-attempt2.in","r",stdin);
    freopen("D_result.out","w",stdout);
    int T,x,r,c;
    string t[5][5][5];

    t[1][1][1] = SI;
    t[1][1][2] = NO;
    t[1][1][3] = NO;
    t[1][1][4] = NO;

    t[2][1][1] = SI;
    t[2][1][2] = SI;
    t[2][1][3] = NO;
    t[2][1][4] = NO;

    t[3][1][1] = SI;
    t[3][1][2] = NO;
    t[3][1][3] = NO;
    t[3][1][4] = NO;

    t[4][1][1] = SI;
    t[4][1][2] = SI;
    t[4][1][3] = NO;
    t[4][1][4] = NO;

    t[2][2][1] = SI;
    t[2][2][2] = SI;
    t[2][2][3] = NO;
    t[2][2][4] = NO;

    t[3][2][1] = SI;
    t[3][2][2] = SI;
    t[3][2][3] = SI;
    t[3][2][4] = NO;

    t[4][2][1] = SI;
    t[4][2][2] = SI;
    t[4][2][3] = NO;
    t[4][2][4] = NO;

    t[3][3][1] = SI;
    t[3][3][2] = NO;
    t[3][3][3] = SI;
    t[3][3][4] = NO;

    t[4][3][1] = SI;
    t[4][3][2] = SI;
    t[4][3][3] = SI;
    t[4][3][4] = SI;

    t[4][4][1] = SI;
    t[4][4][2] = SI;
    t[4][4][3] = NO;
    t[4][4][4] = SI;

    cin>>T;
    for(int k=1; k<=T; k++)
    {
        cin>>x>>r>>c;
        if(c>r)
            swap(r,c);
        cout<<"Case #"<<k<<": "<<t[r][c][x]<<endl;
    }
    return 0;
}

