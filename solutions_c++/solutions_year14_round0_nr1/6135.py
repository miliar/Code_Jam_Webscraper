#include<iostream>
#include<cstdio>
using namespace std;
int s[2][4][4];
int r[2];
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A.txt","w",stdout);
    int cas;cin>>cas;

    for(int q=1;q<=cas;q++)
    {
        int sol, cnt;
        cnt = 0;
        for(int i=0;i<2;i++)
        {
            cin>>r[i];r[i]--;
            for(int j=0;j<4;j++)
                for(int k=0;k<4;k++)
                {
                    cin>>s[i][j][k];
                }
        }

        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
            {
               // cout<<s[0][r[0]][i]<<' '<<s[1][r[1]][j]<<endl;
                if(s[0][r[0]][i] == s[1][r[1]][j] )
                {
                    cnt++;
                    sol = s[0][r[0]][i];
                }
            }
        cout<<"Case #"<<q<<": ";
        if(cnt == 0)cout<<"Volunteer cheated!"<<endl;
        else if(cnt==1)cout<<sol<<endl;
        else cout<<"Bad magician!"<<endl;

    }
    return 0;
}
