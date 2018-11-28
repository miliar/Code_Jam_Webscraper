#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("Bout1.txt","w",stdout);
    int t;
    cin >> t;
    for(int IN=0; IN<t; ++IN){
        string a;
        cin >> a;
        int sw=0;
        int ans=0;
        for(int i=a.size()-1; i>=0; --i){
            if(a[i] == '+' && sw%2 == 0) continue;
            if(a[i] == '-' && sw%2) continue;
            sw++; ans++;
        }
        cout << "Case #" << IN+1 << ": " << ans << endl;
    }
}
