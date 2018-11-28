#define OSW2

#include <iostream>
#include <functional>
#include <algorithm>
#include <utility>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>

using namespace std;

typedef long long ll;

#define UP 0
#define DN 1
#define LT 2
#define RT 3

int dx[] = {0,0,-1,1};
int dy[] = {-1,1,0,0};
int R,C;
int mp[101][101];
int used[101][101];

int main() {
#ifdef OSW
    freopen("//Users//osw//Desktop//in.txt", "r", stdin);
#endif
#ifdef OSW2
    string file_name = "A-large";
    freopen(("//Users//osw//Downloads//" + file_name + ".in").c_str(), "r", stdin);
    freopen(("//Users//osw//Downloads//" + file_name + ".out").c_str(), "w", stdout);
#endif
    
    int T, t = 0;
    cin >> T;

    while (T-(t++)) {
        cin >> R >> C;
        for (int y=0; y<R; ++y) {
            for (int x=0; x<C; ++x) {
                char ch; cin >> ch;
                int t = 8;
                if ('^'==ch) t = UP;
                if ('v'==ch) t = DN;
                if ('<'==ch) t = LT;
                if ('>'==ch) t = RT;
                mp[x][y] = t;
            }
        }

        bool imp = 0;
        int cnt = 0;
        for (int y=0; y<R; ++y) for (int x=0; x<C; ++x) {
            //cout << x << ',' << y << ' ' ;
            if (mp[x][y]==8) continue;
            int t = mp[x][y];
            int xx = x + dx[t];
            int yy = y + dy[t];
            while (xx>=0 && xx<C && yy>=0 && yy<R && mp[xx][yy]==8) {
                xx += dx[t];
                yy += dy[t];
            }

            if (xx>=0 && xx<C && yy>=0 && yy<R) continue;
            else {
                //cout << xx << ' ' << yy << endl;
                bool can = false;
                for (int k = 0; k < 4; ++k) {
                    int xx = x + dx[k];
                    int yy = y + dy[k];

                    while (xx>=0 && xx<C && yy>=0 && yy<R && mp[xx][yy]==8) {
                        xx += dx[k];
                        yy += dy[k];
                    }
                    if (xx>=0 && xx<C && yy>=0 && yy<R) {
                        ++cnt, can = true;
                        break;
                    }
                }
                if (!can) imp = true;
            }

        }


        cout << "Case #" << t << ": ";
        if (imp) cout << "IMPOSSIBLE" << endl;
        else cout << cnt << endl;
    }
}



