#include <bits/stdc++.h>

int N;
int am[3];

std::string dp[13][27];
std::string an[3];

std::string solve(int d, char c){
    if(!dp[d][c].empty()) return dp[d][c];
    if(d == N) return std::string(1, c);
    
    std::string a, b;
    if(c == 'P'){
        a = solve(d+1, 'P');
        b = solve(d+1, 'R');
    }else if(c == 'R'){
        a = solve(d+1, 'R');
        b = solve(d+1, 'S');
    }else if(c == 'S'){
        a = solve(d+1, 'S');
        b = solve(d+1, 'P');
    }else std::abort();

    if(a < b) return dp[d][c] = a+b;
    else return dp[d][c] = b+a;
}

void test(int t){
    am[0] = am[1] = am[2] = 0;
    for(int i=0; i<13; ++i){
        for(int j=0; j<27; ++j) dp[i][j] = "";
    }
    
    std::cin >> N >> am[0] >> am[1] >> am[2];
    
    an[0] = solve(0, 'P');
    an[1] = solve(0, 'R');
    an[2] = solve(0, 'S');
    
    for(int i=0; i<3; ++i){
        int tc[3];
        tc[0] = tc[1] = tc[2] = 0;
        for(int j=0; j<an[i].size(); ++j){
            if(an[i][j] == 'R') tc[0]++;
            else if(an[i][j] == 'P') tc[1]++;
            else if(an[i][j] == 'S') tc[2]++;
        }
        
        if(tc[0] == am[0] && tc[1] == am[1] && tc[2] == am[2]){
            std::cout << "Case #" << t << ": ";
            std::cout << an[i] << std::endl;
            return;
        }
    }
    
    std::cout << "Case #" << t << ": IMPOSSIBLE" << std::endl;
}

int main(){
    int T;
    std::cin >> T;
    for(int i=1; i<=T; ++i) test(i);
}
