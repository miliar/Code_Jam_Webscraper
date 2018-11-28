#include <iostream>
#include <cstring>
using namespace std;
bool used[5][5];
int r,c;
int t[5][5];
int get(int x, int y) {
    if(x < 0 || y < 0 || x >= r|| y >= c) return -1;
    return t[x][y];
}
int lol;
void f(int x, int y) {
    if(used[x][y]) return;
    ++lol;
    used[x][y] = 1;
    for(int i = 0; i < 8; ++i) {
        int ux = x;
        int uy = y;
        if(i == 0 || i == 1 || i == 2) --ux;
        if(i == 3 || i == 4 || i == 5) ++ux;
        if(i == 0 || i == 6 || i == 3) --uy;
        if(i == 2 || i == 7 || i == 5) ++uy;
        int q = get(ux, uy);
        if(q == 0) goto ohi;
    }
    for(int i = 0; i < 8; ++i) {
        int ux = x;
        int uy = y;
        if(i == 0 || i == 1 || i == 2) --ux;
        if(i == 3 || i == 4 || i == 5) ++ux;
        if(i == 0 || i == 6 || i == 3) --uy;
        if(i == 2 || i == 7 || i == 5) ++uy;
        int q = get(ux, uy);
        if(q == 1) {
            f(ux, uy);
        }
    }
    ohi:;
}
int main() {
    int t2;
    cin>>t2;
    for(int i = 0; i < t2; ++i) {
        cout<<"Case #"<<i+1<<":\n";
        int m;
        cin>>r>>c>>m;
        int cutex = 0;
        int cutey = 0;
        for(int i = 0; i < 1<<(r*c); ++i) {
            int q = i; 
            int w = 0;
            memset(t, 0, sizeof(t));
            for(int j = 0; j < r; ++j) {
                for(int k = 0; k < c; ++k) {
                    t[j][k] = q&1;
                    w += q&1;
                    q /= 2;
                    //cout<<t[j][k]<<' ';
                }
                //cout<<'\n';
            }
            //cout<<'\n'<<'\n';
            if(w != r*c-m) continue;
            if(m == r*c-1) goto ohi3;
            memset(used, 0, sizeof(used));
            for(int j = 0; j < r; ++j) {
                for(int k = 0; k < c; ++k) {
                    if(t[j][k] != 1) continue;
                    for(int i = 0; i < 8; ++i) {
                        int ux = j;
                        int uy = k;
                        if(i == 0 || i == 1 || i == 2) --ux;
                        if(i == 3 || i == 4 || i == 5) ++ux;
                        if(i == 0 || i == 6 || i == 3) --uy;
                        if(i == 2 || i == 7 || i == 5) ++uy;
                        int q = get(ux, uy);
                        if(q == 0) goto ohi;
                    }
                    lol = 0;
                    f(j, k);
                    cutex = j;
                    cutey = k;
                    if(lol == r*c-m) {
                        goto ohi3;
                    }

                    goto ohi2;
                    ohi:;
                }
            }
            ohi2:;
        }
        cout<<"Impossible\n";
        continue;
        ohi3:;
        for(int j =0; j < r; ++j) {
            for(int k = 0; k < c; ++k) {
                if(j == cutex && k == cutey) {
                    cout<<"c";
                }
                else {
                    if(t[j][k]) {
                        cout<<'.';
                    }
                    else {
                        cout<<'*';
                    }
                }
            }
            cout<<'\n';
        }
    }
}
