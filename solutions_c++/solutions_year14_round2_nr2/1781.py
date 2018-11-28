#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

static auto solve = []()
{
    int A,B,K; std::cin >> A >> B >> K;
    int n=0;
    for(int a=0; a<A; ++a)
        for(int b=0; b<B; ++b)
            if((a&b)<K)
                ++n;
    return n;
};

int main()
{
    std::cin.tie(0);
    std::ios_base::sync_with_stdio(false);
    int T; std::cin >> T;
    for (int i=1; i<=T; ++i)
        std::cout << "Case #" << i << ": " << solve() << std::endl;
}
