//
// Created by e5430 on 2016/5/1.
//

#include <vector>
#include <iostream>
#include <string>
#include <c++/cstring>

using namespace std;
void print(int n, char c)
{
    for(int i =0; i < n;++i)
    {
        std::cout << c;
    }
}
void solve()
{
    string tmp;
    cin >> tmp;
    int c[26];
    memset(c, 0, sizeof(c));
    for(int i =0; i < tmp.size();++i)
    {
        c[tmp[i] -'A']++;
    }
    int x[10];
    x[0] = c['Z' -'A'];
    x[2] = c['W' -'A'];
    x[4]  = c['U' -'A'];
    x[8] = c['G' -'A'];
    x[6] = c['X' -'A'];
    x[7] = c['S' -'A'] - x[6];
    x[3] = c['R' - 'A'] - x[4] - x[0];
    x[1] = c['O' -'A'] - x[2] -x[4] - x[0];
    x[5] = c['V' -'A'] -x[7];
    x[9] = (c['N' -'A'] -x[7] -x[1]) /2;
    for(int i =0; i < 10;++i)
    {
        print(x[i], '0' + i);
    }
    std::cout << "\n";
}

int main() {
    int c;
    cin >> c;
    for(int i =0; i < c;++i)
    {
        std::cout << "Case #" << i +1 << ": ";
        solve();
    }
    return 0;
}
