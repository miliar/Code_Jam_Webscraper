#include<iostream>
#include<cassert>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<cstdio>
#include<string>
#include<vector>
#include<cstdlib>
#include<iterator>
#include<ctime>
#include<map>
#include<sstream>
#include<set>
#include<cctype>
#include<queue>
#include <memory.h>

using namespace std;

#define all(c) (c).begin(), (c).end()

template<typename T> inline string intToString(T x){ostringstream q;q << x;return q.str();}
template<typename T> inline T myPow(T x, T n, T MOD){T res = 1;while (n>0) {if (n & 1) {res = 1ll*res * x % MOD;}x = 1ll*x * x % MOD;n/=2;}return res;}
template<typename T> inline T gcd(T a, T b){a=abs(a);b=abs(b);while ((a>0) && (b>0)) {if (a>b)a%=b;else b%=a;}return a+b;}


typedef unsigned long long LLong;
typedef long double LDb;

const int MOD = 1000000007;

int used[17];


int main()
{
#ifdef m0stik
    freopen("input.txt","r",stdin);
    freopen("output.txt", "w", stdout);
#else
//    freopen("river.in","r",stdin);
    //freopen("river.out","w",stdout);
#endif
    int test;
    cin >> test;
    for (int t = 0; t < test; ++t) {
        for (int i = 1; i <= 16; ++i)
            used[i] = 0;
        int x;
        cin >> x;

        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                int q;
                cin >> q;
                if (i+1==x) {
                    used[q]++;
                }
            }
        }

        
        cin >> x;
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                int q;
                cin >> q;
                if (i+1==x) {
                    used[q]++;
                }
            }
        }



        int k = 0;
        int res = 0;
        for (int i = 1; i <= 16; ++i) {
            if (used[i] == 2) {
                k++;
                res = i;
            }
        }

        cout << "Case #" << t+1 << ": ";
        if (k>1) {
            cout << "Bad magician!" << endl;
        }
        else if (k==1) {
            cout << res << endl;
        }
        else {
            cout << "Volunteer cheated!" << endl;
        }
    }

    return 0;
} 