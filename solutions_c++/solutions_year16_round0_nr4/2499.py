/* coder: Anh Tuan Nguyen */
#include <bits/stdc++.h>
using namespace std;

int main()
{
#ifdef gsdt
    freopen("d-small-attempt0.in","r",stdin);
    freopen("d-small-attempt0.out","w",stdout);
#endif // gsdt

    int t;
    cin>>t;
    for(int i=1; i<=t; i++)
    {
        int k,c,s;
        cin>>k>>c>>s;
        cout<<"Case #"<<i<<": ";
        for(int j=1; j<=s; j++)
            cout<<j<<" ";
        cout<<endl;
    }

    return 0;
}

