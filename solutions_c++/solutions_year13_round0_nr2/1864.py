#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <fstream>
#include <string>
#include <cstdio>
#include <cmath>
#include <cstdlib>

#define FOR(i,a,b) for(int i=a;i<b;++i)
#define RFOR(i,a,b) for(int i=a;i>=b;--i)
#define REP(i,n) FOR(i,0,n)
#define RREP(i,n) RFOR(i,n-1,0)
#define EACH(it,v) for(typeof(v.begin()) it=v.begin();it!=v.end();++it)
#define INF (int)1<<30
#define vi vector<int>
#define vs vector<string>
#define pb push_back
#define mkp make_pair
#define ll unsigned long long int
#define uli unsigned long int
#define MAX (int)1e6

using namespace std;

ofstream fout ("B.out");
ifstream fin ("B-large.in");
//ifstream fin ("B.in");
#define cout fout
#define cin fin

int n, m;
int a[101][101];

bool validRow(int i, int j) {
    REP(k,m) {
        if(a[i][k] > a[i][j]) {
            return false;
        }
    }
    return true;
}

bool validCol(int i, int j) {
    REP(k,n) {
        if(a[k][j] > a[i][j]) {
            return false;
        }
    }
    return true;
}
int main() {
    int t;
    cin>>t;
    REP(T,t) {
        cin>>n>>m;
        char c;
        REP(i,n) {
            REP(j,m) {
                cin>>a[i][j];
            }
        }
        
        bool flag = false;
        
        REP(i,n) {
            REP(j,m) {
                if(!validRow(i,j) && !validCol(i,j)) {
                    flag = true;
                    break;
                }
            }
            if(flag) {
                break;
            }
        }
        
        cout<<"Case #"<<T+1<<": "<<(flag ? "NO" : "YES")<<endl;
    }
    system("pause");
    return 0;
}
