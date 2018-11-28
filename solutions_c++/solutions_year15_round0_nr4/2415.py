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
    int t,j;
    cin>>t;
    for(j=1;j<=t;j++)
    {
        int x,r,c;
        cin>>x>>r>>c;
        cout<<"Case #"<<j<<": ";
        if(x==1)
        {
            if(r*c%1==0)
            cout<<"GABRIEL"<<endl;
            else
            cout<<"RICHARD"<<endl;
        }
        else
		 if(x==2)
        {
            if((r*c)%2==0)
            {
                cout<<"GABRIEL"<<endl;
            }
            else
            {
                cout<<"RICHARD"<<endl;
            }
        }
        else if(x==3)
        {
            if((r*c)==6||r*c==9||r*c==12)
            {
                cout<<"GABRIEL"<<endl;
            }
            else
            {
                cout<<"RICHARD"<<endl;
            }
        }
        else
		 if(x==4)
        {
            if((r*c)==12||(r*c)==16)
            {
                cout<<"GABRIEL"<<endl;
            }
            else
            {
                cout<<"RICHARD"<<endl;
            }
        }
    }
}
