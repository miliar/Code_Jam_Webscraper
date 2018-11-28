#include <bits/stdc++.h>

typedef long long ll;
using namespace std;

#define all(x) x.begin(), x.end()
#define f(i,a,b) for(int i = (a); i <= (b); i++)
#define fd(i,a,b) for(int i = (a); i >= (b); i--)
#define mp make_pair
#define faster_io() ios_base::sync_with_stdio(false)
#define pb push_back
#define pii pair<int,int>
#define SZ(x) ((int)x.size())
#define vii vector<pair<int,int>>

const int INF = 1000000005;
const ll INFLL = 100000000000000000ll;
const ll MOD = 1000000007;

// ----------------------------------------------------------------

int T, N;
vector<double> Start, Speed;

ifstream fin("C.TXT");
ofstream fout("C.OUT");

bool ok()
{
    double fail = .00000000001;
    double p = 0, t = 0;
    int n = SZ(Start);

    //cout << "There are " << n << " hikers\n";

    while(true)
    {
        double nx = 360.05;
        //cout << p << " " << t << "\n";

        f(i,0,n-1)
        {
            double pos = t*Speed[i] + Start[i];
            while(pos > 360) pos -= 360;
            if(pos >= p && pos < 360) nx = min(nx,pos);
        }

        if(abs(nx-p) < fail) return false;

        p = nx;
        if(p > 360.0) return true;

        double nt = INF;
        f(i,0,n-1)
        {
            double pos = t*Speed[i] + Start[i];
            while(pos > 360) pos -= 360;
            pos += fail;
            //cout << i << " is at " << pos << " with Speed " << Speed[i] << "\n";
            double ti = pos >= p ? (360.0 - (pos - p)) / Speed[i] : (p - pos) / Speed[i];
            //cout << i << " reaches me in " << ti << "\n";
            nt = min(nt,ti);
        }
        //cout << nt << "\n";
        t += nt;
    }
}

int main()
{
    fin >> T;

    f(t,1,T)
    {
        fin >> N;

        Start.clear(), Speed.clear();

        f(i,1,N)
        {
            double m,p;
            int k;
            fin >> p >> k >> m;
            f(x,0,k-1)
            {
                double sp = 360.00 / (m+x);
                Start.pb(p);
                Speed.pb(sp);
            }
        }

        if(ok()) fout << "Case #" << t << ": 0\n";
        else fout << "Case #" << t << ": 1\n";
    }
}
