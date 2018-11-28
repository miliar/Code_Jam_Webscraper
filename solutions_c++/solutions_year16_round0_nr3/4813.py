#include <bits/stdc++.h>

using namespace std;
#define ll long long
ll n, J ;
vector<string> jamcoins ;

void rec(string s)
{
    if(s.size()==n-1)
    {
        s.push_back('1') ;
        jamcoins.push_back(s) ;
        return ;
    }
    string s2 = s ;
    s2.push_back('0') ;
    rec(s2) ;
    s2 = s ;
    s2.push_back('1') ;
    rec(s2) ;
    return ;
}

ll fastPower(ll b, ll p) {
    ll res = 1;
    while (p) {
        if (p & 1) // p is odd
            res *= b ;
        p >>= 1;
        b *= b;
    }
    return res;
}

ll getBase(string s, ll base)
{
    ll ret = 0 ;
    for(ll i=s.size()-1, j=0;i>=0;i--, j++)
    {
        if(s[i]=='1')
            ret += fastPower(base, j) ;
    }
    return ret ;
}

ll checkPrime(ll x)
{
    for(ll i=2;(i*i)<=x;i++)
    {
        if(x%i==0)
            return i ;
    }
    return -1 ;
}

int main()
{
    ios_base::sync_with_stdio(0) ;
    freopen("C-small-attempt0.in","r",stdin) ;
    freopen("C-small-attempt0.out","w",stdout) ;
    ll t, cs = 1 ;
    cin >> t ;
    while(t--)
    {
        cin >> n >> J ;
        string temp = "1" ;
        rec(temp) ; // go generate all possible jamcoins and put in vector jamcoins
        map<string, vector<ll> > ans ; // should contain: [non prime jamcoin] --> list of divisors in bases 2-->10
        for(ll i=0;i<jamcoins.size();i++)
        {
            vector<ll> vect ; // vector contains its representations in bases 2-->10
            for(ll base=2;base<=10;base++)
            {
                ll val = getBase(jamcoins[i], base) ;
                vect.push_back(val) ;
            }
            // now we need to check that all values in vect are not primes
            vector<ll> vect2 ; // should contain the divisors for all the bases in vect
            bool isOk = 1 ;
            for(int j=0;j<vect.size();j++)
            {
                ll val = checkPrime(vect[j]) ; // val should be the divisor of the number
                if(val==-1)
                {
                    isOk = 0 ;
                    break ;
                }else
                    vect2.push_back(val) ;
            }
            if(isOk)
                ans[jamcoins[i]] = vect2 ;
            if(ans.size()==J)
                break ;
        }
        cout << "Case #" << cs << ":\n" ;
        for(map<string, vector<ll> >::iterator it=ans.begin();it!=ans.end();it++)
        {
            cout << it->first << " " ;
            vector<ll> vect = it->second ;
            for(int i=0;i<vect.size();i++)
                cout << vect[i] << " " ;
            cout << endl ;
        }
    }

    return 0;
}
