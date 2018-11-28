#include<algorithm>
#include<cstdio>
#include<iostream>
#include<map>
#include<set>
#include<sstream>
#include<queue>
#include<vector>

using namespace std;

#define forn(i,n) for(int i=0;i<n;i++)
#define all(v) v.begin(),v.end()

int n;
long double vol,tempgoal;
vector<long double> volpers,temps;

void upd(long double &res, long double othervalue)
{
    if(res < -1.)
        res = othervalue;
    else if(res > othervalue)
        res = othervalue;
    return;
}

long double calc2(int a, int b)
{
    long double mn = 0., mx = vol/volpers[a];
    while(mx-mn>1e-12)
    {
        long double XA = (mx+mn)/2.;
        long double XB = (vol-volpers[a]*XA)/volpers[b];
        if((temps[a]*(XA*volpers[a]) + temps[b]*(XB*volpers[b]))/(XA*volpers[a]+XB*volpers[b]) < tempgoal)
            mx = XA;
        else
            mn = XA;
    }
    long double XA = (mx+mn)/2.;
    long double XB = (vol-volpers[a]*XA)/volpers[b];
    return max(XA,XB);
}

long double calc()
{
    long double res = -2.;
    forn(i,n)
    {
        if(temps[i] == tempgoal)
            upd(res,vol/volpers[i]);
        else
        forn(j,i)
        {
            if(temps[i] < tempgoal && temps[j] > tempgoal)
                upd(res,calc2(i,j));
            else if(temps[i] > tempgoal && temps[j] < tempgoal)
                upd(res,calc2(j,i));
        }
    }
    forn(i,n)
    forn(j,i)
    if(temps[i] == tempgoal && temps[j] == tempgoal)
    {
        upd(res,vol/(volpers[i]+volpers[j]));
    }
    return res;
}

int main()
{
    freopen("B-small.in","r",stdin);
    freopen("B-small.out","w",stdout);
	int casos;
    cin >> casos;
    for(int casito = 1; casito <= casos; casito++)
    {
        cin >> n >> vol >> tempgoal;
        volpers.resize(n);
        temps.resize(n);
        forn(i,n)
            cin >> volpers[i] >> temps[i];
        long double c =calc();
        if(c < -1)
            cout << "Case #"<<casito<<": IMPOSSIBLE" << endl;
        else
        {
            cout << "Case #"<<casito<<": ";
            printf("%.12f\n",(double)c);
        }
    }
}
