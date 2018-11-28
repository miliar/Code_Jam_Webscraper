#include <algorithm>
#include <functional>
#include <numeric>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <complex>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <sstream>

using namespace std;

#define LL long long
#define LD long double
#define ULL unsigned long long

#define Min(a,b) a=min(a,b)
#define Max(a,b) a=max(a,b)
#define Sz(s) int((s).size())
#define All(s) (s).begin(),(s).end()
#define Fill(s,v) memset(s,v,sizeof(s))

#define ROW 1
#define COL 2
#define CHECK 3

int R, C, M;
char grid [50][50];
bool solution_found;

void print_solution(){
    for(int i =0;i<R;i++){
        for(int j=0;j<C;j++){
            cout<<grid[i][j];
        }
        cout<<endl;
    }

}

void special_case(int r, int c, int m, int flag, int prev_flag){
    if(c==2||r==2) return;
    m = -2;

    for(int i = r;i<R;i++){
            for(int j=0;j<C;j++){
                grid[i][j] = '*';
            }
        }

    for(int i = c;i<C;i++){
        for(int j=0;j<R;j++){
            grid[j][i] = '*';
        }
    }

    int k;

    if(prev_flag==ROW){
        for(int i = 0;i>m;i--){
            grid[r][-i] = '.';
        }

        for(k = 0;k<C;k++){
            if(grid[r-1][k]=='.') continue;
        }
        grid[r-1][k-1] = '*';
    } else {
        for(int i = 0;i>m;i--){
            grid[-i][c] = '.';
        }
        for(k = 0;k<R;k++){
            if(grid[k][c-1]=='.') continue;
        }
        grid[k-1][c-1] = '*';
    }

    grid[0][0] = 'c';
    solution_found = true;

    print_solution();
    return;

}

void recurse(int r, int c, int m, int flag, int prev_flag = 0){
    if(solution_found) return;
    if(m<=0){
        if(r<2||c<2) return;
        if(m==-1){
            special_case(r,c,m,flag,prev_flag);
            return;
        }

            //cerr<<"YAH"<<endl;

        for(int i = r;i<R;i++){
            for(int j=0;j<C;j++){
                grid[i][j] = '*';
            }
        }

        for(int i = c;i<C;i++){
            for(int j=0;j<R;j++){
                grid[j][i] = '*';
            }
        }

        if(prev_flag==ROW){
            for(int i = 0;i>m;i--){
                grid[r][-i] = '.';
            }
        } else {
            for(int i = 0;i>m;i--){
                grid[-i][c] = '.';
            }
        }

        grid[0][0] = 'c';
        solution_found = true;

        print_solution();
        return;
    }


    if(flag==ROW){
        m-=C- (C-c);

        recurse(r-1,c,m,ROW, flag);
        recurse(r-1,c,m,COL, flag);


    }


    else {
        m-= R - (R-r);
        recurse(r, c-1, m, ROW, flag);
        recurse(r, c-1, m, COL, flag);


    }



}

void trivial(){
    if(R==1){
        if(C-M>=1){
            solution_found = true;
            for(int i = 0;i<M;i++){
                grid[0][i]='*';
            }
            grid[0][C-1] = 'c';
            print_solution();

        }
    }
    else{
        if(R-M>=1){
            solution_found = true;
            for(int i = 0;i<M;i++){
                grid[i][0]='*';
            }
            grid[R-1][0] = 'c';
            print_solution();

        }
    }


}

void trivial2(){
    for(int i=0;i<R;i++){
        for(int j=0;j<C;j++){
            grid[i][j] = '*';
        }
    }
    grid[0][0] = 'c';
    solution_found = true;
    print_solution();

}

bool find_solution(){
    if(R==1||C==1){
        trivial();
    } else if (M==R*C-1){
        trivial2();
    } else {
        recurse(R, C, M, ROW);
        recurse(R, C, M, COL);
    }

    return solution_found;
}

void init(){
    memset(grid, '.', sizeof(char)*50*50);
    cin>>R>>C>>M;
    solution_found = false;
}

int main(){
    int _T, __T;
    cin>>_T;
    __T = _T;
    while(_T--){
        cout<<"Case #"<<__T-_T<<":"<<endl;;
        init();

        if(M>R*C || !find_solution()){
            cout<<"Impossible"<<endl;
        }

    }
    return 0;

}

