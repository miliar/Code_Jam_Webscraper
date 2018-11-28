#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>

char s[1100];
char d[1100];

char *solve(char *src, char *srcend, char *dst){
    if (src == srcend)
        return dst;
    char a = *std::max_element(src, srcend);
    char *cur = src - 1;
    std::vector<char *> pas;
    pas.push_back(cur);
    do {
        cur = std::find(cur + 1, srcend, a);
        pas.push_back(cur);
    } while (cur < srcend);
    for (int i = 2; i < pas.size(); i++)
        *(dst++) = a;
    dst = solve(pas[0]+1, pas[1], dst);
    for (int i = 2; i < pas.size(); i++)
        dst = std::copy(pas[i-1]+1, pas[i], dst);
    return dst;
    }

int main()
{
    int tc;
    std::cin >> tc;
    for(int tn = 1; tn <= tc; tn++){
        std::cin >> s;
        *solve (s, s+strlen(s), d) = 0;
        std::cout << "Case #" << tn << ": " << d << std::endl;
        }
    return 0;
}
