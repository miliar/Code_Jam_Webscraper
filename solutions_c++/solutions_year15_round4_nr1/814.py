#include <bits/stdc++.h>
using namespace std;

#define mp make_pair
#define pb push_back
#define pii pair<int,int>
#define x first
#define y second

int god;
char grid[105][105];
char done[105][105] = {0};


vector<pii> points;

int dx, dy;
void find_dir(char ch){
    if (ch=='>'){
        dx = 0;
        dy = 1;
    }
    if (ch=='<'){
        dx = 0;
        dy = -1;
    }
    if (ch == 'v'){
        dx = 1;
        dy = 0;
    }
    if (ch == '^'){
        dx = -1;
        dy = 0;
    }
}
int R, C;
int main(){
    freopen("input.txt", "r", stdin);
    freopen("out1.txt", "w" ,stdout);

    scanf("%d", &god);
    for(int cc = 1; cc <=god; cc++){
        memset(done, 0, sizeof done);
        printf("Case #%d: ", cc);
        points.clear();
        scanf("%d%d", &R, &C);
        for (int i = 0; i<R; i++){
            for (int j = 0; j<C; j++){
                scanf(" %c", &grid[i][j]);


                if (grid[i][j]!='.'){
                    points.pb(mp(i,j));
                }
            }
        }
        //cout << "points = " << points.size() << endl;

        // make sure nothing is impossible
        bool poss = true;
        for (int k = 0; k<points.size(); k++){
            int r = points[k].x;
            int c = points[k].y;
            int cnt = 0;
            for (int i = 0; i<R; i++){
                if (grid[i][c]!='.' && i!=r) cnt++;
            }
            for (int i = 0; i<C; i++){
                if (grid[r][i]!='.' && i!=c) cnt++;
            }
            if (cnt == 0) poss = false;
        }
        if (!poss) {
            cout << "IMPOSSIBLE" << endl;
            continue;
        }
        int ans = 0;
        for (int k = 0; k<points.size(); k++){
            // traverse the point

            int r = points[k].x;
            int c = points[k].y;
            int sr = r;
            int sc = c;

            find_dir(grid[r][c]);

            if (done[r][c]) continue;

            queue<pii> q; // list of points encountered during run
            q.push(mp(r,c));
            set<pii> v;
            v.insert(mp(r,c));
            while(1){
                r+=dx;
                c+=dy; // traversing

                if (r<0 || r>=R || c<0 || c>=C){ // out of bounds, need to flip a switch
                    ans++;

                    //cout << "starting at " << sr << "  " << sc << ", cycle added, ending at " << r << " " << c << endl;
                    while (!q.empty()){
                        int tr = q.front().x;
                        int tc = q.front().y;
                        q.pop();
                        done[tr][tc] = true;
                        //cout << tr << " " << tc << " part of path" << endl;
                    }
                    break;
                }
                if (done[r][c] || v.count(mp(r,c))!=0){ // onto a cycle, no need to flip a switch
                    //cout << "cycle detected starting at " << sr << " " << sc << endl;
                    while (!q.empty()){
                        int tr = q.front().x;
                        int tc = q.front().y;
                        q.pop();
                        done[tr][tc] = true;
                        //cout << tr << " " << tc << " part of cycle" << endl;
                    }
                    break;
                }

                if (grid[r][c]!='.'){
                    find_dir(grid[r][c]);
                    q.push(mp(r,c));
                    v.insert(mp(r,c));
                }
            }
        }
        printf("%d\n", ans);
    }


}
