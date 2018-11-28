#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <algorithm>
#include <map>
#include <cmath>
#include <set>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;

#define fi first
#define se second
#define mp make_pair
#define pb push_back

const int INF = 1 << 30;
const double EPS = 1e-8;

vector<string> v;
int maks=-1, ile=0,n,m;

int trie(vi& t)
{
    set<string> s;
    for(int i=0; i<t.size(); i++)
    {
        int cur=t[i];
        for(int j=0; j<v[cur].size(); j++)
        {
            s.insert(v[cur].substr(0,j+1));
        }
        //cout<<v[cur]<<" ";
    }
    //cout<<"wyszlo "<<1+s.size()<<"\n";
    if(!s.size()) return 0;
    return 1+s.size();
}

void wylicz(vector<vi>& t)
{
    int wezly=0;
    //cout<<"wyliczam:\n";
    for(int i=0; i<n; i++)
    {
        //cout<<"t"<<i<<": ";
        wezly+=trie(t[i]);
    }
    if(wezly>maks)
    {
        maks=wezly;
        ile=1;
    }
    else if(wezly==maks)
    {
        ile++;
    }
}

void nawalaj(int x, vector<vi> t)
{
    if(x==m)
    {
        return wylicz(t);
    }
    for(int i=0;i<n;i++)
    {
        vector<vi> t2=t;
        t2[i].pb(x);
        nawalaj(x+1, t2);
    }
}

void solve(int num)
{
    cin>>m>>n;
    v.resize(m);
    for(int i=0; i<m; i++) cin>>v[i];
    maks=-1;
    ile=0;
    nawalaj(0, vector<vi>(n));
    cout<<"Case #"<<num<<": "<<maks<<" "<<ile<<"\n";


}

int main()
{
    ios_base::sync_with_stdio(0);
    int t;
    cin>>t;
    for(int i=1; i<=t; i++)
    {
        solve(i);
    }
}

