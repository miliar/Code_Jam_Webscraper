#include <bits/stdc++.h>


struct max_flow {
    std::vector<bool> seen;
    std::vector<std::set<int>> C;
    
    max_flow ( void ) {}
    max_flow ( int n ) : C(n) , seen(n) {}

    void add_edge ( int fr , int to , int c ) {
        C[fr].insert(to);
    }

    bool find_path ( int fr , int to ) {
        seen[fr] = true;
        if ( fr == to ) {
            return true;
        }

        for ( auto it = C[fr].begin() ; it != C[fr].end() ; ++ it ) {
            if ( !seen[*it] && find_path(*it, to) ) {
                //std::cerr << fr << "->" << (*it) << std::endl;
                C[*it].insert(fr);
                C[fr].erase(it); 
                return true;
            }
        }

        return false;
    }

    int get_max_flow ( int fr , int to ) {
        int flow;
        
        flow = 0;
        while ( find_path(fr, to) ) {
            ++ flow;
            seen.assign(seen.size(), false);
            //std::cerr << std::endl;
        }

        return flow;
    }
};


std::map<std::string, int> word_id;

int get_id ( const std::string& s ) {
    if ( word_id.count(s) ) {
        return word_id[s];
    }
    return word_id[s] = word_id.size() - 1;
}

void read_words ( std::vector<int>& v ) {
    std::string line;

    std::getline(std::cin, line);
    std::stringstream ssin(line);

    while ( ssin >> line ) {
        v.push_back(get_id(line));
    }
}

int main ( void ) {

    max_flow mf;
    std::string line;
    int T, N, t, i;
    std::vector<std::vector<int>> words_at;

    std::getline(std::cin, line);
    std::stringstream ssinT(line);
    ssinT >> T;

    for ( t = 1 ; t <= T ; ++ t ) {
        std::getline(std::cin, line);
        std::stringstream ssinN(line);
        ssinN >> N;

        word_id.clear();
        words_at.assign(N, std::vector<int>());
        for ( i = 0 ; i < N ; ++ i ) {
            read_words(words_at[i]);
            //std::cerr << i << ": ";
//            for ( auto& j : words_at[i] ) {
                //std::cerr << j << " ";
//            }
            //std::cerr << std::endl;
        }
        
        mf = max_flow(N + 2 * word_id.size());

        i = 0;
        for ( auto it = word_id.begin() ; i < word_id.size() ; ++ i , ++ it) {
            mf.add_edge(N + 2*i, N + 2*i+1, 1);
            //std::cerr << N + 2*(it->second) << " " << N + 2*(it->second) + 1 << " " << (it->first) << std::endl;
        }

        for ( i = 0 ; i < N ; ++ i ) {
            for ( auto& j : words_at[i] ) {
                mf.add_edge(i, 2*j + N, 1);
                //std::cerr << i << " " << N + 2*j << std::endl;
                mf.add_edge(2*j + N + 1, i, 1);
                //std::cerr << N + 2*j + 1 << " " << i << std::endl;
            }
        }

        std::cout << "Case #" << t << ": " << mf.get_max_flow(0, 1) << "\n";
    }


    return 0;
}
