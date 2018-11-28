#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int L = 1e3 + 5;
char s[L], ans[L];
int p[L];


int main()
{
    int T;
    scanf("%d", &T);
    for(int Case = 1; Case <= T; ++Case)
    {
        scanf("%s", s);
        int l = strlen(s);
        char now;
        int last, first;
        for(int i = 0; i < l; ++i)
        {
            if(i == 0) p[i] = 0, now = s[i], last = 0, first = 0;
            else
            {
                if(s[i] < now) p[i] = ++last;
                else p[i] = --first, now = s[i];
            }
        }
        
        for(int i = 0; i < l; ++i) ans[p[i] - first] = s[i];
        ans[l] = 0;
        printf("Case #%d: %s\n", Case, ans);
    }
    return 0;
}