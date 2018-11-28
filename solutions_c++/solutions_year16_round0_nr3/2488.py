#include <iostream>
#include <random>
#include <bitset>
#include <ctime>
#include <set>

using namespace std;

int64_t power(int64_t b, int64_t e) {
    if(e == 0) return (int64_t)1;
    return b * power(b, e - (int64_t)1);
}

int64_t ptest(int64_t p) {
    if(p % 2 == 0) return 2;
    for(int i = 3; (i * i) <= p && i <= 200; i += 2) {
        if(p % i == 0) return i;
    }
    return -1;
}

vector<int64_t> check(const bitset<16> &bin) {
    vector<int64_t> divs(11);
    for(int b = 2; b <= 10; b++) {
        int64_t p = 0;
        for(int i = 0; i < 16; i++) if(bin.test(i)) p += power(b, i);
        divs[b] = ptest(p);
        if(divs[b] == -1) return vector<int64_t>();
    }
    return divs;
}

void gen(bitset<16> &bin) {
    for(int i = 0; i < 16; i++) bin.set(i, rand() % 2);
    bin.set(0, true);
    bin.set(15, true);
}

int main()
{
    srand(time(NULL));
    int T, N, J;
    cin >> T >> N >> J;
    cout << "Case #1: " << endl;
    set<string> mem;
    bitset<16> bin;
    while(J > 0) {
        gen(bin);
        vector<int64_t> divs = check(bin);
        if(!divs.empty() && mem.insert(bin.to_string()).second) {
            J--;
            for(int i = 15; i >= 0; i--) cout << bin.test(i);
            for(int b = 2; b <= 10; b++) cout << " " << divs[b];
            cout << endl;
        }
    }
    /*
    bitset<6> bs("110011");
    vector<int64_t> dv = check(bs);
    for(auto i : dv) cout << i << endl;
    */
    return 0;
}
