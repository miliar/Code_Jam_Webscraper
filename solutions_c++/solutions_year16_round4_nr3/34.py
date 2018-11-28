#include <cstdio>
#include <string>
#include <algorithm>
#include <utility>
using namespace std;

int r, c;
int lover[202];
bool matched[202];
char ans[100][101];

int gety(int last) {
    if(last < c) return 0;
    else if(last < c + r) return last - c;
    else if(last < 2 * c + r) return r - 1;
    else return 2 * (c + r) - 1 - last;
}
int getx(int last) {
    if(last < c) return last;
    else if(last < c + r) return c - 1;
    else if(last < c + r + c) return 2 * c + r - 1 - last;
    else return 0;
}
int getd(int last) {
    if(last < c) return 0;
    else if(last < c + r) return 1; // c - 1;
    else if(last < c + r + c) return 2; //x = 2 * c + r - 1 - last;
    else return 3; //0;
}
int reflect(int d, char ch) {
    if(ch == '\\')
        return 3 - d;
    else
        return 1 ^ d;
}

bool solve() {
    for(int i = 0; i < r; i++)
        for(int j = 0; j <= c; j++)
            ans[i][j] = '\0';
    fill_n(matched, 2 * (r + c), false);
    for(int rep = 0; rep < r + c; rep++) {
        // find match
        int last = -1;
        for(int i = 0; i < 2 * (r + c); i++)
            if(!matched[i]) {
                if(lover[i] == last)
                    goto found;
                last = i;
            }
        for(int i = 0; i < 2 * (r + c); i++)
            if(!matched[i]) {
                if(lover[i] == last)
                    goto found;
                last = i;
            }
        // fprintf(stderr, "match not found\n");
        return false;
found:
        matched[last] = matched[lover[last]] = true;
        // fprintf(stderr, "match %d %d\n", last, lover[last]);
        int y = gety(last), x = getx(last), d = getd(last);
        int y1 = gety(lover[last]), x1 = getx(lover[last]), d1 = getd(lover[last]);
        while(y != y1 || x != x1) {
            if(ans[y][x]) {
                d = reflect(d, ans[y][x]);
            } else {
                ans[y][x] = (d & 1) ? '/' : '\\';
                d = (d + 3) % 4;
            }
            switch(d) {
                case 0: y++; break;
                case 1: x--; break;
                case 2: y--; break;
                case 3: x++; break;
            }
            if(x < 0 || y < 0 || x >= c || y >= r) {
                // fprintf(stderr, "out of bound %d %d\n", x, y);
                return false;
            }
            // fprintf(stderr, ">>>>>>>>> %d %d %d\n", x, y, d);
        }
        if(ans[y][x]) {
            d = reflect(d, ans[y][x]);
        } else {
            ans[y][x] = (d + d1 == 3) ? '/' : '\\';
            d = reflect(d, ans[y][x]);
        }
        if((d - d1) % 2) {
            // fprintf(stderr, "direction not match %d %d\n", d, d1);
            return false;
        }
    }
    for(int i = 0; i < r; i++)
        for(int j = 0; j < c; j++)
            if(!ans[i][j])
                ans[i][j] = '/';
    return true;
}

int main() {
    int t;
    scanf("%d", &t);
    for(int i = 1; i <= t; i++) {
        scanf("%d%d", &r, &c);
        for(int j = 0; j < r + c; j++) {
            int p, q;
            scanf("%d%d", &p, &q);
            p--, q--;
            lover[p] = q;
            lover[q] = p;
        }
        printf("Case #%d:\n", i);
        if(solve())
            for(int j = 0; j < r; j++)
                puts(ans[j]);
        else
            puts("IMPOSSIBLE");
    }
}

