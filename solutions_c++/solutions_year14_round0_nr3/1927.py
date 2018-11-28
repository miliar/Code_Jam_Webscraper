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
#define CL(a,v) memset((a),(v),sizeof(a))

int w[6][6];
int d[6][6];

int dx[] = {-1,-1,-1,0,0,1,1,1};
int dy[] = {-1,0,1,-1,1,-1,0,1};

bool f;

void print_f(VI v, int r, int c) {
    map<int,string> h;
    h[0] = ".";
    h[1] = "*";
    h[2] = "c";
    REP(i,r) {
        REP(j, c) {
            cout<<h[v[i*c+j]];
        }
        cout<<endl;
    }
}

bool check(int x, int y, int r, int c) {
    if (x>=0 && x<r && y>=0 && y<c) {
        return true;
    }
    return false;
}

void go(int x, int y, int r, int c) {
    w[x][y] = 1;
    int num = 0;
    REP(k,8) {
        int nx = x+dx[k];
        int ny = y+dy[k];
        if (check(nx,ny,r,c) && d[nx][ny]) num++;
    }
    //cout<<x<<" "<<y<<" :"<<num<<endl;
    if (num == 0) {
        REP(k,8) {
            int nx = x+dx[k];
            int ny = y+dy[k];
            if (check(nx,ny,r,c) && !w[nx][ny]) {
                go(nx,ny,r,c);
            }
        }
    }
}

int ok(VI v, int r, int c) {
    //print_f(v,r,c);
    CL(w,0); CL(d,0);
    f = false;
    REP(i,r) REP(j,c) d[i][j] = v[i*c+j];
    REP(i,r) {
        REP(j,c) {
            if (d[i][j] == 0) {
                REP(ii,r) REP(jj,c) w[ii][jj] = d[ii][jj];
                go(i,j,r ,c);
                 // cout<<endl;
                 // REP(aa,r) REP(bb,c) cout<<w[aa][bb]<<" ";
                 // cout<<endl;
                f = true;
                REP(ii,r) REP(jj,c) if (!w[ii][jj]) f=false;
                //cout<<"is ok:"<<f<<endl;
                if (f) {
                    return i*c+j;
                }
            }
        }
    }
    return -1;
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#endif

    int T; cin>>T;
    REP(t,T){
        int r,c,m; cin>>r>>c>>m;
        //cout<<r<<" "<<" "<<c<<" "<<m<<endl;
        int n = r*c;
        VI v(n);
        REP(i,m) {
            v[n-1-i] = 1;
        }

        cout<<"Case #"<<t+1<<": \n";
        bool was = false;
        do {
            int res = ok(v,r,c);
            //cout<<res<<endl;
            if (res>=0) {
                v[res] = 2;
                print_f(v,r,c);
                was = true;
                break;
            }
        } while(next_permutation(v.begin(), v.end()));
        if (!was) cout<<"Impossible"<<endl;
    }


    return 0;
}