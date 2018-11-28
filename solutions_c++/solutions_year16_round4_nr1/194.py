#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>

//char ansv[5000];

void solve(int n, int p, int r, int s){
    if (n == 0){
        if (p)
            std::cout << "P";
        if (r)
            std::cout << "R";
        if (s)
            std::cout << "S";
        return;
        }
    if (p == r){
        solve(n-1, (p+1)/2, (r  )/2, (s  )/2);
        solve(n-1, (p  )/2, (r+1)/2, (s  )/2);
        }
    if (s == r){
        solve(n-1, (p  )/2, (r+1)/2, (s  )/2);
        solve(n-1, (p  )/2, (r  )/2, (s+1)/2);
        }
    if (p == s){
        solve(n-1, (p+1)/2, (r  )/2, (s  )/2);
        solve(n-1, (p  )/2, (r  )/2, (s+1)/2);
        }
    }

int main()
{
    int tc;
    std::cin >> tc;
    for(int tn = 1; tn <= tc; tn++){
        int n, p, r, s;
        std::cin >> n >> r >> p >> s;
        std::cout << "Case #" << tn << ": ";
        if (abs(p-r) > 1 || abs(s-r) > 1 || abs(s-p) > 1)
            std::cout << "IMPOSSIBLE";
        else
            solve(n, p, r, s);
        std::cout << std::endl;
        }
    return 0;
}
