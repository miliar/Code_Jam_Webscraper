#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <functional>
#include <numeric>

using namespace std;

#define vi vector<int>
#define vvi vector<vector<int> >
#define all(e) e.begin(),e.end()
#define pb push_back

int main(int argc, const char *argv[]) {
    int N;
    cin >> N;
    cin.ignore();
    for(int ca=0; ca<N; ca++) {

        vector<string> b;
        for(int i=0; i<4; i++) {
            string line;
            getline(cin, line);
            b.push_back(line);
        }
        cin.ignore();

        int dx[] = {1,0,1,1};
        int dy[] = {0,1,1,-1};

        bool owin = false;
        bool xwin = false;
        bool full = true;

        for(int i=0; i<4; i++) {
            for(int j=0; j<4; j++) {
                if(b[i][j] == '.') full=false;
                for(int d=0; d<4; d++) {
                    int t = 0;
                    int x = 0;
                    int o = 0;
                    for(int k=0; k<4; k++) {
                        int ni = i+k*dy[d];
                        int nj = j+k*dx[d];
                        if(ni < 0 || ni > 3) break;
                        if(nj < 0 || nj > 3) break;
                        if(b[ni][nj] == 'T') t++;
                        if(b[ni][nj] == 'X') x++;
                        if(b[ni][nj] == 'O') o++;
                    }
                    //cout << "o="<<o<<", x="<<x<<"t="<<t << endl;
                    if(o==4 || (o==3 && t==1)) owin=true;
                    if(x==4 || (x==3 && t==1)) xwin=true;
                }
            }
        }

        string ans;
        if(xwin) {
            ans = "X won";
        } else if(owin) {
            ans = "O won";
        } else if(full) {
            ans = "Draw";
        } else {
            ans = "Game has not completed";
        }

        cout << "Case #" << (ca+1) << ": " << ans << endl;
    }
    return 0;
}

