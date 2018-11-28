#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("Dout.txt","w",stdout);
    int t;
    cin >> t;
    for(int IN=0; IN<t; ++IN){
        cout << "Case #" << IN+1 << ": ";
        long long k, c;
        cin >> k >> c;
        long long s;
        cin >> s;
        for(int i=0; i<s; ++i)
            cout << i+1 << " " ;
        cout << endl;
    }
}
