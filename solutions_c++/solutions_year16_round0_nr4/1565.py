#include <cassert>
#include <cstdio>
#include <set>
#include <string>

uint64_t possible(uint64_t current, uint64_t N, std::set<char>& seen_digits, uint64_t remaining_depth = 10000000)
{
    if(remaining_depth == 0)
        return -1;
    
    auto current_str = std::to_string(current);
    for(auto c : current_str)
        seen_digits.insert(c);
    
    return seen_digits.size() == 10 ? current : possible(current + N, N, seen_digits, remaining_depth - 1);
}


int main(int argc, char** argv)
{
    int T;
    scanf("%d", &T);
    
    for(int t = 1; t <= T; ++t)
    {
        printf("Case #%d:", t);
        int K, C, S;
        scanf("%d %d %d", &K, &C, &S);
        
        assert(K == S);
        
        for(int i = 1; i <= S; ++i)
            printf(" %d", i);
        printf("\n");
    }
}