#include <bits/stdc++.h>
using namespace std;

void solve(int tt)
{
    int n;
    cin >> n ;
    vector<int> v(10,0);
    vector<int> t(10,1);
    int i ;
    for(i = 1 ; i < 1001 ; i++)
    {
        int p = i * n ;
        do
        {
            v[ p % 10] = 1;
            p /= 10;
        }
        while(p);
        if(v == t) break;
    }
    if( i > 1000 ) cout<< "Case #" << tt<< ": INSOMNIA" <<endl;
    else cout << "Case #" << tt << ": " << i*n << endl;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    for(int tt = 1 ; tt <= t ;tt++)
        solve(tt);
    return 0;
}
