#include <cstdio>
#include <iostream>
#include <cmath>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <sstream>
#include <iterator>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <cctype>
#include <limits>
#include<ctime>

using namespace std;
const double EPS = 1e-9;
//const long long  INF = 1000000000000000000;
#define ll long long

typedef pair<ll, ll> PII;
typedef pair<double,double> PDD;
typedef vector<long long> VLL;
typedef vector<int> VI;

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define REP(i,n) FOR(i,0,n)

#define UNIQUE(v) SORT(v), v.erase(unique(v.begin(),v.end()),v.end())
#define SORT(c) sort((c).begin(),(c).end())



double calc(double C, double F, double X) {
    double rate = 2;
    double time_spent =0;
    while(1) {
        double tge = X/rate;
        double tbf = (C)/rate;
        double tgebf = X/(rate+F);
        double tge2 = tbf + tgebf;
        if (fabs(tge-tge2)<EPS || tge<tge2) return time_spent + tge;
        time_spent += tbf;
        rate += F;
    }
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#endif

    int T; cin>>T;
    REP(t,T){
        double C,F,X; cin>>C>>F>>X;
        double res = calc(C,F,X);
        cout<<"Case #"<<t+1<<": ";
        printf ("%.7f\n", res);
    }


    return 0;
}