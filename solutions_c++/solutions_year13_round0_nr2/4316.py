#include<iostream>
#include<algorithm>
#include<cstring>
#include<cstdio>
using namespace std;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int casos,n,m;
    bool b;
    int mat[105][105],maxi[105],maxj[105];
    cin>>casos;
    for(int k=1;k<=casos;k++)
    {
        cin>>n>>m;
        b = true;
        memset(maxi,0,sizeof(maxi));
        memset(maxj,0,sizeof(maxj));
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
                cin>>mat[i][j];
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
            {
                maxi[i] = max(mat[i][j],maxi[i]);
                maxj[j] = max(mat[i][j],maxj[j]);
            }
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
            {
                if(!(mat[i][j] >= maxi[i] or mat[i][j] >= maxj[j]))
                {
                    b = false;
                    break;
                }
            }
        cout<<"Case #"<<k<<": ";
        if(b)
            cout<<"YES"<<endl;
        else
            cout<<"NO"<<endl;

    }
    return 0;
}
