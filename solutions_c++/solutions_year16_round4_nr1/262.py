#include <iostream>
#include <iomanip>
#include <cstring>
#include <cstdio>
#include <cassert>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <utility>

typedef long long ll;
typedef std::pair<int, int> pii;
typedef std::pair<ll, ll> pll;

int N, R, P, S;

struct hand {
    int obj;

    hand() : obj(0) {}
    hand(int _o) : obj(_o) {}

    bool operator < (const hand & r) const {
        if(obj == 1 && r.obj == 2) return true;
        if(obj == 2 && r.obj == 3) return true;
        if(obj == 3 && r.obj == 1) return true;
        return false;
    }
};

void brute() {
    assert(R + P + S == 1<<N);

    std::set<std::string> hold;

    std::string ord;
    for(int i = 0; i < P; ++i) ord += 'P';    
    for(int i = 0; i < R; ++i) ord += 'R';    
    for(int i = 0; i < S; ++i) ord += 'S';    

    do {
        // std::cout << ord << std::endl;
        std::string cpy = ord;
        bool good = true;
        while(cpy.size() > 1 && good) {
            std::string nxt = "";
            for(int i = 0; i < cpy.size(); i += 2) {
                if(cpy[i] == cpy[i + 1]) {
                    good = false;
                    break;
                } else {
                    if(cpy[i] == 'R' && cpy[i + 1] == 'S') nxt += 'R';
                    if(cpy[i] == 'R' && cpy[i + 1] == 'P') nxt += 'P';
                    if(cpy[i] == 'P' && cpy[i + 1] == 'S') nxt += 'S';
                    if(cpy[i + 1] == 'R' && cpy[i] == 'S') nxt += 'R';
                    if(cpy[i + 1] == 'R' && cpy[i] == 'P') nxt += 'P';
                    if(cpy[i + 1] == 'P' && cpy[i] == 'S') nxt += 'S';
                }
            }
            cpy = nxt;
        }
        if(good) hold.insert(ord);
    } while(std::next_permutation(ord.begin(), ord.end()));

    if(hold.size()) {
        std::cout << *(hold.begin()) << std::endl;
    } else {
        std::cout << "IMPOSSIBLE" << std::endl;
    }
}

std::string build(char start) {
    std::string res; res += start;
    while(res.size() < (1<<N)) {
        std::string nxt = "";
        for(char c : res) {
            if(c == 'R') nxt += "SR";
            if(c == 'P') nxt += "RP";
            if(c == 'S') nxt += "SP";
        }
        res = nxt;
    }
    return res;
}

std::string rec(std::string s) {
    if(s.size() == 2) {
        if(s[0] < s[1]) return s;
        else {
            std::string ret;
            ret += s[1]; ret += s[0];
            return ret;
        }
    }
    std::string sf = s.substr(0, s.size() / 2);
    std::string sb = s.substr(s.size() / 2);

    assert(sf.size() == sb.size());

    std::string frnt = rec(sf);
    std::string back = rec(sb);

    if(frnt < back) return frnt + back;
    else            return back + frnt;
}

std::string solve() {
    assert(R + P + S == 1<<N);
    
    std::string wr = build('R');
    std::string ws = build('S');
    std::string wp = build('P');

    // std::cout << wr << " " << ws << " " << wp << std::endl;

    bool g1 = true, g2 = true, g3 = true;
    int wrr = std::count(wr.begin(), wr.end(), 'R');
    int wrp = std::count(wr.begin(), wr.end(), 'P');
    int wrs = std::count(wr.begin(), wr.end(), 'S');
    int wsr = std::count(ws.begin(), ws.end(), 'R');
    int wsp = std::count(ws.begin(), ws.end(), 'P');
    int wss = std::count(ws.begin(), ws.end(), 'S');
    int wpr = std::count(wp.begin(), wp.end(), 'R');
    int wpp = std::count(wp.begin(), wp.end(), 'P');
    int wps = std::count(wp.begin(), wp.end(), 'S');

    if(wrr != R || wrp != P || wrs != S) g1 = false;
    if(wsr != R || wsp != P || wss != S) g2 = false;
    if(wpr != R || wpp != P || wps != S) g3 = false;

    if(!g1 && !g2 && !g3) 
        return "IMPOSSIBLE";

    if(g1) return rec(wr);
    if(g2) return rec(ws);
    if(g3) return rec(wp);

    // std::string r1, r2, r3;
    // if(g1) r1 = rec(wr);
    // if(g2) r2 = rec(ws);
    // if(g3) r3 = rec(wp);

    // if(g1 && g2 && g3) {
    //     if(r1 <= r2 && r1 <= r3) return r1;
    //     if(r2 <= r1 && r2 <= r3) return r2;
    //     if(r3 <= r1 && r3 <= r2) return r3;
    //     assert(false);
    // }
}

int main() {
    int CS;
    std::cin >> CS;
    // std::cout << std::fixed << std::setprecision(8);
    for(int cs = 1; cs <= CS; ++cs) {
        std::cin >> N >> R >> P >> S;

        std::cout << "Case #" << cs << ": " << solve() << std::endl;
        // brute();
    }
}
