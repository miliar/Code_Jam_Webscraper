#include <cstdio>
#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <algorithm>
#include <cmath>
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

const int dy[] = {-1, 0, 1, 0};
const int dx[] = {0, 1, 0, -1};
const string dc = "^>v<";

int solve(const vector<string>& s)
{
    int h = s.size();
    int w = s[0].size();

    int ans = 0;
    for(int y=0; y<h; ++y){
        for(int x=0; x<w; ++x){
            if(s[y][x] == '.')
                continue;
            
            int cnt = -1;
            for(int i=0; i<4; ++i){
                int y2 = y;
                int x2 = x;
                do{
                    y2 += dy[i];
                    x2 += dx[i];
                }while(0 <= y2 && y2 < h && 0 <= x2 && x2 < w && s[y2][x2] == '.');

                if(0 <= y2 && y2 < h && 0 <= x2 && x2 < w){
                    if(dc[i] == s[y][x]){
                        cnt = 0;
                        break;
                    }
                    cnt = 1;
                }
            }

            if(cnt == -1)
                return -1;
            ans += cnt;
        }
    }

    return ans;
}

int main()
{
    int n;
    cin >> n;

    for(int i=1; i<=n; ++i){
        int h, w;
        cin >> h >> w;
        vector<string> s(h);
        for(int j=0; j<h; ++j)
            cin >> s[j];

        int ans = solve(s);
        if(ans == -1)
            cout << "Case #" << i << ": IMPOSSIBLE" << endl;
        else
            cout << "Case #" << i << ": " << solve(s) << endl;
    }

    return 0;
}