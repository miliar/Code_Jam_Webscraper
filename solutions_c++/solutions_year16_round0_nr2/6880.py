#include <iostream>
#include <string>
#include <vector>
#include <stdio.h>
#include <queue>
#include <set>
#include <algorithm>
using namespace std;

int main()
{
    int test_case;
    cin>>test_case;
    int case_num = 0;
    while (test_case--) {
        case_num++;
        string s;
        cin>>s;
        int len = s.size(), i = 0, res = 0;
        for (i = 1; i < len; i++) {
            if (s[i] != s[i - 1])
                res++;
        }
        if (s[len - 1] == '-')
            res++;
        printf("Case #%d: %d\n", case_num, res);
    }
}

