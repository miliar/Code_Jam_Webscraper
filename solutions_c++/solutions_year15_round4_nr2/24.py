#include<bits/stdc++.h>
#include<cmath>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
#define FZ(n) memset((n),0,sizeof(n))
#define FMO(n) memset((n),-1,sizeof(n))
#define MC(n,m) memcpy((n),(m),sizeof(n))
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define FOR(x,y) for(__typeof(y.begin())x=y.begin();x!=y.end();x++)
#define IOS ios_base::sync_with_stdio(0); cin.tie(0)
// Let's Fight!

typedef pair<double, double> pdd;

const int MAXN = 111;
const double EPS = 1E-10;

int N;
double V, X;
pdd src[MAXN];

double calc()
{
    for(int i=0; i<N; i++)
        src[i].F -= X;
    sort(src, src+N);
    if(src[0].F > EPS || src[N-1].F < -EPS)
        return -1;

    double avg = 0;
    double sv = 0;
    for(int i=0; i<N; i++)
    {
        avg += src[i].F * src[i].S;
        sv += src[i].S;
    }
    avg /= sv;

    if(avg < 0)
    {
        reverse(src, src+N);
        for(int i=0; i<N; i++)
            src[i].F = -src[i].F;
    }

    double nowv = 0, nowxv = 0;
    for(int i=0; i<N; i++)
    {
        if(nowxv + src[i].F * src[i].S < EPS)
        {
            nowxv += src[i].F * src[i].S;
            nowv += src[i].S;
        }
        else
        {
            nowv += -nowxv / src[i].F;
            break;
        }
    }

    return V / nowv;
}

int main()
{
    IOS;
    int T;
    cin>>T;
    for(int tt=1; tt<=T; tt++)
    {
        cin>>N>>V>>X;
        for(int i=0; i<N; i++)
            cin>>src[i].S>>src[i].F;

        double ans = calc();
        cout<<"Case #"<<tt<<": ";
        if(ans < 0) cout<<"IMPOSSIBLE";
        else cout<<fixed<<setprecision(10)<<ans;
        cout<<endl;
    }
    return 0;
}
