#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <numeric>
#include <string>
#include <iomanip>
#include <cstdio>

using namespace std;
typedef long long LL;

LL solve(LL N, vector<LL>& s, vector<LL>& m, LL D){
    if(N <= 1) return 1;
    vector<vector<LL> > children(N);
    for(int i = 0; i < N; i++){
        if(i > 0) children[m[i]].push_back(i);
        //cout << i<< " : " << s[i] << ", " << m[i] << endl;
    }

    set<pair<int,int> > cand;
    set<pair<int,int> > cur;
    int ans = 0;
    cand.insert(pair<int,int>(0,0));
    for(LL lower = -D; lower <= 0; lower++){
        LL upper = lower + D;
        while(!cand.empty() && cand.begin()->first <= upper){
            int id = cand.begin()->second;
            if(id==0 || cur.count(pair<int,int>(s[m[id]],m[id])) > 0) cur.insert(*cand.begin());
            cand.erase(cand.begin());
            for(int i = 0; i < children[id].size(); i++){
                cand.insert(pair<int,int>(s[children[id][i]], children[id][i]));
            }
        }
        while(!cur.empty() && cur.begin()->first < lower){
            vector<int> erase_list;
            erase_list.push_back(cur.begin()->second);
            while(!erase_list.empty()){
                int id = erase_list.back();
                erase_list.pop_back();
                if(cur.count(pair<int,int>(s[id], id)) > 0){
                    cur.erase(pair<int,int>(s[id], id));
                    for(int i = 0; i < children[id].size(); i++){
                        erase_list.push_back(children[id][i]);
                    }
                }
            }
        }
        //cerr << lower << " : " << upper << ", " << priority[left] << " : " << cur << endl;
        ans = max<int>(ans, cur.size());
    }
    return ans;
}

int main(){
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++){
        LL N, D;
        cin >> N >> D;
        LL S, as, cs, rs;
        LL M, am, cm, rm;
        cin >> S >> as >> cs >> rs;
        cin >> M >> am >> cm >> rm;
        vector<LL> s(N);
        vector<LL> m(N);
        LL S0 = S;
        for(int i = 0; i < N; i++){
            s[i] = S - S0;
            S = (S * as + cs) % rs;
            if(i > 0){
                m[i] = M % i;
            }
            M = (M * am + cm) % rm;
        }
        cout << "Case #" << t << ": " << solve(N, s, m, D) << endl;
    }
    return 0;
}

