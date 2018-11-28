#include <iostream>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <queue>
#include <ctime>
#include <cassert>
#include <cstdio>
#include <algorithm>
#include <unordered_set>
#include <unordered_map>
#include <bitset>

using namespace std;

#define fr first
#define sc second
#define mp make_pair
#define pb push_back
#define epr(...) fprintf(stderr, __VA_ARGS__)
#define db(x) cerr << #x << " = " << x << endl
#define db2(x, y) cerr << "(" << #x << ", " << #y << ") = (" << x << ", " << y << ")\n"; 

#define equal equalll
#define less lesss
const int N = 10;
const int INF = 1e9;
const int dx[4] = {1, 0, -1, 0};
const int dy[4] = {0, 1, 0, -1};
const int P = 31;

int r, c;
long long cnt;
int b[N][N];
set < unsigned long long > q;

void read() {
    scanf("%d%d", &r, &c);

}

void print() {
    for (int i = 0; i < r; i++, cerr << endl)
        for (int j = 0; j < c; j++)
            cerr << b[i][j] << " ";
    cerr << "====================\n";
}

bool check() {
    //print();
    for (int i = 0; i < r; i++)
        for (int j = 0; j < c; j++) {
            if (b[i][j] == -1) continue;
            int mn = 0;
            int mx = 0;
            for (int k = 0; k < 4; k++) {
                int x = i + dx[k];
                int y = j + dy[k];
                y = (y + c) % c;    
                if (!(0 <= x && x < r)) continue;
                if (b[x][y] == -1) {
                    mx++;
                }
                else {
                    if (b[x][y] == b[i][j]) {
                        mn++;
                        mx++;
                    }
                }
            }
            if (!(mn <= b[i][j] && b[i][j] <= mx))
                return 0;
        }
    return 1;
}



void rec(int t)  {
    //db(t);
    int x = t / c;
    int y = t % c;
    if (x == r) {
        //print();
        //for (int j = 1; j < c; j++) {
            //for (int i = 0; i < r; i++)
                //if (b[i][0] != b[i][j]) {
                    //if (b[i][j] < b[i][0])
                        //return;
                    //else
                        //break;
                //}
        //}

        unsigned long long hash = 0;
        for (int shift = 0; shift < c; shift++) {
            unsigned long long tmp = 0;
            for (int i = 0; i < r; i++)
                for (int j = 0; j < c; j++)
                    tmp = tmp * P + b[i][(j + shift) % c];
            if (shift == 0 || tmp < hash)
                hash = tmp; 
        }
        q.insert(hash);
        return;
    }
    for (int k = 1; k <= 4; k++) {
        b[x][y] = k;
        if (check()) {
            if (1) 
                rec(t + 1);
            else {
                int x1 = x + 1;
                int y1 = y;
                if (x1 == r) {
                    x1 = 0;
                    y1++;
                }
                if (y1 == c) {
                    x1 = r;
                    y1 = 0;
                }
                rec(x1 * c + y1);
            }
        }
    }
    b[x][y] = -1;
}

void solve() {
    //cnt = 0;
    memset(b, -1, sizeof(b));
    q.clear();
    rec(0);
    cout << q.size() << "\n"; 
    //int old = cnt;
   //int rstupid() << endl;
    //int nw = stupid();
    //db2(old, nw);
    //assert(old == stupid());

}

void printAns() {
}

void stress() {

}


int main(){
#ifdef DEBUG
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
#endif
    if (1) {
        int k = 1;
        scanf("%d", &k);
        for (int tt = 0; tt < k; tt++) {
            printf("Case #%d: ", tt + 1);
            read();
            solve();
            printAns();
        }
    }
    else {
        stress();
    }

    return 0;
}

