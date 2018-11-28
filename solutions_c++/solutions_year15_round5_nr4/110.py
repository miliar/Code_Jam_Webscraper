#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;
typedef long long ll;
const int MAXN = 1100;

ifstream fin ("D.in");
ofstream fout ("D.out");

vector <pair <ll, ll> > v;
ll ntot;

int N;
vector <ll> res;
vector <ll> g;

ll gcd (ll a, ll b)
{
    if (b == 0) return a;
    return gcd (b, a % b);
}

vector <pair <ll, ll> > t;

void solve()
{
    while (v.size() > 1)
    {
        ll nval = v[1].first;
        //cout << nval << " " << v.size() << endl;
        res.push_back (nval);
        
        t.clear();
        int tloc = 0;
        for (int i = 0; i < v.size(); i++)
        {
            if (tloc < t.size() && v[i].first == t[tloc].first + nval)
            {
                v[i].second -= t[tloc].second;
                tloc++;
            }
            
            if (v[i].second > 0)
                t.push_back (make_pair (v[i].first, v[i].second));
        }
        
        v.clear();
        for (int i = 0; i < t.size(); i++)
            v.push_back (t[i]);
    }
    
    while (v[0].second > 1)
    {
        v[0].second /= 2;
        res.push_back(0);
    }
    sort (res.begin(), res.end());
}

int main()
{
    int ntest = 0;
    fin >> ntest;
    for (int test = 0; test < ntest; test++)
    {
        v.clear();
        res.clear();
        g.clear();
        t.clear();
        
        int P; fin >> P;
        for (int i = 0; i < P; i++)
        {
            ll e; fin >> e;
            v.push_back (make_pair (e, 0));
        }
        for (int i = 0; i < P; i++)
            fin >> v[i].second;
        
        sort (v.begin(), v.end());
        
        ntot = -v[0].first;
        for (int i = 0; i < P; i++)
            v[i].first += ntot;
        solve();
        
        N = res.size();
        sort (res.begin(), res.end());
        /*ll x = res[0];
        for (int i = 0; i < N; i++)
        {
            x = gcd (x, res[i]);
            g.push_back (x);
        }*/
        
        fout << "Case #" << test + 1 << ":";
        
        for (int i = 0; i < N; i++)
            fout << " " << res[i];
        fout << "\n";
    }
    return 0;
}
