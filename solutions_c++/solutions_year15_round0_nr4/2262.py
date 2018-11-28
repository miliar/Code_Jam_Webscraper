#include <iostream>
#include <fstream>
using namespace std;
bool ans[5][5][5];
int main() {
    int t,a,b,c,i,j;
    ifstream cinn("c.in");
    ofstream coutt("txt.in");
    cinn>>t;
    for(i=1;i<=4;i++) {
        for(j=1;j<=4;j++) {
            ans[1][i][j]=true;
            if(!(i*j%2))ans[2][i][j]=true;
            if(!(i*j%3))ans[3][i][j]=true;
            if(!(i*j%4))ans[4][i][j]=true;
        }
    }
    ans[3][3][1]=false;
    ans[3][1][3]=false;
    ans[4][1][4]=false;
    ans[4][4][1]=false;
    ans[4][2][2]=false;
    ans[4][2][4]=false;
    ans[4][4][2]=false;
    for(i=0;i<t;i++) {
        cinn>>a>>b>>c;
        if(ans[a][b][c]) coutt<<"Case #"<<i+1<<": GABRIEL"<<endl;
        else coutt<<"Case #"<<i+1<<": RICHARD"<<endl;
    }
}
