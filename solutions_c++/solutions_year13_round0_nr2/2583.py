#include <algorithm>
#include <numeric>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <complex>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef set<int> se;
typedef pair<int,int> pii;
typedef long long int tint;

#define forsn(i,s,n) for(int i = (int)(s); i<((int)n); i++)
#define dforsn(i,s,n) for(int i = (int)(n)-1; i>=((int)s); i--)
#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define decl(v, c) typeof(c) v = c
#define forall(i, c) for(decl(i, c.begin()); i!=c.end(); ++i)
#define rall(c) (c).rbegin(), (c).rend()
#define all(c) (c).begin(), (c).end()
#define D(a) << #a << "=" << a << " "


#define si(a) int((a).size())
#define pb push_back
#define mp make_pair

int T[100][100];
int n,m;
int max_col[100];
int max_row[100];





int main () {
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);

    int t;

    cin >> t;

    //cout << t << endl;
    //forn(caso,5) {
    forn(caso,t) {

        cin >> n >> m;

        forn(i,n) forn(j,m) cin >> T[i][j];

        forn(i,n) max_row[i] = 0;
        forn(j,m) max_col[j] = 0;

        forn(i,n) forn(j,m) {
            max_row[i] = max (max_row[i],T[i][j]);
            max_col[j] = max(max_col[j],T[i][j]);
        }

        string res = "YES";

        forn(i,n) forn(j,m) if (T[i][j] < max_row[i] && T[i][j]< max_col[j]) res = "NO";


        cout << "Case #"<<caso+1<<": "<<res<<endl;


    }


  return 0;

}


