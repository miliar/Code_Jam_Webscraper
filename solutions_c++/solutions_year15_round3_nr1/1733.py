#include <bits/stdc++.h>
#define FOR(i,n) for(int i =0; i < n; i++)
#define ll long long
#define s(a) cin>>a;

using namespace std;

int main()
{
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t, x,answer;
    s(t)
    x = 1;
    while(t--)
    {
        int r, c, l;
        s(r) s(c) s(l)
        //cout<<r<<c<<l<<endl;
        answer = (c-r)/l + l;

        cout<<"Case #"<<x<<": "<<answer<<endl;
        x++;
    }


    return 0;
}
