#include <bits/stdc++.h>

using namespace std;

#define ld long double
#define pld pair<ld,ld>
#define ff first
#define ss second
#define vpld vector<pld>
#define pb push_back
#define LL long long
#define MOD 1000000007
#define rep(i,a,b) for(LL i = a; i<=b ; ++i)

LL t,k,c,s;

int main()
{
    cin >> t;

    rep(tt,1,t){
    cin >> k >> c >> s;

    
    LL prod = 1;
    rep(i,1,c-1)
    {
        prod*=k;
    }

    cout << "Case #"<<tt<<": ";
    rep( i ,1, k)
    {
        cout << (i-1)*prod + 1<<" ";
    }

    cout <<"\n";
    }

    return 0;
}
