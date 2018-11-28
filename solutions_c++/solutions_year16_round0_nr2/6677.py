#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <stack>
#include <cctype>
#include <vector>
#include <cmath>

using namespace std;

typedef long long ll;
const double pi = 4*atan(1);
int gcd(int a, int b)   {return b == 0? a:gcd(b,a%b);}
int lcm(int a, int b)   {return a/gcd(a,b)*b;}


int main()
{
    int T;
    cin >> T;
    for(int cas = 1; cas <= T; ++cas) {
        string input;
        cin >> input; 
        int len = input.length();
        char last = input[0];
        int cnt = 0;
        for(int i = 1; i < len; ++i) {
            if (input[i] == last) 
                continue;
            ++cnt;
            last = input[i];
        }
        if (last == '-')
            ++cnt;
        printf("Case #%d: %d\n", cas, cnt);
    }
    return 0;
}
