#include <fstream>

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

const int nmax= 100;

int v[nmax+1][nmax+1];

int n, m;

bool f(int x, int y){
    int cnt= 0;
    for (int i= 1; i<=n; ++i){
        if (v[i][y]<=v[x][y]){
            ++cnt;
        }
    }
    if (cnt==n){
        return 1;
    }
    cnt= 0;
    for (int i= 1; i<=m; ++i){
        if (v[x][i]<=v[x][y]){
            ++cnt;
        }
    }
    if (cnt==m){
        return 1;
    }else{
        return 0;
    }
}

void check(){
    for (int i= 1; i<=n; ++i){
        for (int j= 1; j<=m; ++j){
            if (f(i, j)==0){
                fout<<"NO\n";
                return;
            }
        }
    }
    fout<<"YES\n";
}

int main(){
    int nt;
    fin>>nt;
    for (int ct= 1; ct<=nt; ++ct){
        fin>>n>>m;
        for (int i= 1; i<=n; ++i){
            for (int j= 1; j<=m; ++j){
                fin>>v[i][j];
            }
        }

        fout<<"Case #"<<ct<<": ";
        check();        
    }

    return 0;
}
