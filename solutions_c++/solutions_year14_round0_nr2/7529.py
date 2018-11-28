#include <iostream>
#include <cmath>
#include <algorithm>
#include <ios>
#include <fstream>
#include <stdio.h>
#include <string>
#include <vector>
#include <sstream>
#include <cmath>
#include <deque>

using namespace std;
struct _ { ios_base::Init i; _() { cin.sync_with_stdio(0); cin.tie(0); } } _;

typedef long long ll;
typedef long double ld;
typedef vector<ll> vl;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef pair<ll,ll> llp;

#define sz(a) int((a).size())
#define pb push_back
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define btr(c, i) for(typeof((c).rbegin()) i = (c).rbegin(); i != (c).rend(); i++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define strrev(c) (string((c).rbegin(), (c).rend()))
#define INF 1000000
#define OUT2(X) {cout X; out X;}

int main() {
    ifstream in("B-large.in");
    ofstream out("b_out.txt");
    int cases;
    in >> cases;
    out.precision(15);
    cout.precision(15);
    for (int t = 1; t <= cases; t++) {
        ld f,c,x,cur=2.0, ans=0.0;
        in >> c >> f >> x;
        while (true) {
            if ( (c / cur + x / (cur + f)) < (x / cur) ) {
                ans += c / cur;
                cur += f;
            } else {
                ans += x / cur;
                break;
            }
        }
        OUT2(<< "Case #" << t << ": ");
        OUT2(<< ans << '\n');
    }
    return 0;
}
