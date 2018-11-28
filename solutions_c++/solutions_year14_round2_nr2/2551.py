#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <algorithm>
#include <conio.h>
#include <iomanip>
#include <sstream>

#define fo(a, b, c) for(a = ( b ); a < ( c ); a++)
#define fr(a, b) fo(a, 0, ( b ))
#define fi(a) fr(i, ( a ))
#define fj(b) fr(j, ( b ))
#define fk(c) fr(k, ( c ))

#define ul64 uint_least64_t
#define uf64 uint_fast64_t
#define il64 int_least64_t
#define if64 int_fast64_t
#define vs vector<string>
#define vi vector<int>
#define vd vector<double>
#define vul64 vector<ul64>
#define vuf64 vector<uf64>
#define vil64 vector<il64>
#define vif64 vecotr<if64>
#define vc vector<char>
#define pb push_back
#define ppb pop_back
#define ss stringstream

#define MAX_LEN 50

using namespace std;

int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("l.out", "w", stdout);
    int i, j, k, tt, a, b, c;
    vi list;
    cin>>tt;
    int cases;
    int ctr;
    fr(cases, tt)
    {
        ctr = 0;
        cin>>a>>b>>c;
        fi(a)
        fj(b)
            if((i&j) < c) /*cout<<(a&b)<<" "<<c<<endl;*/ ctr++;
        cout<<"Case #"<<cases+1<<": "<<ctr<<endl;
    }
    return 0;
}
