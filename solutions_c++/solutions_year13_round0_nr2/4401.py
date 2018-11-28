#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;

#define vi vector<int>
#define vii vector< vector<int> >
#define vs vector<string>
#define iii pair<int,int>
#define i64 long long
#define pb push_back
#define FOR(i,j,k) for(int i = (j) ; i <= (k) ; i++ )
#define FORN(i,j,k) for(int i = (j) ; i >= (k) ;i--)
#define FORI(xx,x,it) for(xx::iterator it = x.begin() ; it != x.end() ; it++)
#define FORNI(xx,x,it) for(xx::reverse_iterator it = x.rbegin() ; it != x.rend() ; it++)
#define si size()
#define all(a) (a.begin(),a.end())
#define allr(a) (a.rbegin(),a.rend())
#define MAX 100000
#define INF 2140000000
#define MOD 1000000007

int t,n,m;
int lawn[100][100];

bool check1(int ii, int jj) {

    FOR(i,0,m-1) {
        if(lawn[ii][i] > lawn[ii][jj])
            return 0;
    }

    return 1;
}


bool check2(int ii, int jj) {

    FOR(i,0,n-1) {
        if(lawn[i][jj] > lawn[ii][jj])
            return 0;
    }

    return 1;
}

int main() {
    freopen("B-large.in","r",stdin);
    freopen("jam2o.txt","w",stdout);


    cin >> t;

    FOR(kk,1,t) {
            cin >> n >> m;

            FOR(i,0,n-1) {
                FOR(j,0,m-1) {
                    cin >> lawn[i][j];
                }
            }

             cout << "Case #" << kk << ": ";

            bool val = 1;

            FOR(i,0,n-1) {
                FOR(j,0,m-1) {
                    if(!(check1(i,j) || check2(i,j))) {
                        val = 0;
                        break;
                    }
                }

                if(!val)
                    break;
            }

            if(val)
                cout << "YES\n";
            else
                cout << "NO\n";
    }

	return 0;
}
