#!/usr/bin/env cppsh
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <set>
#include <iterator>
#include <vector>
#include <sstream>
#include <cmath>
#include <queue>

int main(int argc, char* argv[])
{
    std::string str;
    std::getline(std::cin, str);
    const int T = atoi(str.c_str());
    for (int it = 0; it < T; ++it)
    {
        int R, C, W, ans;
        std::cin >> R >> C >> W;
        ans = (R-1)*C/W;
        int M = (C-W)/W;
        ans += M;
        ans += W;
        int remainder = C - M*W;
        if (remainder % W)
            ans += 1;
        std::cout << "Case #" << (it+1) << ": " << ans << std::endl;
    }
    return 0;
}
