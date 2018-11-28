#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("B-small-attempt0 (3).in","r",stdin);
    freopen("orb.txt","w",stdout);
    int t,z;
    cin>>t;
    for(z=1;z<=t;z++)
    {
        int n;
        cin>>n;
        int mat[50][50],i,j,freq[2503]={0};
        for(i=0;i<2*n-1;i++)
        {
            for(j=0;j<n;j++)
            {
                cin>>mat[i][j];
                freq[mat[i][j]]++;
            }
        }
        cout<<"Case #"<<z<<": ";
        for(i=1;i<=2500;i++)
        {

            if(freq[i]&1)
                cout<<i<<" ";
        }
        cout<<endl;
    }
    return 0;
}
