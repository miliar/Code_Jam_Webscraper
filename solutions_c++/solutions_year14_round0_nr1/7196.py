#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    freopen("A-small-attempt0.in", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    int t,k=0;
    cin>>t;
    while(k++<t)
    {
        int r1,r2,a1[4][4],a2[4][4];
        cin>>r1;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                cin>>a1[i][j];
        cin>>r2;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                cin>>a2[i][j];
        cout<<"Case #"<<k<<": ";
        int flag=0,ans;
        r1--;r2--;
        for(int i=0;i<4;i++)
        {
            if(a2[r2][i]==a1[r1][0]||a2[r2][i]==a1[r1][1]||a2[r2][i]==a1[r1][2]||a2[r2][i]==a1[r1][3])
                {flag++;ans=a2[r2][i];}
        }
        if(flag==0)
            cout<<"Volunteer cheated!"<<endl;
        else if(flag==1)
            cout<<ans<<endl;
        else cout<<"Bad magician!"<<endl;
    }
    return 0;
}
