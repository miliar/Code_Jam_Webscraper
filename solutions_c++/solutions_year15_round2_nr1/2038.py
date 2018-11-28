#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <unordered_set>

int swap(int x) {
    std::string s = std::to_string(x);
    return std::stoi(std::string(s.rbegin(), s.rend()));
}

int solve(int N) {
    if (N <= 10) {
        return N;
    }
    std::queue<std::vector<int> > myqueue;
    std::unordered_set<int> myset ({1,2,3,4,5,6,7,8,9,10});
    std::vector<int> ini(10, 10);
    myqueue.push(ini);
    while (true) {
        std::vector<int> tmp = myqueue.front();
        //std::cerr << "work with : " << tmp[0] << std::endl;
        tmp[0] += 1;
        tmp[1] += 1;
        //std::cerr << "add result : " << tmp[0] << std::endl;
        if (tmp[0] == N) {
            return tmp[1];
        }
        if (myset.find(tmp[0]) == myset.end()) {
            //std::cerr << "push" << std::endl;
            myqueue.push(tmp);
            myset.insert(tmp[0]);
        }

        std::vector<int> tmp2 = myqueue.front();
        tmp2[0] = swap(tmp2[0]);
        //std::cerr << "swap result : " << tmp2[0] << std::endl;
        tmp2[1] += 1;
        if (tmp2[0] == N) {
            return tmp2[1];
        }
        if (myset.find(tmp2[0]) == myset.end()) {
            //std::cerr << "push" << std::endl;
            myqueue.push(tmp2);
            myset.insert(tmp2[0]);
        }
        myqueue.pop();
        //std::cerr << "- -- --- ----- --- -- -" << std::endl;
    }
}

int main() {
    int T = 0;
    int N = 0;
    std::cin >> T;
    for (int i = 0; i < T; ++i) {
        std::cin >> N;
        std::cout << "Case #" << i + 1 << ": " << solve(N) << std::endl;
    }
    return 0;
}
