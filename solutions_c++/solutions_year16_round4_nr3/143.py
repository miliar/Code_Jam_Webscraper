#define _USE_MATH_DEFINES
#include <cstdio>
#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <complex>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <bitset>
#include <numeric>
#include <limits>
#include <climits>
#include <cfloat>
#include <functional>
using namespace std;

const int dy[] = {1, 0, -1, 0};
const int dx[] = {0, -1, 0, 1};

vector<string> solve(int r, int c, const vector<int>& v)
{
    for(int i=0; i<(1<<(r*c)); ++i){
        bitset<16> bs(i);
        vector<string> s(r, string(c, '/'));
        for(int j=0; j<r*c; ++j){
            if(bs[j])
                s[j/c][j%c] = '\\';
        }

        bool ok = true;
        for(int j=0; j<r+c; ++j){
            vector<int> py(2), px(2), pd(2);
            for(int k=0; k<2; ++k){
                int a = v[2*j+k];
                if(a <= c){
                    py[k] = -1;
                    px[k] = a - 1;
                    pd[k] = 0;
                }
                else if(a <= r + c){
                    py[k] = (a - c) - 1;
                    px[k] = c;
                    pd[k] = 1;
                }
                else if(a <= r + c * 2){
                    py[k] = r;
                    px[k] = c - (a - r - c);
                    pd[k] = 2;
                }
                else{
                    py[k] = r - (a - r - c * 2);
                    px[k] = -1;
                    pd[k] = 3;
                }
            }

            int y = py[0];
            int x = px[0];
            int d = pd[0];
            for(;;){
                y += dy[d];
                x += dx[d];
                if(!(0 <= y && y < r && 0 <= x && x < c))
                    break;
                if(s[y][x] == '/')
                    d ^= 1;
                else
                    d ^= 3;
            }

            if(y != py[1] || x != px[1]){
                ok = false;
                break;
            }
        }

        if(ok)
            return s;
    }

    return vector<string>(1, "IMPOSSIBLE");
}

int main()
{
    int T;
    cin >> T;

    for(int t=1; t<=T; ++t){
        int r, c;
        cin >> r >> c;
        vector<int> v(2*(r+c));
        for(int i=0; i<2*(r+c); ++i)
            cin >> v[i];

        vector<string> ans = solve(r, c, v);
        cout << "Case #" << t << ":" << endl;
        for(unsigned i=0; i<ans.size(); ++i)
            cout << ans[i] << endl;
    }

    return 0;
}