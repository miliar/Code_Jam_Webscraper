//
//  main.cpp
//  CountingSheep
//
//  Created by TT on 09/04/2016.
//  Copyright © 2016 TT. All rights reserved.
//

#include <iostream>
#include <vector>
#include <sstream>
#include <iomanip>
#include <climits>
#include <cstring>
#include <algorithm>
#include <climits>
#include <queue>
#include <bitset>
#include <unordered_map>
#include <unordered_set>
#include <fstream>
#include <climits>
#include <numeric>


#define READ_FILE 1
#define MAX_BITS 32
#define INF 0x00ffffffffffffffULL
#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define REP(i, n) FOR(i, 0, n)
#define TRACE(x) cout << #x << " = " << x << endl
#define pb(x) push_back((x))
#define PBITS(x) cout << #x << " = " << bitset<MAX_BITS>((x)) << endl
#define all(s) s.begin(), s.end()

typedef long lint;
typedef long long llint;
typedef unsigned long ulint;
typedef unsigned long long ullint;

using namespace std;

typedef unsigned long long ull;

ifstream fin("A-large (1).in");
ofstream fout("A-large.out");

int acum(vector<int>& sen){
    int ret = 0;
    REP(i, sen.size()){
        ret += sen[i];
    }
    return ret;
}

bool isMajority(vector<int>& sen){
    int sum = acum(sen);
    if (sum == 0){
        return false;
    }
    REP(i, sen.size()){
        if (sen[i] / (sum * 1.0) > 0.5){
            return true;
        }
    }
    return false;
}

void fMain(int t){
    int N;
    if (READ_FILE){
        fin >> N;
    } else {
        cin >> N;
    }

    vector<int> sen;

    REP(i, N){
        int tmp;
        if (READ_FILE){
            fin >> tmp;
        } else {
            cin >> tmp;
        }

        sen.pb(tmp);
    }

    vector<pair<int, int> > res;
    int m = *min_element(all(sen));


    while(*max_element(all(sen)) != m){
        auto maxx = max_element(all(sen));
        (*maxx)--;
        res.pb(make_pair((int)(maxx-sen.begin()), -1));
        if (isMajority(sen)){
            TRACE(t);
        }
    }

    if (isMajority(sen)){
        TRACE(t);
    }

    if (m % 2 == 1){
        if (N % 2 == 0){
            for (int i=0; i<N; i+=2){
                res.pb(make_pair(i, i + 1));
                sen[i]--;
                sen[i+1]--;
                if (isMajority(sen)){
                    TRACE(t);
                }
            }
        } else {
            res.pb(make_pair(0, -1));
            sen[0]--;
            if (isMajority(sen)){
                TRACE(t);
            }
            for (int i=1; i<N; i+=2){
                res.pb(make_pair(i, i + 1));
                sen[i]--;
                sen[i+1]--;
                if (isMajority(sen)){
                    TRACE(t);
                }
            }
        }
        m--;
    }

    if (isMajority(sen)){
        TRACE(t);
    }



    string s = "";
    REP(i, m){
        REP(j, N){
            s += (char)('A' + j);
        }

    }

    for (int i=0; i<s.length(); i+=2){
        res.pb(make_pair((int)(s[i]-'A'), (int)(s[i+1]-'A')));
        sen[(int)(s[i]-'A')]--;
        sen[(int)(s[i+1]-'A')]--;
        if (isMajority(sen)){
            TRACE(t);
        }
        if (acum(sen) < 0){
            TRACE("s");
        }
    }

    if (READ_FILE){
        fout << "Case #" << t << ": ";
        REP(i, res.size()){
//            TRACE(res[i].first);
//            TRACE(res[i].second);
            fout << (char)(res[i].first + 'A');
            if (res[i].second != -1){
                fout << (char)(res[i].second + 'A');
            }
            fout << ' ';
        }
        fout << endl;

    } else {
        cout << "Case #" << t << ": ";
        REP(i, res.size()){
//            TRACE(res[i].first);
//            TRACE(res[i].second);
            cout << (char)(res[i].first + 'A');
            if (res[i].second != -1){
                cout << (char)(res[i].second + 'A');
            }
            cout << ' ';
        }
        cout << endl;
    }
}




int main(int argc, const char * argv[]) {
    int T;
    if (READ_FILE){
        fin >> T;
    } else {
        cin >> T;
    }
    for (int t = 1; t <=T; ++t){
        fMain(t);
    }
    fin.close();
    fout.flush();
    fout.close();
    return 0;
}
