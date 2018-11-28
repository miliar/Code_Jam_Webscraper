#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <numeric>
#include <complex>

using namespace std;

typedef long long ll;

#define mp make_pair
#define pb push_back
#define PI 3.1415926535897932384626433832795
typedef pair<int, int>  pii;
typedef vector<int>     vi;
typedef vector< pii >   vpii;

#define MAXR  30
#define MAXRC 30
#define INF   100000
#define MAXN  30


int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, -1, 0, 1};
int ans[MAXR][MAXR][MAXRC];
int a[MAXN][MAXN];
int r, c, n;
int tc;

void solve(int r, int c) {
    int rc = r*c;
    int N = 1<<rc;
    memset(a, 0, sizeof(a));
    for(int i=0; i<=rc; ++i) ans[r][c][i] = INF;

    for(int m=0; m<N; ++m) {
        int t = m;
        int sum = 0;

        for(int i=1; i<=r; ++i) 
            for(int j=1; j<=c; ++j) {
                a[i][j] = t & 1;
                sum += t & 1;
                t = t >> 1;
            }

        // calc        
        int pen = 0;
        for(int i=1; i<=r; ++i) 
            for(int j=1; j<=c; ++j) if (a[i][j]) {
                for(int z=0; z<4; ++z) {
                    int i1 = i + dx[z];
                    int j1 = j + dy[z];
                    if (a[i1][j1]) pen++;
                }                
            }
        pen /= 2;
        if (pen < ans[r][c][sum]) ans[r][c][sum] = pen;
    }
}

void init() {
    for(int i=1; i<=16; ++i) {
        fprintf(stderr, "***%i\n", i);
        for(int j=i; j<=16; ++j) if (i*j <= 16) solve(i, j);
    }
}

int greed2(int r, int c, int n) {
    int res = c*(r - 1) + r*(c - 1);

    if (n <= (r*c + 1)/2) return 0;

    int n2 = r*c - n;
        //printf("n2=%i  res=%i\n", n2, res);

        // -4
    int m = ( (c-2)*(r - 2) - 1)/2;

    if (m >= n2) return res - n2*4;
    res -= m*4;
    n2  -= m;

        //printf("n2=%i res=%i\n", n2, res);
        // -3
    m = (r*c - (c-2)*(r - 2) + 1) / 2 - 1;
        int m2 = 1;

    if (r % 2 == 0 && c % 2 == 0) {
        m  = r - 2 + c - 2;
        m2 = 2;
    }

    if (r % 2 == 1 && c % 2 == 0) {
        m = r - 2 + c - 2;
        m2 = 2;
    }

    if (r % 2 == 0 && c % 2 == 1) {
        m  = r - 2 + c - 2;
        m2 = 2;
    }

    if (r % 2 == 1 && c % 2 == 1) {
        m  = r - 1 + c - 1;
        m2 = 0;
    }



        //printf("m=%i m2=%i\n", m, m2);

    if (m >= n2) return res - n2*3;
    res -= m*3;
    n2  -= m;

    if (m2 >= n2) return res - n2*2;
    res -= m2*2;
    n2  -= m2;

    return res;
}

int greed(int r, int c, int n) {
    // r <= c
    int res = c*(r - 1) + r*(c - 1);
    //
    if (r == 1) {
        res = 0;
        int z = (c + 1) / 2;
        if (z >= n) return 0;
        n -= z;
        if (c % 2 == 0) {
            n--;
            res++;
            if (n==0) return res;            
        } 
        res += n*2;
        return res;
    } 

    if (r == 2) {
        int n2 = r*c - n;
        // -3
        int m = (c - 2);
        if (m >= n2) return res - n2*3;
        res -= m*3;
        n2  -= m;
        
        // -2
        n2--;
        res -= 2;
        if (!n2) return res;

        n2--;
        res -= 2;
        if (!n2) return res;

        return res;
    }

    if (r >= 3) {
        if (n <= (r*c + 1)/2) return 0;

        int n2 = r*c - n;
        //printf("n2=%i  res=%i\n", n2, res);

        // -4
        int m = ((c-2)*(r - 2) + 1)/2;
        if (m >= n2) return res - n2*4;
        res -= m*4;
        n2  -= m;

        //printf("n2=%i res=%i\n", n2, res);
        // -3
        m = (r*c - (c-2)*(r - 2) + 1) / 2 - 1;
        int m2 = 1;

        if (r % 2 == 0 && c % 2 == 0) {
            m--;
            m2++;
        }

        if (r % 2 == 1 && c % 2 == 0) {
            m--;
            m2++;
        }

        if (r % 2 == 0 && c % 2 == 1) {
            m--;
            m2++;
        }

        if (r % 2 == 1 && c % 2 == 1) {
            m -= 3;
            m2 += 3;
        }



        //printf("m=%i m2=%i\n", m, m2);

        if (m >= n2) return res - n2*3;
        res -= m*3;
        n2  -= m;

        if (m2 >= n2) return res - n2*2;
        res -= m2*2;
        n2  -= m2;

        return res;
    }
    return 0;    
}

int go(int r, int c, int n) {
    if (r >= 3) {
        int c1 = greed(r, c, n);
        int c2 = greed2(r, c, n);
        return min(c1, c2);
    } else return greed(r, c, n);
}

void check() {
    for(int i=4; i<=16; ++i) {
        for(int j=i; j<=16; ++j) if (i*j <= 25) {
            for(int z=0; z<=i*j; ++z) {
                int c1 = ans[i][j][z];
                int c2 = go(i, j, z);
                if (c1 != c2) {
                    printf("r=%i c=%i n=%i   ok=%i  fail=%i\n", i, j, z, c1, c2);
                    return ;
                }
            }
        }
    }

}

int main() {
    init();

/*
    //solve(4, 5);
    printf("%i \n", ans[4][5][17]);
    //return 0;
    

    check();
    printf("check!\n");
    return 0;
*/
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    //solve(3, 3);
    //printf("%i\n", ans[3][3][5]);
    scanf("%i", &tc);
    for(int tt=1; tt<=tc; ++tt) {
        scanf("%i %i %i", &r, &c, &n);
        if (r > c) swap(r, c);

        if (r*c <= 16)
            printf("Case #%i: %i\n", tt, ans[r][c][n]);
        else
            printf("Case #%i: %i\n", tt, go(r, c, n) );
    }
    
    return 0;
}