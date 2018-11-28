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
    //ifstream in("A-small-attempt0.in");
    ifstream in("B-small-attempt0.in");
    ofstream out("output_b.txt");
    int cases;
    in >> cases;
    for (int c = 1; c <= cases; c++) {
        OUT2(<< "Case #" << c << ": ");
        int a,b,k,ans = 0;
        in >> a >> b >> k;
        for (int i = 0; i < a; i++) {
            for (int j = 0; j < b; j++) {
                if ( (i & j) < k) ans++;
            }
        }
        OUT2(<< ans << endl);
    }

    return 0;
}
