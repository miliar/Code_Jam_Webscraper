#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <sstream>
#include <math.h>

#define fo(a, b, c) for(a = ( b ); a < ( c ); a++)
#define fr(a, b) fo(a, 0, ( b ))
#define fi(a) fr(i, ( a ))
#define fj(b) fr(j, ( b ))
#define fk(c) fr(k, ( c ))

#define ul64 uint_least64_t
#define vs vector<string>
#define vi vector<int>
#define vd vector<double>
#define vul64 vector<ul64>
#define vc vector<char>
#define pb push_back
#define ppb pop_back
#define ss stringstream

#define ROWS 4
#define COLS 4

using namespace std;

double solve(double &cookie, double t, double &mul, double c, double f, double x)
{
    double t1 = (double)(x - cookie)/mul;
    double mul2 = mul + f;
    double ck2 = 0;
    double t2 = (double)c/mul + ((double)x)/mul2;

    if(t1<t2){
        cookie = x;
        return t1;
    }
    else{
        cookie = ck2;
        t2 = (double)c/mul;
        mul = mul2;
        return t2;
    }
}

int main()
{
    int i, j, k, tt, cases;
    double c, f, x;
    double ckee, mul;
    double tm;
    double time, tc;
    freopen("b-large.in", "r", stdin);
    freopen("b-large.out", "w", stdout);
    cin>>tt;
    cout<<std::fixed<<setprecision(7)<<setiosflags(ios::showpoint);
    fr(cases, tt)
    {
        time = tc = ckee = 0;
        cin>>c>>f>>x;
        mul = 2;
        tc = ((double)c/mul);
        ckee = 0;
        while(ckee < x){
            time += solve(ckee, time, mul, c, f, x);
        }
        cout<<"Case #"<<cases+1<<": "<<time<<endl;
    }
}
