#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>

char s[20010];
int n;
int sum;

int solve(int i, int d){
    int j = i+1;
    while(s[i]!=s[j] && j+d < n){
        j += solve(j, d+1);
        }
    sum += s[i]==s[j] ? 10 : 5;
    return j+1-i;
    }


int main()
{
    int tc;
    std::cin >> tc;
    for(int tn = 1; tn <= tc; tn++){
        std::cin >> s;
        n = strlen(s);
        sum = 0;
        for (int i = 0; i < n; i+=solve(i, 1))
            ;
        std::cout << "Case #" << tn << ": " << sum << std::endl;
        }
    return 0;
}
