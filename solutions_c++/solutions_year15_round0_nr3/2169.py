#include<iostream>
#include<algorithm>
#include<cstdlib>
using namespace std;

const int BUF = 10005;


// 1: 1
// 2: i
// 3: j
// 4: k
static int adj[5][5] = {{0, 0,  0,  0,  0},
                        {0, 1,  2,  3,  4},
                        {0, 2, -1,  4, -3},
                        {0, 3, -4, -1,  2}, 
                        {0, 4,  3, -2, -1}};


int inv(int v) {
    // 1: 1
    // 2: i
    // 3: j
    // 4: k
    if (v == 1) return 1;
    else return -v;
}


int mul(int a, int b) {
    int signSelf = a > 0 ? 1 : -1;
    int signOpp  = b > 0 ? 1 : -1;
    return adj[abs(a)][abs(b)] * signSelf * signOpp;   
}


int len;
long long nRep;
int vList[BUF];

void read() {
    cin >> len >> nRep;
    
    string str;
    cin >> str;
    
    for (int i = 0; i < str.size(); ++i) {
        if (str[i] == 'i')
            vList[i] = 2;
        else if (str[i] == 'j')
            vList[i] = 3;
        else if (str[i] == 'k')
            vList[i] = 4;
    }
}


int calc(int idx, int table[BUF]) {
    int ret = 1;
    for (int i = 0; i < (idx / len) % 4; ++i)
        ret = mul(ret, table[len - 1]);
    ret = mul(ret, table[idx % len]);
    return ret;
}


int calcRange(int l, int r, int table[BUF]) {
    return mul((l == 0 ? 1 : inv(calc(l - 1, table))), calc(r, table));
}


void work(int cases) {
    
    int table[BUF];
    table[0] = vList[0];
    for (int i = 1; i < len; ++i) {
        int signSelf = table[i - 1] > 0 ? 1 : -1;
        int signOpp  = vList[i] > 0 ? 1 : -1;
        table[i] = adj[abs(table[i - 1])][abs(vList[i])] * signSelf * signOpp;        
    }

    for (int i = 0; i < min(len * 4LL, len * nRep); ++i) {
        if (calcRange(0, i, table) != 2)
            continue;
        
        for (int j = i + 1; j < min(i + len * 4LL + 1, len * nRep); ++j) {
            if (calcRange(i + 1, j, table) == 3 && calcRange(j + 1, len * nRep - 1, table) == 4) {
                cout << "Case #" << cases << ": YES" << endl;
                return;
            }
        }
    }
    cout << "Case #" << cases << ": NO" << endl;
}


int main() {
    int cases;
    cin >> cases;
    
    for (int i = 0; i < cases; ++i) {
        read();
        work(i + 1);
    }
    return 0;
}
