#include<iostream>
#include<string>
#include<math.h>
#include<vector>
#include<string.h>
#include<cstdio>
using namespace std;

int main()
{
    int n,m,k;
    int t;
    freopen("input.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>t;
    for (int i=1;i<=t;i++)
    {
        cout<<"Case #"<<i<<": ";
        cin>>n>>m>>k;
        int ans=0;
        for (int j=0;j<n;j++)
            for (int x=0;x<m;x++)
            if ((j&x)<k) ans++;
          //  cout<<j<<" "<<x<<" : ";
        cout<<ans<<endl;

    }
 return 0;
}
