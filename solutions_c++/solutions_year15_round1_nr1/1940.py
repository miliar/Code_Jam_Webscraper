#include <bits/stdc++.h>
#define mp make_pair
#define ll long long

using namespace std;
vector <ll> v;

int main()
{
   freopen("in.txt" , "r" , stdin);
   freopen("out.txt" , "w" , stdout);
    int t;
    int a ;
    cin >> t ;
    a=0;
    while(a++ < t)
    {
        int n ;
        cin >> n;
        v.clear();
        for(int i = 0 ; i < n ; i ++)
        {
            ll x;
            cin >> x;
            v.push_back(x);
        }
        ll ans1=0 ;
        ll ans2=0;
        ll dif = 0;
        for(int i = 1 ; i < n ; i++)
        {
            if(v[i] < v[i-1])
            {
                ans1+= v[i-1] - v[i];
                dif = max(dif , v[i-1] - v[i]);
            }
        }
        for(int i = 0 ; i < n-1 ; i++)
        {
            if(v[i] < dif)
                ans2+=v[i];
            else
                ans2+=dif;
        }
        cout << "Case #" << a << ": " << ans1 << " " << ans2 << endl;
    }
}



