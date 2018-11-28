#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string.h> 
#include <sstream>
#include <set>
#include <map>
using namespace std; 

typedef long long llong; 

int N; 
int M; 
int info[1001][3];

const llong mod = 1000002013L; 

struct rec {
   int from; 
   llong cnt; 
};

vector<int> stations; 
set<int> exist; 
map<int,int> cnt[2]; 
vector<rec> pre;



/*bool cmp(rec a, rec b) {
    if (a.from < b.from) {
        return true; 
    }
    return false; 
}*/

void insert(int st, llong p) {
    bool ext = false; 
    for (int i = 0; i < pre.size(); i++) {
        if (pre[i].from == st) {
            ext = true; 
            pre[i].cnt += p; 
            break; 
        }
    }    
    if (!ext) {
        rec r; 
        r.from = st;
        r.cnt = p; 
        pre.push_back(r); 
    }
    //sort(pre.begin(), pre.end(), cmp);
}

llong cal_cost(int from, int to) {
    llong num = to - from; 
    llong a = N; 
    llong b = N-num+1; 
    return (a+b)*num/2; 
}

llong delete_1(int st, llong p) {
    
    llong ret = 0; 
    for (int i = pre.size()-1; i >= 0; i--) {
        llong minus = p;
        if (pre[i].cnt < p) {
            minus = pre[i].cnt;
        }
        pre[i].cnt -= minus; 
        p -= minus;
        ret += minus * cal_cost(pre[i].from, st);  
        //cout << "yes" << pre[i].from << " " << st << " " << minus << endl; 
        if (p == 0) {
            break; 
        }
    }
    
    return ret; 
    
}

llong cal(int st) {
    int in = cnt[0][st]; 
    int out = cnt[1][st];
    
    llong ret = 0; 
    if (in > out) {
        int p = in - out; 
        insert(st, p); 
    }
    else if (in < out) {
        int p = out - in; 
        ret += delete_1(st, p); 
    }
    
    return ret; 
}

void solve(int cas) {
    stations.clear(); 
    exist.clear(); 
    cnt[0].clear();
    cnt[1].clear();   
    
    
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < 2; j++) {
            //cout << i << " " << info[i][j] << endl; 
            
            if (exist.find(info[i][j]) == exist.end()) {
                exist.insert(info[i][j]);
                stations.push_back(info[i][j]);  
            }
            if (cnt[j].find(info[i][j]) == cnt[j].end()) {
                cnt[j][info[i][j]] = info[i][2];
            }
            else {
                int tmp = cnt[j][info[i][j]]; 
                tmp += info[i][2]; 
                cnt[j][info[i][j]] = tmp; 
            }
        }
    } 
    
    sort(stations.begin(), stations.end());
    
    /*for (int i = 0; i < stations.size(); i++) {
        cout << stations[i] << endl; 
    }*/
    llong ret = 0; 
    
    pre.clear();  
    for (int i = 0; i < stations.size(); i++) {
        int st = stations[i]; 
        llong c = cal(st); 
        ret += c; 
        
        //cout << st << " " << c << endl; 
    }
    
    llong total = 0; 
    
    for (int i = 0; i < M; i++) {
        total += cal_cost(info[i][0], info[i][1]) * info[i][2]; 
    }
    //cout << "total = " << total << endl; 
    ret = (total - ret) % mod; 
    cout << "Case #" << cas << ": " << ret << endl; 
}

int main() {
    int T;
    cin >> T; 
    for (int t = 0; t < T; t++) {
        cin >> N >> M; 
        for (int i = 0; i < M; i++) {
            cin >> info[i][0] >> info[i][1] >> info[i][2];  
        }        
        solve(t+1); 
    }
    return 0; 
}
