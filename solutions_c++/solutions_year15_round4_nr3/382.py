//tonynater

#include <algorithm>
#include <cstdio>
#include <cstring>
#include <fstream>
#include <iostream>
#include <set>
#include <sstream>
#include <string>
#include <vector>

#define sz(x) ((int) x.size())

using namespace std;

typedef long long ll;

const ll MOD = 1000000007;
const ll MULT = 93845;

const int INF = 1<<30;

const int MAXN = 18;
const int MAXWORDS = 3000;

int N;

vector<int> all;
vector<int> hbase_eng, hbase_fr, hsent[MAXN];
vector<int> cbase_eng, cbase_fr, csent[MAXN];

bool ENG[MAXWORDS], FR[MAXWORDS];
bool BBENG[MAXWORDS], BBFR[MAXWORDS];

int polyhash(string s) {
    ll ret = 0;
    for(int i = 0; i < sz(s); i++) {
        ret *= MULT;
        ret += s[i];
        ret %= MOD;
    }
    return ((int) ret);
}

int main() {
    freopen("/Users/tonynater/Downloads/C-small-attempt1.in", "r", stdin);
    ofstream out("/Users/tonynater/Store/Computer/Xcode_repos/Miscellaneous/GCJ_2015/R2_C/r2_c_small.out");
    
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    
    int T;
    cin >> T;
    for(int t = 0; t < T; t++) {
        cin >> N;
        all.clear();
        
        string line, word;
        getline(cin,line);
        getline(cin,line);
        stringstream sline(line);
        hbase_eng.clear();
        while(sline >> word) {
            hbase_eng.push_back(polyhash(word));
            all.push_back(polyhash(word));
        }
        getline(cin,line);
        sline = stringstream(line);
        hbase_fr.clear();
        while(sline >> word) {
            hbase_fr.push_back(polyhash(word));
            all.push_back(polyhash(word));
        }
        
        N -= 2;
        for(int i = 0; i < N; i++) {
            getline(cin,line);
            sline = stringstream(line);
            hsent[i].clear();
            while(sline >> word) {
                hsent[i].push_back(polyhash(word));
                all.push_back(polyhash(word));
            }
        }
        
        sort(all.begin(), all.end());
        cbase_eng.clear();
        for(int i = 0; i < sz(hbase_eng); i++) {
            int h = hbase_eng[i];
            cbase_eng.push_back(lower_bound(all.begin(),all.end(),h)-all.begin());
        }
        cbase_fr.clear();
        for(int i = 0; i < sz(hbase_fr); i++) {
            int h = hbase_fr[i];
            cbase_fr.push_back(lower_bound(all.begin(),all.end(),h)-all.begin());
        }
        for(int i = 0; i < N; i++) {
            csent[i].clear();
            for(int j = 0; j < sz(hsent[i]); j++) {
                int h = hsent[i][j];
                csent[i].push_back(lower_bound(all.begin(),all.end(),h)-all.begin());
            }
        }
        
        memset(BBENG,0,sizeof(BBENG));
        for(int i = 0; i < sz(cbase_eng); i++) {
            BBENG[cbase_eng[i]] = 1;
        }
        memset(BBFR,0,sizeof(BBFR));
        for(int i = 0; i < sz(cbase_fr); i++) {
            BBFR[cbase_fr[i]] = 1;
        }
        
        int res = INF;
        for(int i = 0; i < (1<<N); i++) {
            memcpy(ENG,BBENG,sizeof(ENG));
            memcpy(FR,BBFR,sizeof(FR));
            for(int j = 0; j < N; j++) {
                if((i>>j)&1) {
                    for(int k = 0; k < sz(csent[j]); k++) {
                        ENG[csent[j][k]] = 1;
                    }
                }else {
                    for(int k = 0; k < sz(csent[j]); k++) {
                        FR[csent[j][k]] = 1;
                    }
                }
            }
            
            int cres = 0;
            for(int j = 0; j < MAXWORDS; j++) {
                if(ENG[j] && FR[j]) {
                    ++cres;
                }
            }
            res = min(cres, res);
        }
        
        cout << t << '\n';
        out << "Case #" << t+1 << ": " << res << '\n';
    }
    
    return 0;
}