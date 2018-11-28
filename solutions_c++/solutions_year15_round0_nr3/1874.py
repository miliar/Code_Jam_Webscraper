#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
using namespace std;

int trans[4][4]
= { {0, 1, 2, 3},
    {1, 0, 3, 2},
    {2, 3, 0, 1},
    {3, 2, 1, 0}};
int transSign[4][4]
= { {0, 0, 0, 0},
    {0, 1, 0, 1},
    {0, 1, 1, 0},
    {0, 0, 1, 1}};

const int MAXS = 10010;
int ans;
long long X, L, XL;
char str[MAXS];
char subs[MAXS];
int st[MAXS], sign[MAXS];
int bst[MAXS], bsign[MAXS];
bool kAppear[MAXS];

inline int ctonum(char c)
{
    switch(c)
    {
        case 'i' : return 1;
        case 'j' : return 2;
        case 'k' : return 3;
        default :  return 0;
    }
}

int main()
{
    int TC;
    scanf("%d", &TC);

    for (int tc = 1; tc <= TC; ++tc) {
        int len = 0;
        ans = 0;
        scanf("%lld%lld", &L, &X);
        XL = X*L;
        scanf("%s", subs);
        memset(kAppear, 0, sizeof(kAppear));

        for (int i = 0; i < X; ++i) {

            for (int j = 0; j < L; j++) {
                str[len] = subs[len%L];
                ++len;
            }
        }

        st[0] = ctonum(str[0]);
        sign[0] = 0;

        for (int i = 1; i < XL; ++i) {
            st[i] = trans[st[i-1]][ctonum(str[i])];
            sign[i] = sign[i-1] ^ transSign[st[i-1]][ctonum(str[i])];
        }

        bst[XL-1] = ctonum(str[XL-1]);
        bsign[XL-1] = 0;

        if (bst[XL-1] == 3 && bsign[XL-1] == 0) {
            kAppear[XL-1] = true;
        }

        for (int i = XL-2; i >= 0; --i) {            
            bst[i] = trans[ctonum(str[i])][bst[i+1]];
            bsign[i] = bsign[i+1] ^ transSign[ctonum(str[i])][bst[i+1]];

            kAppear[i] |= kAppear[i+1];
            if (bst[i] == 3 && bsign[i] == 0) {
                kAppear[i] = true;
            }
        }

        //calculation for backward function
        if (st[XL-1] == 0 && sign[XL-1] == 1) {
            for (int i = XL-2; i >= 1; --i) {
                if (bst[i] == 1 && bsign[i] == 0 && kAppear[i]) {
                    if (st[i-1] == 1 && sign[i-1] == 0) {
                        ans = 1;
                        break;
                    }
                }
            }    
        }       

        printf("Case #%d: %s\n", tc, ans ? "YES" : "NO");
    }
    return 0;
}