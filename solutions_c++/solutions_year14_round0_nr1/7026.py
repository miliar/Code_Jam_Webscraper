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
typedef std::pair<int,int> P;
typedef std::pair<int,P> State;

const int INF = 1001001001;

// S N E W(南北東西)
const int dx[8] = {0, 0, 1, -1, 1, 1, -1, -1}, dy[8] = {1, -1, 0, 0, 1, -1, 1, -1};

int main(){
    int T;
    std::cin >> T;

    FOR(_, 1, T+1){
        int x, y;
        std::cin >> x;
        --x;

        int A[4][4], B[4][4];
        REP(i, 4){
            REP(j, 4){
                std::cin >> A[i][j];
            }
        }

        std::cin >> y;
        --y;

        REP(i, 4){
            REP(j, 4){
                std::cin >> B[i][j];
            }
        }
        
        std::vector<int> first, second, cand(4);
        REP(i, 4){
            first.push_back(A[x][i]);
            second.push_back(B[y][i]);
        }

        std::sort(first.begin(), first.end());
        std::sort(second.begin(), second.end());
        
        cand.erase(std::set_intersection(first.begin(), first.end(),
                                         second.begin(), second.end(),
                                         cand.begin()), 
                   cand.end());
        
        if(cand.empty()){
            printf("Case #%d: Volunteer cheated!\n", _);
        }else if(cand.size() == 1){
            printf("Case #%d: %d\n", _, cand[0]);
        }else{
            printf("Case #%d: Bad magician!\n", _);
        }
    }
}
