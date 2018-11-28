#include <set>
#include <map>
#include <string>
#include <sstream>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
#define ABS(a) (a) < 0 ? -(a) : (a)

int inter(set<int>& l, set<int>& r){
    int cnt = 0;
    for(set<int>::iterator i = l.begin(); i != l.end(); ++i){
        if(r.find(*i) != r.end())
            cnt += 1;
    }
    return cnt;
}

int main()
{
    int T;
    string line, w;
    getline(cin, line);
    T = atoi(line.c_str());
    for(int tcase=1; tcase<=T; ++tcase){
        int gid = 1;
        map<string, int> ids;
        set<int> egt, pgt;
        getline(cin, line);
        //printf("%s\n", line.c_str());
        int N = atoi(line.c_str());
        {
            getline(cin, line);
            istringstream is(line);
            while(is >> w) {
                int id = ids[w];
                if(id == 0) {ids[w] = gid; id = gid; gid += 1;};
                egt.insert(id);
            }
        }
        {
            getline(cin, line);
            istringstream is(line);
            while(is >> w) {
                int id = ids[w];
                if(id == 0) {ids[w] = gid; id = gid; gid += 1;};
                pgt.insert(id);
            }
        }
        N -= 2;
        fprintf(stderr, "T%d %d\n", tcase, N);
        if(N < 1){
            printf("Case #%d: %d\n", tcase, inter(egt, pgt));
            continue;
        }
        set<int> sents[21];
        for(int n=0; n < N; ++n){
            getline(cin, line);
            istringstream is(line);
            while(is >> w) {
                int id = ids[w];
                if(id == 0) {ids[w] = gid; id = gid; gid += 1;};
                sents[n].insert(id);
            }
        }
        fprintf(stderr, "gid %d\n", gid);
        int ans = 987654321;
        for(int ser=0; ser < (1 << N); ++ser){
            int eset[2200]; memset(eset, 0, sizeof(eset));
            int pset[2200]; memset(pset, 0, sizeof(pset));
            for(auto& e : egt) eset[e] = 1;
            for(auto& p : pgt) pset[p] = 1;
            for(int i=0; i < N; ++i){
                const set<int>& s = sents[i];
                if(ser & (1<<i)){
                    for(const auto& w : s) eset[w] = 1;
                }else{
                    for(const auto& w : s) pset[w] = 1;
                }
            }
            int ii = 0;
            for(int i=0; i < 2200; ++i){
                if(eset[i]&pset[i]) ii += 1;
            }
            ans = min(ans, ii);
        }
        printf("Case #%d: %d\n", tcase, ans);
    }
    return 0;
}
