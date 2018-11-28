//
//  main.cpp
//  CodeJam2014_DeceitfulWar
//
//  Created by Neurosion on 4/12/14.
//  Copyright (c) 2014 Neurosion Development. All rights reserved.
//

#include <fstream>
#include <set>

namespace
{
    void CONSUME_LINE(std::ifstream & f)
    {
        static char buffer[1024];
        f.getline(buffer, 1024);
    }
    
    std::set<double> get_blocks(std::ifstream & f, int count)
    {
        std::set<double> retval;
        for (int i = 0; i < count; ++i) {
            double block;
            f >> block;
            retval.insert(block);
        }
        CONSUME_LINE(f);
        return retval;
    }
    
    int get_score(std::set<double> k_blocks, std::set<double> n_blocks, bool honest)
    {
        int n_score = 0;
        auto block_count = k_blocks.size();
        for (int i = 0; i < block_count; ++i) {
            auto k_lightest = *k_blocks.begin();
            auto k_heaviest = *k_blocks.rbegin();
            auto n_lightest = *n_blocks.begin();
            auto n_heaviest = *n_blocks.rbegin();
            
            if (honest) {
                if (n_heaviest > k_heaviest) {
                    ++n_score;
                    k_blocks.erase(k_lightest);
                }
                else {
                    k_blocks.erase(k_blocks.upper_bound(n_heaviest));
                }
                n_blocks.erase(n_heaviest);
            }
            else {
                if (n_heaviest > k_lightest) {
                    ++n_score;
                    k_blocks.erase(k_lightest);
                    n_blocks.erase(n_blocks.upper_bound(k_lightest));
                }
                else {
                    k_blocks.erase(k_heaviest);
                    n_blocks.erase(n_lightest);
                }
            }
        }
    
        return n_score;
    }
}

int main(int argc, const char * argv[])
{
    std::ifstream input("/Users/neurosion/Documents/Projects/CodeJam2014_DeceitfulWar/D-large.in");
    std::ofstream output("/Users/neurosion/Documents/Projects/CodeJam2014_DeceitfulWar/large-output.dat");
    
    int test_cases;
    input >> test_cases;
    CONSUME_LINE(input);
    
    for (int i = 1; i <= test_cases; ++i) {
        int block_count;
        input >> block_count;
        CONSUME_LINE(input);
        std::set<double> n_blocks = get_blocks(input, block_count);
        std::set<double> k_blocks = get_blocks(input, block_count);
        
        int deceitful_score = get_score(k_blocks, n_blocks, false);
        int honest_score = get_score(k_blocks, n_blocks, true);
        
        output << "Case #" << i << ": " << deceitful_score << " " << honest_score << "\n";
    }

    input.close();
    output.close();
    
    return 0;
}

