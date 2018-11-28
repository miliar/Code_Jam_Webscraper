#include <iostream>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <unordered_map>
#include <cstdlib>
#include <cstdio>
#include <stack>
#include <string>
#include <cstring>
#include <limits.h>

using namespace std;

#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define M_PI		3.14159265358979323846
#define forn(i, n) for(int i = 0; i < n; ++i)
#define forr(i, j, k) for(int i = j; i <= k; ++i)
#define all(x) begin(x), end(x)
typedef long long ll;
typedef long double ld;
typedef pair<int, double> pid;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vi> vii;
typedef vector<string> vs;

ifstream fin("B-small-attempt5.in");
ofstream fout("b.out");
template<class T>
void printVec(vector<T> v){
    for(auto x : v)
        cout << x << ' ';
    cout << endl;
}
template<class T>
void print2DVec(vector<vector<T> > V){
    for(auto v : V)
        printVec<T> (v);
}
struct cmp{
    bool operator () (const pid &p1, const pid &p2){
        return p1.second > p2.second;
    }
};
const double eps = 1e-12;

void solve(){
    int n;
    double v, x;
    fin >> n >> v >> x;
    double a[100], b[100];
    forn(i, n){
        fin >> a[i] >> b[i];
    }
    if(n == 2 && abs(b[0] - b[1]) < eps){
        n = 1;
        a[0] = a[0] + a[1];
    }
    if(n == 1){
        if(b[0] > x + eps || b[0] < x - eps){
            fout << "IMPOSSIBLE"  << endl;
        }
        else
            fout << v / a[0] << endl;
    }
    else if (n == 2){
        if((b[1] - x) * (b[0] - x) > eps){
            fout << "IMPOSSIBLE" << endl;
            cout << b[0] << ' ' <<b[1] << ' ' << x << endl;
        }
        else{
            double v0 = v * (x - b[1]) / (b[0] - b[1]);
            double v1 = v - v0;
            double t0 = v0 / a[0];
            double t1 = v1 / a[1];
            fout << max(t1, t0) << endl;
        }


    }

}

int main(){
    int T;
    fout.setf(ios::fixed);
    fout.precision(12);
	fin >> T;
    for(int tc = 1;tc <= T; ++tc){
		cout << "Calculating case #" << tc <<"....\n";
        fout << "Case #" << tc << ": ";
        solve();
    }
}
