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
#define X first
#define Y second
#define mp make_pair
#define pb push_back
#define double long double

const int INF = 1 << 30;
const double EPS = 1e-16;

int n;
double v, x;
vector<pair<double,double> > cr(200);

int check(double t)
{
    double v0=0, x0=0;
    for(int i=0;i<n;i++)
    {
        double v1=min(cr[i].Y*t,v-v0);
        double x1=cr[i].X;
        x0=(v0*x0+v1*x1)/(v0+v1);
        v0+=v1;
    }
    if(v0*(1.0+EPS)<v) return 0;
    if(x0>x*(1.0+EPS)) return 0;

    // COPYPASTE!! DANGER!!
    v0=0; x0=0;
    for(int i=n-1;i>=0;i--)
    {
        double v1=min(cr[i].Y*t,v-v0);
        double x1=cr[i].X;
        x0=(v0*x0+v1*x1)/(v0+v1);
        v0+=v1;
    }
    if(v0*(1.0+EPS)<v) return 0;
    if(x0*(1.0+EPS)<x) return 0;
    return 1;
}

void solve(int num)
{
    cin>>n>>v>>x;
    int fail=0;
    double mini=1000, maksi=0;
    cr.resize(n);
    for(int i=0;i<n;i++)
    {
        cin>>cr[i].Y>>cr[i].X;
        mini=min(mini,cr[i].X);
        maksi=max(maksi,cr[i].X);
    }
    sort(cr.begin(),cr.end());
    double st=0.0, en=INF; en*=en; en*=INF;
    if(maksi<x || mini>x) fail=1;
    else
    {
        while(st*(1+EPS)<en)
        {
            double shot=(st+en)/2.0;
            if(check(shot)) en=shot;
            else st=shot;
        }
    }

    cout<<"Case #"<<num<<": ";
    if(fail) cout<<"IMPOSSIBLE\n";
    else cout<<en<<"\n";
}

int main()
{
    ios_base::sync_with_stdio(0);
    int t;
    cin>>t;
    cout<<setprecision(8)<<fixed;
    for(int i=1; i<=t; i++)
    {
        solve(i);
    }
}

