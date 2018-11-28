#include <iostream>
#include <cstring>

char s[110];

int main()
{
    int tc;
    std::cin >> tc;
    for(int tn = 1; tn <= tc; tn++){
        std::cin >> s;
        int ans = 0;
        char cur = '+';
        for (int p = strlen(s) - 1; p >= 0; --p){
            ans += cur != s[p];
            cur = s[p];
            }
        std::cout << "Case #" << tn << ": " << ans << std::endl;
        }
    return 0;
}
