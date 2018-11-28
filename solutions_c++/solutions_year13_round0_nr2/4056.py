//GCJ LawnMower

#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <stdio.h>
#include <map>
#include <queue>
#include <utility>
#include <set>
#include <iterator>

using namespace std;

int lawn[100][100];
int current_rows[100];
int current_cols[100];
int N, M;
//need priority_queue
typedef pair<int,int> pii;
map<int, vector<pii> > lawn_map;
typedef vector<pii>::iterator iter_v;
typedef set<int>::iterator iter_s;

bool is_good_row(int lawn[100][100], int current_cols[100], int l)
{
    int i = 0;
    while(current_cols[i] == 0 && i < M) ++i; // make sure there are good cols
    if (i < M ) {int val = lawn[l][i];
        for(; i < M; ++i) {
            if (current_cols[i] == 1) if (lawn[l][i] != val) return false;
        }
    }
    return true;
}

bool is_good_col(int lawn[100][100], int current_rows[100], int l)
{
    int i = 0;
    while(current_rows[i] == 0 && i < N) ++i; // make sure there are good cols
    if (i < N ) {int val = lawn[i][l];
        for(; i < N; ++i) {
            if (current_rows[i]  == 1) if (lawn[i][l] != val) return false;
        }
    }
    return true;
}

bool test_lawn(int lawn[100][100])
{
    int r = N, c = M;
    while(r > 0 && c > 0) {
        //cout << r << ' ' << c << endl;
        if (r == 1 || c == 1) return true;
        vector<pii> &v = lawn_map.begin()->second;
        //cout << lawn_map.begin()->first << endl;

        if (v.empty()) { lawn_map.erase(lawn_map.begin()); }
        else {
            set<int> rows;
            set<int> cols;
            for(iter_v it = v.begin(); it != v.end(); ++it) {
                //cout << it->first << ' ';
                rows.insert(it->first);
                //cout << it->second << ' ';
                cols.insert(it->second);}
            bool test = false;
            iter_s it = rows.begin();
            while (!test && it != rows.end()) {
                //cout << *it << endl;
                if(is_good_row(lawn, current_cols, *it)) {// found a good row
                    int a = *it;
                    current_rows[a] = 0;
                    --r;
                    int i = 0;
                    while(i != v.size()) {
                        if(v[i].first == a) { v.erase(v.begin() + i); }
                        else ++i;
                    }
                    //cout << a << "row" << endl;
                    test = true;
                } else ++it;
            }
            it = cols.begin();
            while(!test && it != cols.end()) {
                //cout << *it << endl;
                if (is_good_col(lawn, current_rows, *it)) {//found a good column
                    int a = *it;
                    //cout << a << endl;
                    current_cols[a] = 0;
                    --c;
                    //cout << a << "one" << endl;
                    int i = 0;
                    while(i != v.size()) {
                        if(v[i].second == a) { v.erase(v.begin() + i); }
                        else ++i;
                    }
                    //cout << a << "two" << endl;
                    //cout << a <<  "col" << endl;
                    test = true;
                } else ++it;
            }
            // either test == true -> found a good line,
            // or no good line exists in which case return false
            if(!test) return false;
        }
    }
}


int main()
{
    freopen ("B-large.in", "r", stdin);
    freopen ("B-large.out", "w", stdout);
    int T,a;
    scanf("%d", &T); //cout << T << endl;
    for(int t = 1; t <= T; t++) {
        lawn_map.clear();
        scanf("%d %d", &N, &M);
        for(int i = 0; i < N; ++i) {
        for(int j = 0; j < M; ++j) {
            scanf("%d", &a);
            lawn[i][j] = a;
            lawn_map[a].push_back(make_pair(i,j));
        }
        }
        // show lawn  - WORKS
        /*
        cout << N << ' ' << M << endl;
        for(int i = 0; i < N; i++) {
        for(int j = 0; j < M; j++) cout << lawn[i][j] << ' '; cout << endl; } */
        //show map - WORKS
        /*

        for(map<int, vector<pii> >::iterator miit = lawn_map.begin();
                    miit != lawn_map.end(); ++miit)
            {cout << miit->first << ' ';
            for(iter_v viit = (miit->second).begin();
                        viit != (miit->second).end(); ++viit)
                        cout << viit->first << ":" << viit->second << ' ';
            cout << endl;
            }
        */

        for(int i = 0; i < N; ++i) current_rows[i] = 1;
        for(int j = 0; j < M; ++j) current_cols[j] = 1;
        bool result = test_lawn(lawn);
        if (result) printf("Case #%d: YES\n", t);
        else printf("Case #%d: NO\n", t);
    }

    return 0;
}


