#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <set>

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REP(i,j) FOR(i,0,j)
#define mp std::make_pair

typedef long long ll;
typedef unsigned long long ull;
typedef std::pair<char,int> P;

const int INF = 1001001001;

// S N E W(南北東西)
const int dx[8] = {0, 0, 1, -1, 1, 1, -1, -1}, dy[8] = {1, -1, 0, 0, 1, -1, 1, -1};

int N;
std::vector<P> ss[100];

int can(){
    int res = 0;
    REP(i, N){
        FOR(j, i+1, N){
            if(ss[i].size() != ss[j].size()){return -1;}
            REP(k, (int)ss[i].size()){
                P lp = ss[i][k], rp = ss[j][k];
                if(lp.first != rp.first){return -1;}
                res += std::abs(lp.second-rp.second);
            }
        }
    }
    return res;
}

int main(){
    int T;
    std::cin >> T;
    FOR(_, 1, T+1){
        std::cin >> N;

        REP(i, N){
            ss[i].clear();
        }

        REP(i, N){
            std::string s;
            std::cin >> s;

            char length = 1;
            REP(j, (int)s.size()){
                if(j+1 == (int)s.size() || s[j] != s[j+1]){
                    ss[i].push_back(mp(s[j], length));
                    length = 1;
                }else{
                    length += 1;
                }
            }

            // REP(j, (int)ss[i].size()){
            //     printf("%c, %d\n", ss[i][j].first, ss[i][j].second);
            // }
        }

        int res = can();
        if(res != -1){
            printf("Case #%d: %d\n", _, res);
        }else{
            printf("Case #%d: Fegla Won\n", _);
        }
    }
}
