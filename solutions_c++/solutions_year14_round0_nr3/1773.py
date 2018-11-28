#include<fstream>
#include<string>
#include<iostream>
#include<iomanip>
using namespace std;

#define MAXN 100
#define DN 8

ifstream fin("C-small-attempt3.in");
ofstream fout("C-small-attempt3.out");

int dr[DN] = {1, 1, 1, 0, -1, -1, -1, 0},
    dc[DN] = {1, 0, -1, -1, -1, 0, 1, 1};

int column, row, mine;
bool solved;
char ans[MAXN][MAXN];
bool done[MAXN][MAXN];

void print_ans() {
    int i,j;
    if (solved) {
        for (i=0; i<row; ++i) {
            for (j=0; j<column; ++j) fout<<ans[i][j];
            fout<<endl;
        }
    } else {
        fout<<"Impossible"<<endl;
    }
}

void dfs(int count, int r, int c) {
    done[r][c] = true;
    if (solved) return;

    bool ok = true;
    int change_r[DN], change_c[DN];
    int change = 0, tr, tc, i;
    for (i=0; i<DN && ok; ++i) {
        tr = r+dr[i]; tc = c+dc[i];
        if (tr<0 || tc<0 || tr>=row || tc>=column || ans[tr][tc] != '*') continue;
        ans[tr][tc] = '.';
        change_r[change] = tr;
        change_c[change] = tc;
        ++change;
    }

    if (count + change + mine == column*row) {
        solved = true;
        return;
    }

    for (i=0; i<DN && change>0 && !solved; ++i) {
        tr = r+dr[i]; tc = c+dc[i];
        
        if (tr<0 || tc<0 || tr>=row || tc>=column || done[tr][tc]) continue;
        dfs(count+change, tr, tc);
    }

    if (!solved) for (i=0; i<change; ++i) ans[change_r[i]][change_c[i]] = '*';
    done[r][c] = false;
}

int main() {
    int T,c;
    fin>>T;
    
    for (c=1; c<=T; ++c) {
        fin>>row>>column>>mine;

        solved = false;
        int i,j;
        for (i=0; i<row; ++i)
            for (j=0; j<column; ++j) {
                ans[i][j] = '*';
                done[i][j] = false;
            }

        ans[0][0] = 'c';
        if (mine+1 == column*row) solved = true;
        dfs(1, 0, 0);
        
        // output
        fout<<"Case #"<<c<<":"<<endl;
    
        print_ans();

    }
    return 0;
}
