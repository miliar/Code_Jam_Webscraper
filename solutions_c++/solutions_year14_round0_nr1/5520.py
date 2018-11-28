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


int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#endif

    int T; cin>>T;
    REP(i,T){
        int n; cin>>n; n--;
        vector<int> v(16); REP(j,16) cin>>v[j];
        int m; cin>>m; m--;
        vector<int> v2(16); REP(j,16) cin>>v2[j];
        int cnt = 0;
        int res = 0;
        REP(j,4) {
            REP(k,4) {
                //cout<<v[n*4+j]<<" "<<v2[m*4+k]<<endl;
                if (v[n*4+j] == v2[m*4+k]) {
                    cnt++;
                    res = v[n*4+j];
                    break;
                }
            }
        }
        cout<<"Case #"<<i+1<<": ";
        if (cnt == 1) {
            cout<<res<<endl;
        }
        if (cnt == 0) {
            cout<<"Volunteer cheated!"<<endl;
            
        } 
        if (cnt>1) {
            cout<<"Bad magician!"<<endl;
        }



    }


    return 0;
}