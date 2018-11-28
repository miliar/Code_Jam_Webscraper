#include <algorithm>
#include <vector>
#include <map>
#include <unordered_map>
#include <cstdio>
#include <deque>

class Eaters
{
public:
    std::deque<int> eaters;
    
    Eaters(std::deque<int> eaters) : eaters(eaters)
    {
        std::sort(this->eaters.begin(), this->eaters.end());
        std::reverse(this->eaters.begin(), this->eaters.end());
    }
    
    Eaters(const Eaters& other) : eaters(other.eaters)
    {
    }
    
    bool operator<(const Eaters& other) const
    {
        if(eaters.size() == other.eaters.size())
            return std::lexicographical_compare(eaters.begin(), eaters.end(), other.eaters.begin(), other.eaters.end());
        else
            return eaters.size() < other.eaters.size();      
    }
    
    bool operator==(const Eaters& other) const
    {
        if(eaters.size() == other.eaters.size())
            return std::equal(eaters.begin(), eaters.end(), other.eaters.begin());
        else
            return false;      
    }
    
    Eaters& operator=(const Eaters& other)
    {
        if(this != &other)
            eaters = other.eaters;
        
        return *this;
    }
    
    Eaters next_state() 
    {
        Eaters new_eaters = *this;
        int sz = new_eaters.eaters.size();
        for(int i = sz - 1; i >= 0 ; --i)
            if(--new_eaters.eaters[i] == 0)
                new_eaters.eaters.pop_back();
//         printf("next_state of %s is %s\n", to_string().c_str(), new_eaters.to_string().c_str()); 
        return new_eaters;
    }
    
    std::string to_string()
    {
        std::string result = "";
        for(int i = 0; i < int(eaters.size()); ++i)
        {
            if(!result.empty())
                result += ", ";
            result += std::to_string(eaters[i]);
        }
        
        return result;
    }
};

std::map<Eaters, int> memo;

int solve(Eaters eaters, int depth = 0)
{
//     for(int _ = 0; _ < depth; _++)
//         printf("  ");
//     printf("solving %s\n", eaters.to_string().c_str()); 
    if(memo.count(eaters) == 1)
    {
//         for(int _ = 0; _ < depth; _++)
//             printf("  ");
//         printf("best is %d\n", memo[eaters]);
        return memo[eaters];
    }
    
    /// At most the score can be just eating normally
    int current_best = 1 + solve(eaters.next_state(), depth + 1);
    
    std::deque<int> new_eaters;
    
    for(int i = 0; i < int(eaters.eaters.size()); ++i)
    {
        for(int split = 1; split <= eaters.eaters[i]/2; ++split)
        {
            std::deque<int> new_state = new_eaters;
            new_state.insert(new_state.end(), eaters.eaters.begin() + i + 1, eaters.eaters.end());
            new_state.push_back(split);
            new_state.push_back(eaters.eaters[i] - split);
            int split_best = 1 + solve(Eaters(new_state), depth + 1);
//             for(int _ = 0; _ < depth; _++)
//                 printf("  ");
//             printf("split at %d of %d yields %d\n", i, split, split_best);
            current_best = std::min(current_best, split_best);
        }
        
        /// Finished spliting pos i
        new_eaters.push_back(eaters.eaters[i]);
    }
    
//     for(int _ = 0; _ < depth; _++)
//         printf("  ");
//     printf("best is %d\n", current_best);
    memo[eaters] = current_best;
    return current_best;
}

void reset()
{
    memo.clear();
    memo[Eaters(std::deque<int>())] = 0;
}

int main(int argc, char** argv)
{
    int T = 0;
    scanf("%d", &T);
    
    for(int t = 1; t <= T; ++t)
    {
        reset();
        std::deque<int> first_state;
        int D;
        scanf("%d", &D);
        
        for(int i = 0; i < D; ++i)
        {
            int Pi;
            scanf("%d", &Pi);
            first_state.push_back(Pi);
        }
        
        printf("Case #%d: %d\n", t, solve(Eaters(first_state)));
    }
}