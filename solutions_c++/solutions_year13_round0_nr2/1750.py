#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <cmath>
#include <vector>
#include <algorithm>

#define MAX 100
#define test(a) cout << "TEST " << a << endl;
using namespace std;

void clear(int c[MAX][MAX]){
    for(int a=0; a<MAX; a++){
        for(int b=0; b<MAX; b++){
            c[a][b]=0;
        }
    }
}

bool allgood(int grid[MAX][MAX],int b,int  d,int  n,int m){
    bool problem1=false, problem2=false;
    for(int e=0; e<n; e++){
        if(e!=b){
            if(grid[b][d]<grid[e][d]){
                problem1=true;
            }
        }
    }
    for(int e=0; e<m; e++){
        if(e!=d){
            if(grid[b][d]<grid[b][e]){
                problem2=true;
            }
        }
    }
    if(problem1 && problem2){
        return false;
    }
    return true;

}

int main()
{
    ifstream fin ("input.txt");
    ofstream fout ("output.txt");
    int cases, m, n;
    int c[MAX][MAX];
    fin >> cases;
    bool good;
    for(int a=1; a<=cases; a++){
        good=true;
        clear(c);
        fin >> n >> m;
        cout << n << " " << m << endl;
        for(int b=0; b<n; b++){
            for(int d=0; d<m; d++){
                fin >> c[b][d];
            }
        }
        for(int b=0; b<n; b++){
            for(int d=0; d<m; d++){
                if(!allgood(c,b,d, n, m)){
                    good=false;
                }
            }
        }
        if(good){
            fout << "Case #"<< a <<": YES" << endl;
        }
        else {
            fout << "Case #"<< a <<": NO" << endl;
        }
    }
    return 0;
}
