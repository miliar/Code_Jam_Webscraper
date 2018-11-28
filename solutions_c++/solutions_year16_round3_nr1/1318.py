#include <bits/stdc++.h>
using namespace std;

struct node {
    char team;
    int cnt;
    node( char _team, int _cnt ) {
        team = _team;
        cnt = _cnt;
    }
};
vector <node> v;
bool cmp( node a, node b ) {
    return a.cnt > b.cnt;
}

int main() {
    #ifdef Mahir
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif
    int t;
    cin >> t;
    for( int cs = 1; cs <= t; ++cs ) {
        v.clear();
        int n;
        cin >> n;
        for( int i = 0; i < n; ++i ) {
            int a;
            cin >> a;
            v.push_back(node( i+'A', a ));
        }
        cout << "Case #" << cs << ": ";
        while( true ) {
            sort(v.begin(), v.end(), cmp);
            if( v.size() == 2 && v[0].cnt == v[1].cnt ) {
                for( int j = v[0].cnt-1; j >=0 ; --j ) {
                    cout << v[0].team << "" << v[1].team;
                    if( j ) cout << " ";
                    else cout << endl;
                }
                break;
            }
            else {
                cout << v[0].team << " ";
                int tmp = v[0].cnt-1;
                char tmpname = v[0].team;
                reverse(v.begin(), v.end());
                v.pop_back();
                if( tmp != 0 ) {
                    v.push_back(node(tmpname, tmp));
                }
            }
        }
    }
}
