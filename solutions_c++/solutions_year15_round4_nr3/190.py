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

void solve(int num)
{
    int n;
    cin>>n;
    map<string, vector<int> > m;
    string meh;
    getline(cin,meh);
    map<string,int> english, french;
    int common=0;
    for(int i=0;i<n;i++)
    {
        string s,cur="";
        getline(cin, s);
        s+=' ';
        for(int j=0;j<s.length();j++)
        {
            if(s[j]==' ')
            {
                if(i==0) english[cur]+=0;
                else if(i==1) french[cur]+=0;
                else
                {
                    m[cur].pb(i);
                    if(english.count(cur))
                    {
                        m[cur].pb(0);
                        english[cur]++;
                    }
                    if(french.count(cur))
                    {
                        m[cur].pb(1);
                        french[cur]++;
                    }
                }

                cur="";
            }
            else cur+=s[j];
        }
        /*if(cur.length())
        {
            if(i==0) english[cur]+=0;
            else if(i==1) french[cur]+=0;
            else
            {
                m[cur].pb(i);
                if(english.count(cur))
                {
                    m[cur].pb(0);
                    english[cur]++;
                }
                if(french.count(cur))
                {
                    m[cur].pb(1);
                    french[cur]++;
                }
            }
        }*/
    }
    set<string> bleh;
    for(auto e : english)
    {
        if(e.se == 0) bleh.insert(e.fi);
    }
    for(auto f : french)
    {
        if(f.se) continue;
        if(bleh.count(f.fi)) common++;
    }
    int ans=INF;
    // 0-english 1-french
    for(int mask=2;mask<(1<<n);mask+=4)
    {
        int cur=0;
        for(auto it : m)
        {
            int eng=0, fr=0;
            for(int j=0;j<it.se.size();j++)
            {
                if(mask&(1<<it.se[j])) fr++;
                else eng++;
            }
            if(eng&&fr) cur++;
        }
        ans=min(ans,cur);
    }

    cout<<"Case #"<<num<<": "<<ans+common<<"\n";

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

