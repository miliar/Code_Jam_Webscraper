#include <cstdio>
#include <set>
#include <string>
#include <vector>
#include <iostream>
#include <cassert>

void flip(std::vector<int>& things, int position)
{
    for(int i = 0; i <= position; ++i)
        things[i] = !things[i];
}

int main(int argc, char** argv)
{
    int T;
    std::cin >> T >> std::ws;
    
    for(int t = 1; t <= T; ++t)
    {
        printf("Case #%d: ", t);
        std::string pancakes_str;
        std::cin >> pancakes_str >> std::ws;
        
        std::vector<int> pancakes_vec;
        for(auto c : pancakes_str)
            pancakes_vec.push_back(c == '+');
        
        uint64_t a = 0;
        for(int i = pancakes_vec.size() - 1; i >= 0; --i)
            if(!pancakes_vec[i])
            {
                a++;
                flip(pancakes_vec, i);
            }
        printf("%llu\n", a);
        
    }
}