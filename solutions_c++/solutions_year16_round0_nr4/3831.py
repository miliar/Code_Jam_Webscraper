#include <iostream>
#include <cstdio>
using namespace std;
int caso,t,n,k,c,s;
int main()
{
    freopen("D.in","r",stdin);
    freopen("D.out","w",stdout);
    cin>>t;
    for (caso=1;caso<=t;caso++){
        cin>>k>>c>>s;
        cout<<"Case #"<<caso<<": ";
        for (int i=1;i<k;i++)
            cout<<i<<" ";
        cout<<k<<endl;
    }
    return 0;
}
