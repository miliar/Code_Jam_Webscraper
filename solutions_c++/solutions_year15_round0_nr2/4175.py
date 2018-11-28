#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
#include <cassert>

//#define VERBOSE

int solve(std::vector<int> &pancakes) {
    std::sort(pancakes.begin(), pancakes.end());
    int splits = 0, min = pancakes.back();
    while (splits < min && pancakes.back()>1) {
        int v=pancakes.back();
        if (v == 9) {
            pancakes.back() = 3;
            pancakes.push_back(6);
        } else {
            pancakes.back() = v/2;
            pancakes.push_back(v-pancakes.back());
            ++splits;
        }

        std::sort(pancakes.begin(), pancakes.end());
        std::cout << "min: " << min << ", splits: " << splits << " pancakes: ";
        for (int p : pancakes) std::cout << p << ", ";
        std::cout << std::endl;
        if (pancakes.back()+splits < min) min = pancakes.back()+splits;
    }
    return min;
}

int solve_brute(std::vector<int> const &pancake_prev, int step=0) {
#ifdef VERBOSE
    for (int i=0; i<step; ++i) std::cout << " ";
    std::cout << "PANCAKES: ";
    for (int p : pancake_prev) std::cout << p << ", ";
    std::cout << std::endl;
#endif

    std::vector<int> pancakes;
    auto nonzero = std::find_if(pancake_prev.begin(), pancake_prev.end(), [](int i) { return i!=0; });
    if (nonzero == pancake_prev.end()) {
#ifdef VERBOSE
        for (int i=0; i<step; ++i) std::cout << " ";
        std::cout << "SOLVED: " << step << std::endl;
#endif
        return step;
    }
    std::copy(nonzero, pancake_prev.end(), std::back_inserter(pancakes));
    std::sort(pancakes.begin(), pancakes.end());
    int count1 = INT_MAX, count2;
    if (pancakes.back()>3) {
        // worth to try split
        /*std::vector<int> pancakes_split = pancakes;
        int v=pancakes_split.back();
        pancakes_split.back() = v/2;
        pancakes_split.push_back(v-pancakes_split.back());*/
        for (int i=2; i<=pancakes.back()/2; ++i) {
            std::vector<int> pancakes_split = pancakes;
            pancakes_split.back() = i;
            pancakes_split.push_back(pancakes.back()-i);

#ifdef VERBOSE
        std::sort(pancakes.begin(), pancakes.end());
        for (int i=0; i<step; ++i) std::cout << " ";
        std::cout << "SPLIT\n";
#endif

        int sol = solve_brute(pancakes_split, step+1);
        if (sol < count1) count1 = sol;

        }
    }
    // eat pancakes
    for (int &p : pancakes) p = p-1;
    count2 = solve_brute(pancakes, step+1);
    return std::min(count1, count2);
}

int main() {
    srand(0);
    int count;
    std::cin >> count;
    //count = 100;
    for (int i=1; i<=count; ++i) {
        int n;
        std::cin >> n;
        //n = rand()%15+1;
        assert(n>0);
        std::vector<int> pancakes;
        pancakes.reserve(n);
        //std::cerr << "Try: " << n << std::endl;
        for (int j=0; j<n; ++j) {
            int p;
            std::cin >> p;
            //p = rand()%15+1;
            assert(p>0);
            //std::cerr << p << ", ";
            pancakes.push_back(p);
        }
        //std::cerr << std::endl;
        int s1 = solve_brute(pancakes);
        /*int s2 = solve(pancakes);
        if (s1 != s2) {
            std::cout << "Solutions: " << s1 << ", " << s2 << std::endl;
            abort();
        }*/
        std::cout << "Case #" << i << ": " << s1 << std::endl;
    }
}
