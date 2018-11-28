#include <bits/stdc++.h>
using namespace std;

void solve(int tt)
{

    long long  k,c,s;
    cin >> k >> c >> s;
    vector<long long> v(k,0),t(k,1);

    cout<<"Case #"<<tt<<": ";
    if(c==1)
    {
        if(k==s) for(int i = 1 ; i <= k ; i++)
            cout<<i<<' ';
        else cout << "IMPOSSIBLE";

        cout << endl;
    }
    else
    {
        if( c * s < k ) { cout<<"IMPOSSIBLE"<<endl; }
        else {for(int i = 0 ; i <  k ; i++) cout << i + 1 << ' ';
                     cout<<endl;
        }

    }
}
int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    for(int tt = 1 ; tt <= t ; tt++)
        solve(tt);
    return 0;
}
