#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

typedef long long LL;
#define rep(it,s) for(__typeof((s).begin()) it=(s).begin();it!=(s).end();it++)

vector<vector<string> > m;
vector<int> id;
int x;
int r, c;

void init() {

    m.clear();
    id.clear();

    if (x == 1) {

        vector<string> v;
        v.push_back( "*" );
        m.push_back( v );
        id.push_back(0);

    }
    if (x == 2) {

        vector<string> v;
        v.push_back( "**" );
        m.push_back( v );
        id.push_back(0);

        v.clear();
        v.push_back( "*" );
        v.push_back( "*" );
        m.push_back( v );
        id.push_back(0);

    }
    if (x == 3) {

        vector<string> v;
        v.push_back( "***" );
        m.push_back( v );
        id.push_back(0);

        v.clear();
        v.push_back( "*" );
        v.push_back( "*" );
        v.push_back( "*" );
        m.push_back( v );
        id.push_back(0);

        //

        v.clear();
        v.push_back( "**" );
        v.push_back( "*" );
        m.push_back( v );
        id.push_back(1);

        v.clear();
        v.push_back( "**" );
        v.push_back( " *" );
        m.push_back( v );
        id.push_back(1);

         v.clear();
        v.push_back( " *" );
        v.push_back( "**" );
        m.push_back( v );
        id.push_back(1);

        v.clear();
        v.push_back( "*" );
        v.push_back( "**" );
        m.push_back( v );
        id.push_back(1);


    }
    if (x == 4) {

        vector<string> v;
        v.push_back( "****" );
        m.push_back( v );
        id.push_back(0);

        v.clear();
        v.push_back( "*" );
        v.push_back( "*" );
        v.push_back( "*" );
        v.push_back( "*" );
        m.push_back( v );
        id.push_back(0);

        //

        v.clear();
        v.push_back( "**" );
        v.push_back( "**" );
        m.push_back( v );
        id.push_back(1);

        //

        v.clear();
        v.push_back( "**" );
        v.push_back( "*" );
        v.push_back( "*" );
        m.push_back( v );
        id.push_back(2);

        v.clear();
        v.push_back( "***" );
        v.push_back( "  *" );
        m.push_back( v );
        id.push_back(2);

        v.clear();
        v.push_back( " *" );
        v.push_back( " *" );
        v.push_back( "**" );
        m.push_back( v );
        id.push_back(2);

        v.clear();
        v.push_back( "*" );
        v.push_back( "***" );
        m.push_back( v );
        id.push_back(2);

        //

        v.clear();
        v.push_back( "**" );
        v.push_back( " *" );
        v.push_back( " *" );
        m.push_back( v );
        id.push_back(2);

        v.clear();
        v.push_back( "***" );
        v.push_back( "*" );
        m.push_back( v );
        id.push_back(2);

        v.clear();
        v.push_back( "*" );
        v.push_back( "*" );
        v.push_back( "**" );
        m.push_back( v );
        id.push_back(2);

        v.clear();
        v.push_back( "  *" );
        v.push_back( "***" );
        m.push_back( v );
        id.push_back(2);

        //

        v.clear();
        v.push_back( "*" );
        v.push_back( "**" );
        v.push_back( "*" );
        m.push_back( v );
        id.push_back(3);

        v.clear();
        v.push_back( "***" );
        v.push_back( " *" );
        m.push_back( v );
        id.push_back(3);

        v.clear();
        v.push_back( " *" );
        v.push_back( "**" );
        v.push_back( " *" );
        m.push_back( v );
        id.push_back(3);

        v.clear();
        v.push_back( " *" );
        v.push_back( "***" );
        m.push_back( v );
        id.push_back(3);

        //

        v.clear();
        v.push_back( "*" );
        v.push_back( "**" );
        v.push_back( " *" );
        m.push_back( v );
        id.push_back(4);

        v.clear();
        v.push_back( " **" );
        v.push_back( "**" );
        m.push_back( v );
        id.push_back(4);

        v.clear();
        v.push_back( " *" );
        v.push_back( "**" );
        v.push_back( "*" );
        m.push_back( v );
        id.push_back(4);

        v.clear();
        v.push_back( "**" );
        v.push_back( " **" );
        m.push_back( v );
        id.push_back(4);

    }

}

bool found;
bool has[5][5];
int index;

bool inside(int xx, int yy) {
    if (xx<0 || xx>=r) return false;
    if (yy<0 || yy>=c) return false;

    return true;
}

void rec(int xx, int yy, int used) {

    if (yy == c) return rec(xx+1, 0, used);
    if (xx == r) {
        found |= used;
        return;
    }

    if (has[xx][yy]) return rec(xx, yy+1, used);

    for (int i=0; i<m.size(); i++) {

        //Check

        bool bad = 0;

        int dy = 0;

        for (int j=0; j<m[i][0].length(); j++) if (m[i][0][j] == '*') {
            dy = -j;
            break;
        }

        for (int k=0; k<m[i].size(); k++) {

            for (int j=0; j<m[i][k].length(); j++) if (m[i][k][j] == '*') {

                if ( inside(xx+k, yy+j+dy) && !has[xx+k][yy+j+dy]);
                else {
                    bad = 1;
                    k = 10;
                    break;
                }

            }

        }

        if (bad) continue;

        // PUT

        for (int k=0; k<m[i].size(); k++) {

            for (int j=0; j<m[i][k].length(); j++) if (m[i][k][j] == '*') {

                if ( inside(xx+k, yy+j+dy) && !has[xx+k][yy+j+dy]) {
                    has[xx+k][yy+j+dy] = 1;
                }

            }

        }

        rec(xx, yy+1, used || (index == id[i]));

        // Take out

        for (int k=0; k<m[i].size(); k++) {

            for (int j=0; j<m[i][k].length(); j++) if (m[i][k][j] == '*') {

                if ( inside(xx+k, yy+j+dy) ) {
                    has[xx+k][yy+j+dy] = 0;
                }

            }

        }

    }

}

int main() {

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int tt;
    cin>>tt;
    for (int cas=1; cas<=tt; cas++) {

        cin>>x>>r>>c;

        init();

        bool good = 1;

        for (int i=0; i<m.size(); i++) {

            found = 0;

            index = id[i];

            for (int j=0; j<r; j++) for (int k=0; k<c; k++) has[j][k] = 0;

            rec(0, 0, 0);

            good &= found;

        }

        if (!good) printf("Case #%d: RICHARD\n", cas);
        else printf("Case #%d: GABRIEL\n", cas);

    }

    return 0;

}
