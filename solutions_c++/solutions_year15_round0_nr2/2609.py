#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

void incr(vector<int> &d)
{
    for (int i=0; i<d.size(); i++)
    {
        d[i]++;
    }
}

void decr(vector<int> &d)
{
    for (int i=0; i<d.size(); i++)
    {
        d[i]--;
    }
}

int getMax(vector<int> &d)
{
    int b=0;
    int mx = d[0];
    for (int i=1; i<d.size(); i++)
    {
        if (mx<d[i])
        {
            mx=d[i];
            b=i;
        }
    }

    return b;
}

void split(vector<int> &d, int mxi, vector<int> &basesplit)
{
    int t = basesplit[d[mxi]];
    d[mxi]-=t;
    d.push_back(t);
}

void unsplit(vector<int> &d, int mxi)
{
    int t = d.back();
    d[mxi]+=t;
    d.pop_back();
}

string hasht(vector<int> &d)
{
    string s;
    for (int i=0; i<d.size(); i++) s.push_back(d[i]+'0');
    sort(s.begin(), s.end());
    return s;
}

unordered_map<string, int> mem;

int calc(vector<int> &d)
{
    //static int safe = 0;
    //safe++;
    //if (safe>1000) return 0;
    string s = hasht(d);
    if (mem.count(s)>0) return mem[s];

    int mxi = getMax(d);
    if (d[mxi]<=3) return d[mxi];
    decr(d);
    int ans = calc(d);
    incr(d);

    /*split(d, mxi, bsplit);
    ans = min(ans, calc(d,bsplit));
    unsplit(d, mxi);
    */

    int dmax = d[mxi];
    /*for (int i=0; i<bsplit[dmax].size(); i++)
    {
        d[mxi]-=bsplit[dmax][i];
        d.push_back(bsplit[dmax][i]);
        ans = min(ans, calc(d, bsplit));
        d.pop_back();
        d[mxi]+=bsplit[dmax][i];
    }*/
    for (int i=1; i<dmax; i++)
    {
        d[mxi]-=i;
        d.push_back(i);
        ans = min(ans, calc(d));
        d.pop_back();
        d[mxi]+=i;
    }

    return mem[s] = ans+1;
}

int main()
{
    freopen("B-small-attempt5.in", "r", stdin);
    freopen("b.out", "w", stdout);

    int T;
    cin>>T;
    for (int cas=1; cas<=T; cas++)
    {
        int n;
        cin>>n;
        vector<int> d(n);
        for (int i=0; i<n; i++)
        {
            cin>>d[i];
        }

        cout<<"Case #"<<cas<<": "<<calc(d)<<endl;
    }

    return 0;
}
