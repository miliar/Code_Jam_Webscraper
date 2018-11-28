#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;

bool ok(int q[][100], int n, int m, int a, int b)
{
    int i;
    bool r=0,c=0;
    for (i=0;i<n;i++)
        if (q[i][b]>q[a][b]) {r=1;break;}

    for (i=0;i<m;i++)
        if (q[a][i]>q[a][b]) {c=1;break;}

    if (r && c) return false;
    return true;
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("op.txt", "w", stdout);

    int T,t;
    int i,j,k,n,m;
    int a[100][100];
    bool ko;

    cin>>T;t=1;
    while (T--)
    {
        cin>>n>>m;ko=1;
        for (i=0;i<n;i++)
            for (j=0;j<m;j++)
                cin>>a[i][j];

         for (i=0;i<n;i++)
            for (j=0;j<m;j++)
                if (!ok(a,n,m,i,j)) ko=0;


        cout<<"Case #"<<t<<": ";
        if (ko) cout<<"YES"<<endl;
        else cout<<"NO"<<endl;
        t++;
    }

    return 0;
}
