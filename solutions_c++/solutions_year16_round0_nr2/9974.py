#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#define rep(i, j, k) for(int i = j; i <= k; i++)

using namespace std;

int t;

int main() 
{
	//freopen("b.in", "r", stdin); freopen("b.out", "w", stdout);
    cin >> t;
	int tt = t;
	string s;
	for (int i = 0; i < t; i++)
	{
		cin >> s;
        int len = s.length();
        int num = 0;
		num += (s[0] == '-');
        for (int i = 1; i < len; i++)
            if (s[i - 1] == '+' && s[i] == '-') num+=2;
        printf("Case #%d: %d\n", i + 1, num);
    }
    return 0;
}
