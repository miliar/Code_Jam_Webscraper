#include <iostream>
#include <string>
#include <vector>
#include <cassert>


#define LL int64_t


std::string f(std::string s, int c)
{
    std::string gg(s.size(), 'G');
    std::string cur = s;
    for (int i = 1; i < c; ++i) {
        std::string next;
        for (int j = 0; j < cur.size(); ++j) {
            if (cur[j] == 'L') {
                next += s;
            } else {
                next += gg;
            }
        }
        cur = next;
    }
    return cur;
}

void gen(int k, int c)
{
    std::vector<bool> wasL;
    std::string s(k, '?');
    
    std::vector<std::string> v;
    for (int i = 0; i < (1 << k); ++i) {
        for (int j = 0; j < k; ++j) {
            s[k - j - 1] = (i & (1 << j)) ? 'L' : 'G';
        }
        auto r = f(s, c);
        //std::cout << r << "\n";
        if (wasL.empty()) {
            wasL.resize(r.size(), false);
            v.resize(r.size(), "");
        }
        if (i + 1 == (1 << k)) continue;
        for (size_t j = 0; j < r.size(); ++j) {
            if (r[j] == 'L') wasL[j] = true;
        }
        for (size_t j = 0; j < r.size(); ++j) {
            v[j].push_back(r[j]);
        }
    }
    for (size_t i = 0; i < wasL.size(); ++i) {
        std::cout << (wasL[i] ? '-' : '+');
    }
    std::cout << "\n";
    for (size_t i = 0; i < wasL.size(); ++i) {
        if (!wasL[i]) {
            std::cout << i << "\n";
            break;
        }
    }
    for (size_t i = wasL.size(); i -- > 0 ;) {
        if (!wasL[i]) {
            std::cout << wasL.size() - 1 - i << "\n";
            break;
        }
    }
    
    for (size_t i = 0; i < v.size(); ++i) {
        for (size_t j = i + 1; j < v.size(); ++j) {
            bool ok = true;
            for (size_t q = 0; q < v[i].size(); ++q) {
                if (v[i][q] == 'L' && v[j][q] == 'L') {
                    ok = false;
                    break;
                }
            }
            if (ok) {
                std::cout << i << " " << j << "\n";
            }
        }
    }
}

int oeis(int n) { return 0; }

// 1 2 5 27 194 1865 ...

LL myp(LL a, int b)
{
    LL res = 1;
    for (int i = 1; i <= b; ++i) {
        res *= a;
    }
    return res;
}

std::vector<LL> solve(int k, int c, int s)
{
    std::vector<LL> result;
    if (c == 1) {
        if (s >= k) {
            for (int i = 1; i <= k; ++i) {
                result.push_back(i);
            }
        }
    } else {
        
    }
    return result;
}

std::vector<LL> solveSmall(int k, int c, int s)
{
    assert(k == s);
    std::vector<LL> result;
    LL kc = myp(k, c - 1);
    for (int i = 1; i <= k; ++i) {
        result.push_back(kc * i);
    }
    return result;
}

int main()
{
    
    int T, k, c, s;
    std::cin >> T;
    for (int t = 1; t <= T; ++t) {
        std::cin >> k >> c >> s;
        std::cout << "Case #" << t << ":";
        for (auto v : solveSmall(k,c,s)) {
            std::cout << " " << v;
        }
        std::cout << "\n";
    }
    
    return 0;
}