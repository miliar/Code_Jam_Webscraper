
#include<stdio.h>
#include<iostream>
using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
    int t,kas=0;
    cin>>t;
    while(t--)
    {
        int a,b;
        int f[10][10];
        int l[10][10];

        cin>>a;

        for(int i=1; i<=4; i++)
        for(int j=1; j<=4; j++)
        cin>>f[i][j];

        cin>>b;

        for(int i=1; i<=4; i++)
        for(int j=1; j<=4; j++)
        cin>>l[i][j];

        int res = 0;
        int cnt = 0;
        for(int i=1; i<=4; i++)
        for(int j=1; j<=4; j++)
        {
            if(f[a][i] == l[b][j])
            {
                cnt++;
                res = f[a][i];
            }
        }
        if(cnt == 0)
            cout<<"Case #"<<++kas<<":"<<" Volunteer cheated!"<<endl;
        else if(cnt==1)
            cout<<"Case #"<<++kas<<": "<<res<<endl;
        else cout<<"Case #"<<++kas<<":"<<" Bad magician!"<<endl;
    }
    return 0;
}
