#include<iostream>
#include<algorithm>
#include<vector>
#include<map>
#include<queue>
#include<set>
#include<cstring>
using namespace std;


int board[100][100];
int R[5] = {-1,1,-1,0,0};
int C[5] = {-1,0,0,1,-1};
int h,w;

bool leads(int r, int c, int dir) {
    r += R[dir];
    c += C[dir];
    while( r >= 0 && r < h && c >= 0 && c < w) {
        if(board[r][c] != 0) return true;
    r += R[dir];
    c += C[dir];

        
    }
    return false;
}


int f() {
    cin>>h>>w;
    for(int i=0;i<h;i++) for(int j=0;j<w;j++) {
        char mv;
        cin>>mv;
        if(mv == '.') board[i][j]=0;
        if(mv == '<') board[i][j]=4;
        if(mv == '>') board[i][j]=3;
        if(mv == 'v') board[i][j]=1;
        if(mv == '^') board[i][j]=2;
    }
    int result = 0;
    

    for(int i=0;i<h;i++) {
        for(int j=0;j<w;j++) {
            if(board[i][j]) {
                if(!leads(i,j,board[i][j])) {
                    bool fails = true;
                    for(int d = 1; d <= 4; d++) {
                        if(leads(i,j,d)) fails=false;
                    }
                    if(fails) return -1;
                    result++;
                }

            }
        }
    }
    return result;
}

int main() {

    int t;
    cin>>t;
    for(int a=1;a<=t;a++) {
     cout<<"Case #"<<a<<": ";
        int v = f();
        if(v==-1) cout<<"IMPOSSIBLE\n";
        else cout<<v<<endl;
    }
}
