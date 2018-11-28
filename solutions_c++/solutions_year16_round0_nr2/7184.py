#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

const int maxn = 100 + 5;
char s[maxn];
char t[maxn];

int main()
{
//    freopen("in.txt", "r", stdin);
//    freopen("B-large.in", "r", stdin);
//    freopen("out.out", "w", stdout);
    int T;

    cin>>T;
    int Case = 0;
    getchar();
    while (T--) {
        gets(s);
        int len = strlen(s);
        int Count = 0;
        for (int i=len-1; i>=0; --i) {
            if (s[i] == '-') {
                if (s[0] == '+') {
                    ++Count;
                    int j = 1;
                    while (s[j] == '+') {
                        s[j] = '-';
                        ++j;
                    }
                }
                ++Count;
                for (int j=0,k=i; j<=i; ++j,--k) {
                    if (s[k] == '-') {
                        t[j] = '+';
                    } else {
                        t[j] = '-';
                    }
                }
                for (int j=0; j<=i; ++j) {
                    s[j] = t[j];
                }
            }
        }
        ++Case;
        printf("Case #%d: %d\n", Case, Count);
    }
    return 0;
}



