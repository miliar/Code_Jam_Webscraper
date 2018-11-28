#include <bits/stdc++.h>


int D;
std::vector<int> S;
std::vector<int> M;
std::vector<std::vector<int>> G;
std::vector<std::array<int, 3>> events;
std::vector<std::pair<int, int>> feasible;


void go1 ( int u ) {
    std::queue<int> q;

    q.push(u);

    while ( !q.empty() ) {
        u = q.front(); q.pop();
    
        feasible[u].first = S[u] - D;
        feasible[u].second = S[u];

        if ( u > 0 ) {
            feasible[u].first = std::max(feasible[u].first, feasible[M[u]].first);
            feasible[u].second = std::min(feasible[u].second, feasible[M[u]].second);
        }

        if ( feasible[u].first <= feasible[u].second ) {
            events.push_back({feasible[u].first, 0, u});
            events.push_back({feasible[u].second, 1, u});

            for ( auto& v : G[u] ) {
                q.push(v);
            }
        }
    }
}


int main ( void ) {

    int T;
    std::cin >> T;

    for ( int tc = 1 ; tc <= T ; ++ tc ) {
        int N;
        std::cin >> N >> D;

        G.clear();
        events.clear();

        G.resize(N);
        S.resize(N);
        M.resize(N);
        feasible.resize(N);

        long long S0, As, Cs, Rs, M0, Am, Cm, Rm;
        std::cin >> S0 >> As >> Cs >> Rs
                 >> M0 >> Am >> Cm >> Rm;

        S[0] = S0;
        M[0] = M0;
        for ( int i = 1 ; i < N ; ++ i ) {
            S[i] = (S[i-1] * As + Cs) % Rs;
            M[i] = (M[i-1] * Am + Cm) % Rm;  
            G[M[i]%i].push_back(i);
        }

        for ( int i = 1 ; i < N ; ++ i ) {
            M[i] %= i;
        }
        
        go1(0);

        std::sort(events.begin(), events.end());
        
        int answer = 0;
        std::set<int> present;


        for ( auto& evt : events ) {
            if ( evt[1] ) {
                present.erase(evt[2]);
            }
            else {
                present.insert(evt[2]);
            }
            answer = std::max(answer, (int) present.size());
        }

        std::cout << "Case #" << tc << ": " << answer << "\n";;
    }


    return 0;
}
