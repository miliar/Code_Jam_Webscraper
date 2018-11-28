#include <iostream>
#include <vector>
#include <string>
#include <cstdio>

#define FOR(i,C) for(int i=0; i<C; i++)
#define FOR_REV(i,C) for(int i=C-1; i>=0; i--)

typedef long long ll_t;

using namespace std;

string ans(int* N, vector<vector<int> >* grid);

int main(int argc, char* argv[]){
  int T;

  cin >> T;

  // read input
  ll_t c = 0;
  while( cin ){
    if( ++c > T ) return -1;

    int N[2];
    vector<vector<int> > grid[2];

    for (int t = 0; t < 2; ++t) {
        cin >> N[t];

        for (int i = 0; i < 4; ++i) {
            vector<int> tmp;
            for (int j = 0; j < 4; ++j) {
                int card;
                cin >> card;
                tmp.push_back(card);
            }
            grid[t].push_back(tmp);
        }
    }

    // output answer
    cout << "Case #" << c << ": " << ans(N,grid) << endl;
  }
}

string ans(int* N, vector<vector<int> >* grid){
    vector<int> ret;

    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            if ( grid[0][N[0]-1][i] == grid[1][N[1]-1][j] ) {
                ret.push_back(grid[0][N[0]-1][i]);
                break;
            }
        }
    }

    if (ret.size() == 1) {
        char str[5];
        sprintf(str, "%d", ret[0]);
        return str;
    } else if (ret.size() > 1) {
        return "Bad magician!";
    } else {
        return "Volunteer cheated!";
    }
}



