#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <sstream>
#include <cstdint>
#include <vector>
#include <algorithm>

#define TRACE(cmd)
//#define TRACE(cmd) cmd

typedef intmax_t Int;

struct Party {
    int count;
    char letter;
    
    bool operator<(const Party& rhs) {
        return count < rhs.count;
    }
};

std::string solve(std::vector<Party>&);

int main() {
    int T;
    std::cin >> T;
    for (int t=1; t<=T; ++t) {
        Int n;
        std::cin >> n;

        std::vector<Party> parties;
        parties.reserve(n);
        for (int l=0; l<n; ++l) {
            int c;
            std::cin >> c;
            parties.push_back(Party{c, char('A' + l)});
        }
        std::cout << "Case #" << t << ": " << solve(parties) << std::endl;
    }
    return 0;
}

std::string solve(std::vector<Party>& p) {
    std::stringstream r;
    
    std::make_heap(p.begin(), p.end());
    TRACE(std::clog << "size: " <<  p.size() << std::endl);  
    while (p.size()>1) {//< must be
        /*
        int rest = 0;
        for (int i=1; i<p.size(); ++i) {
            rest += p[i].count;
        }
        if (p[0].count > rest) {
            std::cout << "<something went wrong>" << std::endl;
            break;
        }
        //*/
        // always remove first
        std::pop_heap(p.begin(), p.end());
        
        r << p.back().letter;
        p.back().count--;
        
        // first was dominating; implicit check for 0
        if (p.back().count > p.front().count) {
            r << p.back().letter;
            p.back().count--;

            //if (p.back().count != 0) { //< must
            std::push_heap(p.begin(), p.end());
            r << " ";
            continue;
        }

        // removing 1; rest must be 1
        if (p.back().count == 0) {
            if (p.size() == 2) { // last two
                p.front().count--;
                r << p.front().letter;
                p.clear();
            } else {
                p.pop_back();
            }
        } else {
            // this might break balance, reduce!
            if (p.back().count < p.front().count) {
                std::pop_heap(p.begin(), p.end()-1);
                p[p.size()-2].count--;
                r << p[p.size()-2].letter;

                // push back this one
                std::push_heap(p.begin(), p.end() - 1);
            }

            // push back;
            std::push_heap(p.begin(), p.end());
        }
        
        r << " ";
    }

    std::string ret = r.str();
    ret.pop_back();

    return ret;
}


