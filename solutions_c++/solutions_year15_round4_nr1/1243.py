#include <iostream>

using namespace std;

int T;
int r,c;

int dx[5] = {0,-1,0,1,0};
int dy[5] = {0,0,1,0,-1};

int v[100][100];
bool valid(int x, int y) {
    if((x<0) || (x>=r)) return 0;
    if((y<0) || (y>=c)) return 0;
    return 1;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(NULL);
    cin >> T;
    for(int t=1; t<=T; t++) {
        cin >> r >> c;
        for(int i=0; i<r; i++) {
            for(int j=0; j<c; j++) {
                char cc;
                cin >> cc;
                if(cc == '.') {
                    v[i][j] = 0;
                } else if(cc=='^') {
                    v[i][j] = 1;
                } else if(cc=='>') {
                    v[i][j] = 2;
                } else if(cc=='v') {
                    v[i][j] = 3;
                } else v[i][j] = 4;
            }
        }

        int sol = 0;
        bool term = 0;;

        for(int i=0; i<r; i++) {
            for(int j=0; j<c; j++) {
                if(!v[i][j]) continue;

                bool ok[5] = {1,1,1,1,1};
                bool ook = 0;

                for(int k=1; k<=4; k++) {
                    int ii = i+dx[k];
                    int jj = j+dy[k];
                    while((valid(ii,jj)) && (!v[ii][jj])) {
                        ii += dx[k];
                        jj += dy[k];
                    }
                    if(!valid(ii,jj)) {
                        ok[k] = 0;
                    } else ook = 1;
                }

                if(!ook) term = 1;
                if(!ok[v[i][j]]) sol++;
            }
        }

        cout << "Case #" << t << ": ";
        if(term) {
            cout << "IMPOSSIBLE" << endl;
        } else cout << sol << endl;
    }

    return 0;
}
