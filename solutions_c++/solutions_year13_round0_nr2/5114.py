#include <iostream>

using namespace std;

int t,n,m;
int a [100][100];

bool hBig(int x,int y)
{
    for (int i=0; i<n; i++)
        if (a[x][y]<a[i][y])
            return false;
    return true;
}

bool wBig(int x,int y)
{
    for (int i=0; i<m; i++)
        if (a[x][y]<a[x][i])
            return false;
    return true;
}

int main()
{
    bool ans;
    cin>>t;
    for (int i=0; i<t; i++)
    {
        ans=true;
        cin >>n>>m;
        for (int j=0; j<n; j++)
            for (int k=0; k<m; k++)
                cin >>a[j][k];

        for (int j=0; j<n; j++)
            for (int k=0; k<m; k++)
                if (!(wBig(j,k) || (hBig(j,k))))
                    ans=false;
        cout << "Case #" <<i+1;
        if (ans)
            cout<<": YES"<<endl;
        else
            cout<<": NO"<<endl;
    }
    return 0;
}
