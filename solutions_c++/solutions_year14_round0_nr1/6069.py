#include <iostream>
#include <cstdio>
using namespace std;
int a[5][5], b[5][5], n, m, ans;
int judge()
{
    int res=0;
    for (int i=1; i<=4; i++)
    {
        for (int j=1; j<=4; j++)
            if (a[n][i] == b[m][j])
            {
                ans = a[n][i];
                res++;
            }

    }
    if (res==1) return 1;
    else if (res>1) return 2;
    else return 3;
}
int main()
{
    int t, x=1;
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("out.out", "w", stdout);
    cin>>t;

    while (t--)
    {
        cin>>n;
        for (int i=1; i<=4; i++)
        for (int j=1; j<=4; j++)
            cin>>a[i][j];
        cin>>m;
        for (int i=1; i<=4; i++)
        for (int j=1; j<=4; j++)
            cin>>b[i][j];
        int a = judge();
        cout<<"Case #"<<x++<<": ";
        if (a==1) cout<<ans<<endl;
        else if (a==2) cout<<"Bad magician!"<<endl;
        else if (a==3) cout<<"Volunteer cheated!"<<endl;
    }
    return 0;
}
