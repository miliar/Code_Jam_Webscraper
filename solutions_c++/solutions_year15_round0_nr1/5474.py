#include<bits/stdc++.h>
using namespace std;
#define VAR(a,b) __typeof(b) a=(b)
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REP(i,n) FOR(i,0,n)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define SZ(c) (c).size()
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<PII> VPII;
typedef vector<VI> VVI;

int main()
{
    int t;
    cin>>t;
    for(int ix=1;ix<=t;ix++)
    {
        int n,as=0,ps=0;
        string ss;
        cin>>n>>ss;
        
        for(int i=0;i<ss.length();i++)
        {
            if(ss[i]=='0')
            ;
            else if(ps>=i)
            {
                ps+=(ss[i]-'0');
            }
            else
            {
                as+=(i-ps);
                ps =i+(ss[i]-'0');

            }
        }
        cout<<"Case #"<<ix<<": "<<as<<endl;
    }
}
