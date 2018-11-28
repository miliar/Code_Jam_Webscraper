#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int a[111111];

int main()
{
    //freopen("a.in","r",stdin);
    //freopen("a.out","w",stdout);
    int cas,cass=0,n,m;
    cin>>cas;
    while(cas--){
        cass++;
        cin>>n>>m;
        for(int i=1;i<=n;i++)
            cin>>a[i];
        sort(a+1,a+1+n);
        int p=1,q=n;
        int ans=0;
        while(p<=q){
            if(a[p]+a[q]<=m)
                ans++,p++,q--;
            else
                ans++,q--;
        }
        cout<<"Case #"<<cass<<": "<<ans<<endl;
    }


    return 0;
}
