#include<iostream>
#include<fstream>
#include<string>
#include<cstring>
using namespace std;

bool checkCol(int lawn[11][11], int n, int m, int j){
    for(int i = 0; i < n; ++i){
        if(lawn[i][j] != 1) return false;
    }
    return true;
}

bool checkRow(int lawn[11][11], int n, int m, int j){
    for(int i = 0; i < m; ++i){
        if(lawn[j][i] != 1) return false;
    }
    return true;
}

string check(int lawn[11][11], int n, int m){
    for(int i = 0; i < n; ++i){
        for(int j = 0; j < m; ++j){
            if(lawn[i][j] == 1){
                //cout<<i<<","<<j<<endl;
                if(!checkCol(lawn, n, m, j) && !checkRow(lawn, n, m, i))
                    return "NO";
            }
        }
    }
    return "YES";
}

int main(){
int T, n, m;    //inputs
int ch;         //lawn elements
int lawn[11][11];       //lawn
int cases = 0;

ifstream fin("B-small-attempt1.in");   //input file
ofstream fout("1.out");     //output file

fin>>T;
    while(T--){
        memset(lawn, -1, sizeof(lawn));
        fin>>n>>m;       
        for(int i = 0; i < n; ++i){
            for(int j = 0; j < m; ++j){
                fin>>ch;
                lawn[i][j] = ch;
            }
        }
        fout<<"Case #"<<++cases<<": "<<check(lawn, n, m)<<endl;
    }

    return 0;
}
