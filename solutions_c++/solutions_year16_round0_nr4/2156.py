#include <bits/stdc++.h>
#define ll long long
using namespace std;
ll t,k,c,s,kpow;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin >> t;
    for(int i=1;i<=t;i++)
    {
        cin >> k >> c >> s;
        kpow=1;
        for(int j=1;j<c;j++)
            kpow*=k;
        cout << "Case #" << i << ":";
        if(kpow==1)
        {
            for(int j=0;j<k;j++)
                cout << " " << j+1;
        }
        else for(int j=0;j<k;j++)
        {
            cout << " " << kpow*j+j+1;
        }
        cout << "\n";
    }
    return 0;
}
