#include <string>
#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <cassert>


struct Partie {
    char name;
    int count;
    
    Partie(char n, int c) : name(n), count(c){}
    Partie(){}
    
    bool operator<(const Partie& o) const
    {
        return o.count < count;
    }
};
struct Tup {
    char c1;
    char c2;
    Tup(char aC1= '0', char aC2 = '0') : c1(aC1), c2(aC2) {}  
};

inline void
clearAndSort(std::vector<Partie>& ps)
{
    std::vector<Partie> result;
    result.reserve(ps.size());
    for (int i = 0; i < ps.size(); ++i) {
        if (ps[i].count == 0) {
            continue;
        }
        result.push_back(ps[i]);
    }
    
    std::sort(result.begin(), result.end());
    ps = result;
}

void
calculate(const std::vector<int>& nums, int c)
{
    std::vector<Partie> ps;
    std::vector<Tup> res;
    ps.reserve(nums.size());
    for (int i = 0; i < nums.size(); ++i) {
        ps.push_back(Partie('A' + i, nums[i]));
    }
     std::cout << "Case #" << c+1 << ": ";
    std::sort(ps.begin(), ps.end());
    while (!ps.empty()) {
        Partie& p1 = ps[0];
        Tup t;
        if (ps.size() >= 2) {            
            Partie& p2 = ps[1];
            
            int diff = p1.count - p2.count;
            assert(diff >= 0);
            if (diff > 1) {
                // only first
                p1.count--;
                t.c1 = p1.name;
            } else {
                // we need to take one of each
                t.c1 = p1.name;
                t.c2 = p2.name;
                p1.count--;
                p2.count--;     
            }
        } else {
            t.c1 = p1.name;
            p1.count--;
        }
        res.push_back(t);
        clearAndSort(ps);
    }
    
    // fix error nasty crap :p
    if (res.back().c2 == '0') {
        // swap between last and almost last
        Tup tmp = res.back();
        res.pop_back();
        res.push_back(res.back());
        res[res.size()-2] = tmp;
    }
    
    for (int i = 0; i < res.size(); ++i) {
        std::cout << res[i].c1;
        if (res[i].c2 != '0') {
            std::cout << res[i].c2;
        }
        std::cout << " ";
    }
    std::cout << "\n";
    
    
    /*std::set<Partie> ps;
    for (int i = 0; i < nums.size(); ++i) {
        ps.insert(Partie('A' + i, nums[i]));
    }
    
    std::cout << "Case #" << c+1 << ": ";
    while (!ps.empty()) {
        // calculate the step here
        auto firstIt = ps.begin();
        Partie first = *firstIt;
        if (ps.size() >= 2) {
            // check distance
            auto sndIt = ps.begin()++;
            Partie snd = *sndIt;
            int diff = first.count - snd.count;
            if (diff > 1) {
                // only first
                first.count--;
                std:: cout << first.name << " ";
                ps.erase(firstIt);
                if (first.count > 0) {
                    ps.insert(first);
                }
            } else {
                // we need to take one of each
                std::cout << first.name << snd.name << " ";
                first.count--;
                snd.count--;
                ps.erase(firstIt);
                ps.erase(sndIt);
                if (first.count > 0) {
                    ps.insert(first);
                }
                if (snd.count > 0) {
                    ps.insert(snd);
                }                
            }
        } else {
            std:: cout << first.name << " ";
            first.count--;
            ps.erase(firstIt);
            if (first.count > 0) {
                ps.insert(first);
            }
        }
    }
    std::cout << "\n";*/
}

int main(void)
{
    int T;
    std::cin >> T;
    std::vector<int> nums;
    for (int i = 0; i < T; ++i) {
        int N;
        std::cin >> N;
        nums.resize(N);
        for (int j = 0; j < N; ++j) {
            std::cin >> nums[j];
        }
        
        calculate(nums, i);
    }

    return 0;
}
