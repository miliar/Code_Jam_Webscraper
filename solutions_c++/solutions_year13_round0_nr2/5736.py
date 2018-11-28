#include <iostream>
#include <set>
#include <vector>

#define forn(i,x,y) for(int i=x;i<y;i++)

using namespace std;

vector< set< pair<int,int> > > elems (101);
int grass[100][100];
int n = 0, m = 0;

bool check(int a, int b) {
    set< pair<int,int> > s = elems[grass[a][b]];
    bool v = true, h = true;
    forn(i,0,m)
        v = v && (grass[a][i] <= grass[a][b]);
    if(v) {
        forn(i,0,m) s.erase(make_pair(a,i));
        return true;
    }
    forn(i,0,n)
        h = h && (grass[i][b] <= grass[a][b]);
    if(h) {
        forn(i,0,n) s.erase(make_pair(i,b));
        return true;
    }
    return false;
}

string ans(void) {
    set< pair<int,int> >::iterator it;
    forn(se,0,101) {
        if(elems[se].empty()) continue;
        set< pair<int,int> > s = elems[se];
        bool possible = true;
        for(it = s.begin(); it != s.end(); it++)
            possible = possible && check(it->first, it->second);
        if(!possible) return "NO";
    }
    return "YES";
}

int main(void) {
    int tests; cin >> tests;
    forn(t,1,tests+1) {
        cin >> n >> m;
        forn(i,0,n) forn(j,0,m) {
            cin >> grass[i][j];
            elems[grass[i][j]].insert(make_pair(i,j));
        }
        cout << "Case #" << t << ": " << ans() << endl;
        forn(i,0,100) elems[i].clear();
    }
}
