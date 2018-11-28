#include <bits/stdc++.h>
using namespace std;

/**
int t, n;

string str[105];
vector<int> vec[105];

int top;
map<string, int> mp;

set<int> eng, fen;

int main() {

    //freopen("C-small-attempt1.in", "r", stdin);
    //freopen("data.out", "w", stdout);

    scanf("%d", &t);
    getchar();
    for(int cas = 1; cas <= t; cas ++) {
        scanf("%d", &n);
        getchar();
        top = 0;
        mp.clear();
        for(int i = 0; i < n; i ++) vec[i].clear();
        for(int i = 0; i < n; i ++) {
            getline(cin, str[i]);
            string tmp = "";
            for(int j = 0; j < str[i].size(); j ++) {
                if(str[i][j] == ' ') {
                    if(mp.find(tmp) == mp.end()) {
                        mp[tmp] = top ++;
                    }
                    vec[i].push_back(mp[tmp]);
                    tmp = "";
                }
                else tmp += str[i][j];
                if(j == str[i].size() - 1) {
                    if(mp.find(tmp) == mp.end()) {
                        mp[tmp] = top ++;
                    }
                    vec[i].push_back(mp[tmp]);
                }
            }
        }


        int res = 0;
        eng.clear();
        fen.clear();
        for(int j = 0; j < vec[0].size(); j ++) eng.insert(vec[0][j]);
        for(int j = 0; j < vec[1].size(); j ++) fen.insert(vec[1][j]);


        for(int i = 2; i < n; i ++) {
            /**
            int cnt1 = 0, cnt2 = 0;

            for(int j = 0; j < vec[i].size(); j ++) {
                if(eng.find(vec[i][j]) != eng.end()) cnt1 ++;
                if(fen.find(vec[i][j]) != fen.end()) cnt2 ++;
            }
            //cout << i << " " << cnt1 << " " << cnt2 << endl;
            if(cnt1 > cnt2) {
                for(int j = 0; j < vec[i].size(); j ++) eng.insert(vec[i][j]);
            }
            else if(cnt1 == cnt2){
                int res1 = 0, res2 = 0;
                set<int> engcpy = eng, fencpy = fen;
                for(int j = 0; j < vec[i].size(); j ++) engcpy.insert(vec[i][j]);
                for(set<int>::iterator it = engcpy.begin(); it != engcpy.end(); it ++) {
                    if(fencpy.find(*it) != fencpy.end()) res1 ++;
                }
                engcpy = eng, fencpy = fen;
                for(int j = 0; j < vec[i].size(); j ++) fencpy.insert(vec[i][j]);
                for(set<int>::iterator it = engcpy.begin(); it != engcpy.end(); it ++) {
                    if(fencpy.find(*it) != fencpy.end()) res2 ++;
                }
                if(res1 <= res2) for(int j = 0; j < vec[i].size(); j ++) eng.insert(vec[i][j]);
                else for(int j = 0; j < vec[i].size(); j ++) fen.insert(vec[i][j]);
            }
            else {
                for(int j = 0; j < vec[i].size(); j ++) fen.insert(vec[i][j]);
            }
            */
/*
int res1 = 0, res2 = 0;
set<int> engcpy = eng, fencpy = fen;
for(int j = 0; j < vec[i].size(); j ++) engcpy.insert(vec[i][j]);
for(set<int>::iterator it = engcpy.begin(); it != engcpy.end(); it ++) {
    if(fencpy.find(*it) != fencpy.end()) res1 ++;
}
engcpy = eng, fencpy = fen;
for(int j = 0; j < vec[i].size(); j ++) fencpy.insert(vec[i][j]);
for(set<int>::iterator it = engcpy.begin(); it != engcpy.end(); it ++) {
    if(fencpy.find(*it) != fencpy.end()) res2 ++;
}
if(res1 <= res2) for(int j = 0; j < vec[i].size(); j ++) eng.insert(vec[i][j]);
else for(int j = 0; j < vec[i].size(); j ++) fen.insert(vec[i][j]);
}
for(set<int>::iterator it = eng.begin(); it != eng.end(); it ++) {
if(fen.find(*it) != fen.end()) res ++;
}
*/
/**
for(int i = 0; i < (1 << (n - 2)); i ++) {
    cnt = 0;
    eng.clear();
    fen.clear();
    for(int j = 0; j < vec[0].size(); j ++) eng.insert(vec[0][j]);
    for(int j = 0; j < vec[1].size(); j ++) fen.insert(vec[1][j]);
    for(int j = 0; j < n - 2; j ++) {
        if(i >> j & 1) {
            for(int k = 0; k < vec[j + 2].size(); k ++) eng.insert(vec[j + 2][k]);
        }
        else {
            for(int k = 0; k < vec[j + 2].size(); k ++) fen.insert(vec[j + 2][k]);
        }
    }
    for(set<int>::iterator it = eng.begin(); it != eng.end(); it ++) {
        if(fen.find(*it) != fen.end()) cnt ++;
    }
    res = min(res, cnt);
}*/
/*
    printf("Case #%d: %d\n", cas, res);
}
return 0;
}*/


/**
Case #1: 1
Case #2: 4
Case #3: 3
Case #4: 8
Case #5: 974
Case #6: 988
Case #7: 984
Case #8: 996
Case #9: 979
*/

